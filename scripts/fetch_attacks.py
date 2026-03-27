#!/usr/bin/env python3
"""Fetch Cloudflare Radar attack time-series and save it for the front-end chart."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_BASE = "https://api.cloudflare.com/client/v4"
OUTPUT_PATH = Path("assets/data/attacks.json")
ISO_FMT = "%Y-%m-%dT%H:%M:%SZ"


def _read_token() -> str:
    token = os.environ.get("CF_API_TOKEN", "").strip()
    if not token:
        raise RuntimeError("CF_API_TOKEN is missing")
    return token


def _build_candidate_urls(start_dt: datetime, end_dt: datetime) -> list[str]:
    start_iso = start_dt.strftime(ISO_FMT)
    end_iso = end_dt.strftime(ISO_FMT)

    queries = [
        {
            "dateStart": start_iso,
            "dateEnd": end_iso,
            "aggInterval": "4h",
            "format": "json",
        },
        {
            "dateStart": start_iso,
            "dateEnd": end_iso,
            "aggInterval": "4h",
        },
        {
            "dateRange": "1d",
            "aggInterval": "4h",
            "format": "json",
        },
        {
            "dateRange": "1d",
            "aggInterval": "4h",
        },
    ]

    paths = [
        "/radar/attacks/layer7/timeseries",
        "/radar/attacks/layer7/timeseries_groups",
        "/radar/attacks/layer3/timeseries",
        "/radar/attacks/layer3/timeseries_groups",
    ]

    urls: list[str] = []
    for path in paths:
        for query in queries:
            urls.append(f"{API_BASE}{path}?{urlencode(query)}")

    return urls


def _request_json(url: str, token: str) -> dict:
    req = Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="GET",
    )

    with urlopen(req, timeout=30) as resp:
        payload = resp.read().decode("utf-8")
        return json.loads(payload)


def _normalize_label(raw_value: str, fallback_idx: int) -> str:
    if not raw_value:
        return f"Point {fallback_idx + 1}"

    normalized = raw_value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
        return parsed.strftime("%H:%M")
    except ValueError:
        return raw_value[-8:-3] if len(raw_value) >= 8 else raw_value


def _extract_points(node: object, points: list[tuple[str, float]]) -> None:
    if isinstance(node, dict):
        has_time = any(k in node for k in ("datetime", "timestamp", "time", "date"))
        number_keys = (
            "value",
            "count",
            "requests",
            "attacks",
            "mitigated",
            "sum",
            "total",
        )

        numeric_value = None
        for key in number_keys:
            current = node.get(key)
            if isinstance(current, (int, float)):
                numeric_value = float(current)
                break

        if has_time and numeric_value is not None:
            raw_time = (
                node.get("datetime")
                or node.get("timestamp")
                or node.get("time")
                or node.get("date")
                or ""
            )
            points.append((str(raw_time), numeric_value))

        for value in node.values():
            _extract_points(value, points)

    elif isinstance(node, list):
        for item in node:
            _extract_points(item, points)


def _build_chart_payload(raw_payload: dict) -> dict:
    root = raw_payload.get("result", raw_payload)
    points: list[tuple[str, float]] = []
    _extract_points(root, points)

    if not points:
        raise RuntimeError("No usable time-series points in Cloudflare response")

    collapsed: dict[str, float] = {}
    for ts, value in points:
        collapsed[ts] = collapsed.get(ts, 0.0) + value

    ordered = sorted(collapsed.items(), key=lambda item: item[0])

    labels = [_normalize_label(ts, idx) for idx, (ts, _) in enumerate(ordered)]
    values = [round(value, 2) for _, value in ordered]

    return {
        "source": "cloudflare-radar",
        "updated_at": datetime.now(timezone.utc).strftime(ISO_FMT),
        "labels": labels,
        "values": values,
        "meta": {
            "points": len(values),
        },
    }


def main() -> int:
    token = _read_token()

    end_dt = datetime.now(timezone.utc)
    start_dt = end_dt - timedelta(days=1)

    last_error: Exception | None = None
    for candidate in _build_candidate_urls(start_dt, end_dt):
        try:
            response_payload = _request_json(candidate, token)

            if response_payload.get("success") is False:
                errors = response_payload.get("errors") or "Unknown API error"
                raise RuntimeError(str(errors))

            chart_payload = _build_chart_payload(response_payload)

            OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
            OUTPUT_PATH.write_text(
                json.dumps(chart_payload, ensure_ascii=True, indent=2) + "\n",
                encoding="utf-8",
            )

            print(f"Saved {OUTPUT_PATH} with {chart_payload['meta']['points']} points")
            return 0
        except (URLError, RuntimeError, json.JSONDecodeError) as exc:
            last_error = exc
            continue

    print(f"Failed to fetch Cloudflare attack data: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
