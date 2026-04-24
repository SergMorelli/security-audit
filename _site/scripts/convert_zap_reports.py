#!/usr/bin/env python3
"""
Convert ZAP report HTML files from flat <pre> plain-text content
to properly structured HTML with section headings, tables, lists, etc.
Text content is preserved exactly; only HTML structure and CSS are added.
"""

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

FILES = [
    (BASE / "zap-reports/comprehensive/en/zap-reports-general-en.html", "en", "ltr", "comprehensive"),
    (BASE / "zap-reports/comprehensive/ar/zap-reports-general-ar.html", "ar", "rtl", "comprehensive"),
    (BASE / "zap-reports/executive/en/zap-reports-general-en.html",     "en", "ltr", "executive"),
    (BASE / "zap-reports/executive/ar/zap-reports-general-ar.html",     "ar", "rtl", "executive"),
    (BASE / "zap-reports/management/en/zap-reports-general-en.html",    "en", "ltr", "management"),
    (BASE / "zap-reports/management/ar/zap-reports-general-ar.html",    "ar", "rtl", "management"),
    (BASE / "zap-reports/technical/en/zap-reports-technical-en.html",   "en", "ltr", "technical"),
    (BASE / "zap-reports/technical/ru/zap-reports-technical-ru.html",   "ru", "ltr", "technical"),
    (BASE / "zap-reports/technical/ar/zap-reports-technical-ar.html",   "ar", "rtl", "technical"),
]

# Accent colour per report type (CSS custom property value)
ACCENT = {
    "comprehensive": "#1565c0",
    "executive":     "#b71c1c",
    "management":    "#2e7d32",
    "technical":     "#0d47a1",
}

# ─────────────────────────────────────────────────────────── CSS ──────────────

def build_css(accent: str, font_family: str) -> str:
    return f"""
    *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: {font_family};
      background: linear-gradient(135deg, #eef2f7 0%, #d5e0ef 100%);
      color: #1a2332;
      line-height: 1.75;
      font-size: 15.5px;
    }}
    main {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 40px 20px 70px;
    }}

    /* ── Header ── */
    .report-header {{
      background: linear-gradient(135deg, {accent} 0%, #0a1628 100%);
      color: #fff;
      padding: 52px 48px;
      margin-bottom: 36px;
      border-radius: 14px;
      box-shadow: 0 12px 40px rgba(0,0,0,.22);
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
    .report-header::before {{
      content: '';
      position: absolute;
      inset: 0;
      background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
      pointer-events: none;
    }}
    .report-header h1 {{
      font-size: 1.95em;
      font-weight: 700;
      margin-bottom: 12px;
      position: relative;
      line-height: 1.3;
    }}
    .report-header .subtitle {{
      font-size: 1.05em;
      opacity: .85;
      margin-bottom: 6px;
      position: relative;
    }}
    .report-header .meta {{
      font-size: .9em;
      opacity: .65;
      position: relative;
    }}
    .tool-badge {{
      display: inline-block;
      background: rgba(255,255,255,.12);
      border: 1px solid rgba(255,255,255,.22);
      color: rgba(255,255,255,.9);
      padding: 6px 18px;
      border-radius: 50px;
      font-size: .82em;
      margin-top: 18px;
      position: relative;
      letter-spacing: .04em;
    }}

    /* ── Sections ── */
    .section {{
      background: #fff;
      padding: 34px 40px;
      margin-bottom: 26px;
      border-radius: 12px;
      box-shadow: 0 2px 18px rgba(0,0,0,.07);
      border-top: 3px solid {accent};
    }}

    /* ── Headings ── */
    h2 {{
      font-size: 1.55em;
      color: {accent};
      margin-bottom: 22px;
      padding-bottom: 10px;
      border-bottom: 2px solid #e4e9f0;
      font-weight: 700;
    }}
    h3 {{
      font-size: 1.15em;
      color: #1a2332;
      margin-top: 24px;
      margin-bottom: 12px;
      font-weight: 600;
      padding-left: 10px;
      border-left: 3px solid {accent};
    }}
    h4 {{
      font-size: 1.0em;
      color: #2c3e50;
      margin-top: 14px;
      margin-bottom: 8px;
      font-weight: 600;
    }}

    /* ── Alerts ── */
    .alert {{
      padding: 14px 18px;
      border-radius: 8px;
      margin: 18px 0;
      font-weight: 500;
      line-height: 1.6;
    }}
    .alert-critical {{
      background: #fff0f0;
      border-left: 5px solid #c62828;
      color: #b71c1c;
    }}
    .alert-warning {{
      background: #fff8e1;
      border-left: 5px solid #f57c00;
      color: #e65100;
    }}
    .alert-info {{
      background: #e8f4fd;
      border-left: 5px solid {accent};
      color: #0d47a1;
    }}

    /* ── Tables ── */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0 22px;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 1px 8px rgba(0,0,0,.1);
      font-size: .93em;
    }}
    thead {{
      background: {accent};
      color: #fff;
    }}
    th {{
      padding: 12px 14px;
      text-align: left;
      font-weight: 600;
      font-size: .88em;
      letter-spacing: .03em;
    }}
    td {{
      padding: 10px 14px;
      border-bottom: 1px solid #f0f0f0;
      color: #2c3e50;
      vertical-align: top;
    }}
    tbody tr:nth-child(even) {{ background: #fafbfc; }}
    tbody tr:hover {{ background: #eef2f7; transition: background .15s; }}
    tbody tr:last-child td {{ border-bottom: none; }}

    /* KV (key-value) table variant */
    table.kv-table th {{
      background: #f0f4f8;
      color: #1a2332;
      width: 36%;
    }}
    table.kv-table td {{ color: #37474f; }}

    /* ── Lists ── */
    ul, ol {{ margin: 10px 0; padding-left: 22px; }}
    li {{ margin: 6px 0; line-height: 1.65; color: #2c3e50; }}

    ul.checklist {{ list-style: none; padding-left: 0; }}
    ul.checklist li {{ padding: 5px 8px 5px 0; display: flex; align-items: flex-start; gap: 8px; }}
    ul.checklist li::before {{ content: "☐"; color: {accent}; font-size: 1.1em; flex-shrink: 0; }}
    ul.checklist li.done::before {{ content: "☑"; color: #2e7d32; }}

    ul.status-list {{ list-style: none; padding-left: 0; }}
    ul.status-list li {{ padding: 4px 0; }}
    ul.status-list li.ok   {{ color: #2e7d32; }}
    ul.status-list li.fail {{ color: #c62828; }}
    ul.status-list li.warn {{ color: #e65100; }}

    /* ── TOC ── */
    .toc {{ background: #f6f9fc; border-radius: 8px; padding: 20px 26px; }}
    .toc ol {{ counter-reset: toc-cnt; list-style: none; padding: 0; }}
    .toc li {{
      counter-increment: toc-cnt;
      padding: 7px 0;
      border-bottom: 1px solid #e4e9f0;
      color: {accent};
      font-weight: 500;
    }}
    .toc li::before {{
      content: counter(toc-cnt) ". ";
      font-weight: 700;
      min-width: 26px;
      display: inline-block;
    }}
    .toc li:last-child {{ border-bottom: none; }}

    /* ── Code ── */
    code {{
      background: #f4f4f4;
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 1px 5px;
      font-family: 'Cascadia Code', 'Courier New', monospace;
      color: #c62828;
      font-size: .88em;
    }}
    pre.code-block {{
      background: #1e1e2e;
      color: #cdd6f4;
      padding: 20px 22px;
      border-radius: 8px;
      overflow-x: auto;
      margin: 14px 0;
      font-family: 'Cascadia Code', 'Courier New', monospace;
      font-size: .87em;
      line-height: 1.65;
      white-space: pre-wrap;
      word-break: break-word;
    }}

    /* ── Misc ── */
    p {{ margin: 10px 0; color: #2c3e50; }}
    .phase-box {{
      background: #f6f9fc;
      border-radius: 8px;
      padding: 16px 20px;
      margin: 14px 0;
      border: 1px solid #dce6f0;
    }}

    /* ── RTL support ── */
    [dir="rtl"] h3 {{ padding-left: 0; padding-right: 10px; border-left: none; border-right: 3px solid {accent}; }}
    [dir="rtl"] .alert {{ border-left: none; border-right: 5px solid; }}
    [dir="rtl"] .alert-critical {{ border-right-color: #c62828; }}
    [dir="rtl"] .alert-warning  {{ border-right-color: #f57c00; }}
    [dir="rtl"] .alert-info     {{ border-right-color: {accent}; }}
    [dir="rtl"] th {{ text-align: right; }}
    [dir="rtl"] ul, [dir="rtl"] ol {{ padding-left: 0; padding-right: 22px; }}
    [dir="rtl"] ul.checklist li {{ padding-right: 0; }}

    @media print {{
      body {{ background: #fff; }}
      .section {{ box-shadow: none; border: 1px solid #e0e0e0; page-break-inside: avoid; }}
      .report-header {{ box-shadow: none; print-color-adjust: exact; -webkit-print-color-adjust: exact; }}
    }}
"""

# ─────────────────────────────────────── helpers ─────────────────────────────

def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def unesc(t: str) -> str:
    return (t.replace("&amp;", "&").replace("&lt;", "<")
             .replace("&gt;", ">").replace("&quot;", '"').replace("&#39;", "'"))

# Known H2 section heading fragments (used to identify major section starts)
H2_FRAGMENTS = [
    # English
    "Executive Summary", "Executive Technical Summary", "Executive Summary for Managers",
    "Table of Contents", "Analysis Methodology", "Technical Methodology",
    "Scanning Infrastructure",
    "Detailed Vulnerability Analysis", "Vulnerability Deep Dive",
    "OWASP Top 10", "NIST Cybersecurity", "Microsoft Security Baseline",
    "Multi-Framework Compliance", "SOC 2", "ISO 27001 Compliance",
    "Vulnerability Remediation", "DevSecOps Integration", "Monitoring &",
    "Infrastructure Architecture",
    "Strategic Action Plan",
    "Key Business Risks", "Business Impact Analysis", "Key Management Priorities",
    "Team Responsibility Matrix", "Technical Situation",
    "Immediate Actions Required", "Current Situation", "Communication Plan",
    "Investment Plan", "Conclusion", "References",
    # Russian
    "Исполнительное резюме", "Технически", "Оглавление",
    "Методология анализа", "Детальный анализ",
    "Анализ соответствия", "Заключение", "Список источников",
    "Ключевые бизнес", "Анализ влияния", "Стратегический план",
    "Матрица ответственности", "Техническая ситуация",
    # Arabic
    "الملخص التنفيذي", "جدول المحتويات", "منهجية التحليل",
    "التحليل التفصيلي", "تحليل الامتثال", "خطة معالجة",
    "خطة العمل", "الخلاصة", "المراجع",
    "المخاطر الرئيسية", "تحليل تأثير الأعمال",
]

# Code-block trigger patterns
CODE_TRIGGERS = re.compile(
    r'^\s*(security_scanner:|scan_configuration:|passive_rules:|active_rules:|'
    r'response_metrics:|scan_quality:|Content-Security-Policy:|X-Frame-Options:|'
    r'Strict-Transport-Security:|X-Content-Type-Options:|X-XSS-Protection:|'
    r'Referrer-Policy:|Permissions-Policy:|nmap |sslscan |curl |openssl |'
    r'<link |<script |\[|\{|"[a-z_]+":\s|[a-z_]+:\s+(true|false|"|\[)|'
    r'def \w|import \w|from \w+\s+import|class \w|return |print\(|'
    r'if __name__|if len\(sys|elif \w|while \w|'
    r'python3 |python |npm |pip3 |pip |node |bash |sh |'
    r'mkdir |chmod |chown |rm -|cp -|mv |sudo |git |docker |kubectl |'
    r'add_header |Header\s+(set|always)\s|ServerTokens|ServerSignature|'
    r'\w+\s*=\s*\{|\w+\s*=\s*\[|except\b|for \w.*\s+in\s|'
    r'crossorigin=|integrity=|#\s+[./])'
    r'|^[\[\{\}\]]\s*$'
)

ALERT_CRIT = re.compile(
    r'(🚨|CRITICAL\s+(SECURITY\s+)?ALERT|CRITICAL\s+VIOLATION|CRITICAL\s+WARNING'
    r'|CRITICAL\s+RISK\s+ASSESSMENT|تحذير حرج|تنبيه حرج|КРИТИЧЕСКОЕ)',
    re.IGNORECASE,
)
ALERT_WARN = re.compile(r'^(⚠️|WARNING:|CAUTION:|\s*ВНИМАНИЕ|\s*تحذير)', re.IGNORECASE)


def line_kind(s: str) -> str:
    """Classify a stripped line into a coarse kind."""
    if not s:
        return "blank"
    if ALERT_CRIT.match(s):   # anchored match – avoids false positives inside table cells
        return "alert-critical"
    if ALERT_WARN.match(s):
        return "alert-warning"
    if s.startswith("☐") or s.startswith("☑"):
        return "checklist"
    if re.match(r"^[•·]\s", s):
        return "bullet"
    if re.match(r"^✅", s):
        return "status-ok"
    if re.match(r"^❌", s):
        return "status-fail"
    if re.match(r"^⚠️", s):
        return "status-warn"
    if re.match(r"^\d+\.\s+\S", s):
        return "numbered"
    return "text"


def is_h2(s: str) -> bool:
    for frag in H2_FRAGMENTS:
        if s.startswith(frag):
            return True
    return False


def is_heading_like(s: str) -> bool:
    """Heuristic: could this be an H3 sub-heading?"""
    if not s or len(s) < 3 or len(s) > 90:
        return False
    if re.match(r"^[•·☐☑✅❌🚨\[\(#]", s):
        return False
    if s.startswith("- ") or s.startswith("+ ") or s.startswith("* "):
        return False  # YAML/markdown list items are not headings
    if re.search(r'crossorigin=|integrity=|<[/\w][^>]*>', s):
        return False  # HTML attribute/tag fragments    # Single lowercase word or lowercase function call → likely code, not a heading
    if " " not in s and s[:1].islower():
        return False
    if "(" in s and s[:1].islower():
        return False  # function call expression    if s.endswith(".") and len(s) > 60:
        return False
    return True


def try_multiline_table(lines: list[str]) -> tuple | None:
    """
    Detect a multi-line table (one cell per line) using emoji-position analysis.
    Risk/severity emojis (🔴🟡🔵ℹ️) must appear at a consistent column index in
    every data row – that column index is used to infer the column count K.
    Returns (headers, rows) or None.
    """
    n = len(lines)
    if n < 6:
        return None

    # Positions of status/risk emoji cells in the full block
    emoji_pos = [
        i for i, ln in enumerate(lines)
        if re.match(r"^[🔴🟡🔵ℹ️❌⚠️✅]", ln)
    ]
    if not emoji_pos:
        return None   # no structural markers → can't reliably detect table

    first_ep = emoji_pos[0]

    # Try K from largest (most specific) to 2 (least)
    for k in range(min(6, n) - 1, 1, -1):
        remaining = n - k
        if remaining <= 0 or remaining % k != 0:
            continue

        # Headers must be before the first emoji and short/plain
        headers = lines[:k]
        if not all(
            len(h) <= 65
            and not re.match(r"^[🔴🟡🔵ℹ️🚨⚠️✅❌☐☑]", h)
            for h in headers
        ):
            continue

        # First emoji must be in the FIRST data row: k ≤ first_ep < 2k
        if not (k <= first_ep < 2 * k):
            continue

        # All emoji cells must share the same column offset
        offsets = {(ep - k) % k for ep in emoji_pos}
        if len(offsets) != 1:
            continue

        rest = lines[k:]
        rows = [rest[i: i + k] for i in range(0, len(rest), k)]
        rows = [r for r in rows if len(r) == k]
        if rows:
            return headers, rows

    return None


def render_table(headers: list[str], rows: list[list[str]]) -> str:
    thead = "<tr>" + "".join(f"<th>{esc(h)}</th>" for h in headers) + "</tr>"
    tbody = "".join(
        "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>"
        for row in rows
    )
    return f"<table><thead>{thead}</thead><tbody>{tbody}</tbody></table>"


# ─────────────────────────────── main converter ───────────────────────────────

class Converter:
    def __init__(self, lang: str, direction: str, report_type: str):
        self.lang = lang
        self.direction = direction
        self.report_type = report_type
        self.out: list[str] = []
        self._in_section = False
        self._list_type: str | None = None   # 'ul' | 'ol' | 'checklist' | 'status'
        self._pending_h3: str | None = None  # buffered potential heading
        self._toc_mode = False
        self._toc_items: list[str] = []

    # ── output helpers ────────────────────────────────────────────────────────

    def emit(self, html: str):
        self.out.append(html)

    def close_list(self):
        if self._list_type in ("ul", "bullet"):
            self.emit("</ul>")
        elif self._list_type == "ol":
            self.emit("</ol>")
        elif self._list_type == "checklist":
            self.emit("</ul>")
        elif self._list_type == "status":
            self.emit("</ul>")
        self._list_type = None

    def flush_pending_h3(self):
        if self._pending_h3 is not None:
            self.emit(f"<h3>{esc(self._pending_h3)}</h3>")
            self._pending_h3 = None

    def open_section(self, h2_text: str):
        self.flush_toc()
        self.close_list()
        self.flush_pending_h3()
        if self._in_section:
            self.emit("</div>")
        self.emit('<div class="section">')
        self.emit(f"<h2>{esc(h2_text)}</h2>")
        self._in_section = True
        self._toc_mode = h2_text.lower() in (
            "table of contents", "оглавление", "جدول المحتويات"
        ) or re.search(r"table of contents|оглавление|جدول المحتويات", h2_text, re.IGNORECASE)

    def flush_toc(self):
        if self._toc_mode and self._toc_items:
            self.emit('<div class="toc"><ol>')
            for item in self._toc_items:
                self.emit(f"  <li>{esc(item)}</li>")
            self.emit("</ol></div>")
        self._toc_mode = False
        self._toc_items = []

    def ensure_section(self):
        if not self._in_section:
            self.emit('<div class="section">')
            self._in_section = True

    # ── block rendering ───────────────────────────────────────────────────────

    def emit_alert(self, text: str, kind: str = "critical"):
        self.close_list()
        self.flush_pending_h3()
        css = "alert-critical" if kind == "critical" else "alert-warning"
        self.emit(f'<div class="alert {css}">{esc(text)}</div>')

    def emit_list_item(self, kind: str, text: str):
        if kind == "bullet":
            if self._list_type != "ul":
                self.close_list()
                self.flush_pending_h3()
                self.emit("<ul>")
                self._list_type = "ul"
            item = re.sub(r"^[•·]\s+", "", text)
            self.emit(f"  <li>{esc(item)}</li>")

        elif kind == "checklist":
            if self._list_type != "checklist":
                self.close_list()
                self.flush_pending_h3()
                self.emit('<ul class="checklist">')
                self._list_type = "checklist"
            done = text.startswith("☑")
            item = re.sub(r"^[☐☑]\s*", "", text)
            cls = ' class="done"' if done else ""
            self.emit(f"  <li{cls}>{esc(item)}</li>")

        elif kind in ("status-ok", "status-fail", "status-warn"):
            if self._list_type != "status":
                self.close_list()
                self.flush_pending_h3()
                self.emit('<ul class="status-list">')
                self._list_type = "status"
            cls_map = {"status-ok": "ok", "status-fail": "fail", "status-warn": "warn"}
            self.emit(f'  <li class="{cls_map[kind]}">{esc(text)}</li>')

        elif kind == "numbered":
            if self._list_type != "ol":
                self.close_list()
                self.flush_pending_h3()
                self.emit("<ol>")
                self._list_type = "ol"
            item = re.sub(r"^\d+\.\s+", "", text)
            self.emit(f"  <li>{esc(item)}</li>")

    def emit_para(self, text: str):
        self.close_list()
        self.flush_pending_h3()
        self.emit(f"<p>{esc(text)}</p>")

    # ── multi-line block processing ───────────────────────────────────────────

    def process_short_block(self, block: list[str], lookahead_first: str):
        """
        Process a run of consecutive short 'plain text' lines (no colon,
        no emoji at start).  Decide whether they form a table, a list, or
        headings.
        """
        # Check if what follows looks like table data (starts with emoji/number/%)
        data_start = bool(
            lookahead_first
            and re.match(r"^[🔴🟡🔵ℹ️✅❌☐☑•·\d]", lookahead_first)
        )
        if data_start and len(block) >= 2:
            # The block is table headers; data rows follow
            return block, True   # signal: need table data collection
        if len(block) == 1:
            return block, False  # single heading-like line
        # Multiple short lines not followed by table data → render as simple list
        return block, False

    # ── main entry ────────────────────────────────────────────────────────────

    def convert(self, raw_text: str) -> str:
        text = unesc(raw_text)
        lines = text.split("\n")

        # ── 1. Title block ────────────────────────────────────────────────────
        # First 1–4 non-blank lines before first recognised section heading or
        # the first long paragraph.  Lines with ≥5 leading spaces are ASCII-art
        # centred text; strip the padding.
        title_lines: list[str] = []
        start_i = 0
        for i, line in enumerate(lines):
            raw_stripped = re.sub(r"^\s{5,}", "", line).strip()
            if not raw_stripped:
                if title_lines:
                    start_i = i + 1
                    break
                continue
            if title_lines and (is_h2(raw_stripped) or len(raw_stripped) > 100):
                start_i = i
                break
            title_lines.append(raw_stripped)
            if len(title_lines) >= 5:
                start_i = i + 1
                break

        # Render header block
        report_title = title_lines[0] if title_lines else "ZAP Security Report"
        role_line    = title_lines[1] if len(title_lines) > 1 else ""
        date_line    = title_lines[2] if len(title_lines) > 2 else ""

        self.emit('<div class="report-header">')
        self.emit(f"  <h1>{esc(report_title)}</h1>")
        if role_line:
            self.emit(f'  <p class="subtitle">{esc(role_line)}</p>')
        if date_line:
            self.emit(f'  <p class="meta">{esc(date_line)}</p>')
        self.emit(
            '  <span class="tool-badge">OWASP ZAP 2.17.0 &mdash; Checkmarx Security Platform</span>'
        )
        self.emit("</div>")

        # ── 2. Body lines ─────────────────────────────────────────────────────
        i = start_i
        n = len(lines)
        code_buf: list[str] = []
        in_code = False

        while i < n:
            raw = lines[i]
            s = re.sub(r"^\s{5,}", "", raw).strip()   # strip ASCII-art indent

            if not s:
                if in_code:
                    self.emit(
                        f'<pre class="code-block">'
                        + "\n".join(esc(l) for l in code_buf)
                        + "</pre>"
                    )
                    code_buf.clear(); in_code = False
                self.close_list()
                i += 1
                continue

            # ── code block ───────────────────────────────────────────────
            if CODE_TRIGGERS.match(s) or (in_code and raw.startswith((" ", "\t"))):
                if not in_code:
                    self.flush_pending_h3(); self.close_list()
                    in_code = True
                code_buf.append(raw)
                i += 1
                continue
            if in_code:
                self.emit(
                    f'<pre class="code-block">'
                    + "\n".join(esc(l) for l in code_buf)
                    + "</pre>"
                )
                code_buf.clear(); in_code = False

            kind = line_kind(s)

            # ── TOC mode ─────────────────────────────────────────────────
            # In TOC mode we collect every line as a TOC entry.
            # We exit TOC mode the SECOND time we see a line that was
            # already collected (i.e. the duplicate that marks the real
            # section start).
            if self._toc_mode:
                # Strip leading "  1.  " numbering from TOC items
                item_text = re.sub(r"^\s*\d+[\.\)]\s+", "", s).strip() or s
                if item_text in self._toc_items:
                    # Second occurrence → flush TOC, process line as normal
                    self.flush_toc()
                    # fall through to normal processing
                else:
                    self._toc_items.append(item_text)
                    i += 1
                    continue

            # ── H2 section heading ────────────────────────────────────────
            if kind == "text" and is_h2(s):
                self.open_section(s)
                i += 1
                continue

            # ── alerts ───────────────────────────────────────────────────
            if kind == "alert-critical":
                self.ensure_section()
                self.emit_alert(s, "critical")
                i += 1
                continue
            if kind == "alert-warning":
                self.ensure_section()
                self.emit_alert(s, "warning")
                i += 1
                continue

            # ── list items ───────────────────────────────────────────────
            if kind in ("bullet", "checklist", "status-ok", "status-fail",
                        "status-warn", "numbered"):
                self.ensure_section()
                self.emit_list_item(kind, s)
                i += 1
                continue

            # ── key-value line ("Key: value" with non-empty value) ────────
            kv_match = re.match(r"^([^:\n]{1,50}):\s+(.+)$", s)
            if kv_match and not is_h2(s):
                self.ensure_section()
                self.close_list()
                self.flush_pending_h3()
                key = kv_match.group(1).strip()
                val = kv_match.group(2).strip()
                self.emit(f"<p><strong>{esc(key)}:</strong> {esc(val)}</p>")
                i += 1
                continue

            # ── line ending with ":" (sub-heading without a value) ────────
            if s.endswith(":") and len(s) <= 80 and not is_h2(s):
                clean = s[:-1]
                # Single-word all-lowercase → YAML key (repos: hooks: stages:)
                # Python control-flow lines → not a heading
                is_code_key = (
                    (" " not in clean and clean[:1:].islower())
                    or bool(re.match(r'^(if |elif |while |for |try$|except|with |else$)', clean))
                )
                if not is_code_key:
                    self.ensure_section()
                    self.close_list()
                    self.flush_pending_h3()
                    self.emit(f"<h3>{esc(s)}</h3>")
                    i += 1
                    continue
                # fall through: emit as paragraph via all_short → empty path

            # ── long paragraph text (> 80 chars) ─────────────────────────
            if len(s) > 80:
                self.ensure_section()
                self.close_list()
                self.flush_pending_h3()
                self.emit(f"<p>{esc(s)}</p>")
                i += 1
                continue

            # ── SHORT PLAIN TEXT: collect a run, then classify ────────────
            # Collect consecutive lines that are: kind="text", not H2, not KV,
            # not ending ":", not blank, and len ≤ 80.
            all_short: list[str] = []
            j = i
            while j < n:
                sj = re.sub(r"^\s{5,}", "", lines[j]).strip()
                if not sj:
                    break
                kj = line_kind(sj)
                # Allow status/warning emojis mid-collection: they can be table
                # cells (e.g. ❌ Non-Compliant, ⚠️ Partial Compliance).
                if kj in ("status-ok", "status-fail", "status-warn",
                          "alert-warning") and len(all_short) > 0:
                    pass  # treat as text in table context
                elif kj != "text":
                    break
                if len(sj) > 80 or is_h2(sj):
                    break
                if re.match(r"^[^:\n]{1,50}:\s+.+$", sj):  # KV
                    break
                if sj.endswith(":"):  # sub-heading line
                    break
                # Once we have ≥4 lines, stop if current line looks like a new
                # sub-heading (≥2 words AND followed by a colon-line or KV).
                if len(all_short) >= 4 and len(sj.split()) >= 2 and j + 1 < n:
                    nxt = re.sub(r"^\s{5,}", "", lines[j + 1]).strip()
                    if nxt.endswith(":") or re.match(r"^[^:\n]{1,50}:\s+.+$", nxt):
                        break
                all_short.append(sj)
                j += 1

            if not all_short:
                self.ensure_section()
                self.emit_para(s)
                i += 1
                continue

            # ── 1) First line may be a heading that precedes a table ─────────
            if len(all_short) > 1 and len(all_short[0].split()) >= 3:
                rest = all_short[1:]
                table = try_multiline_table(rest)
                if table:
                    headers, rows = table
                    self.ensure_section()
                    self.close_list()
                    self.flush_pending_h3()
                    self.emit(f"<h3>{esc(all_short[0])}</h3>")
                    self.emit(render_table(headers, rows))
                    i = j
                    continue

            # ── 2) Try the whole block as a multi-line table ──────────────
            table = try_multiline_table(all_short)
            if table:
                headers, rows = table
                self.ensure_section()
                self.close_list()
                self.flush_pending_h3()
                self.emit(render_table(headers, rows))
                i = j
                continue

            # ── 3) First line is a heading (≥3 words), rest is a table ────
            if len(all_short) > 1 and len(all_short[0].split()) >= 3:
                rest = all_short[1:]
                table = try_multiline_table(rest)
                if table:
                    headers, rows = table
                    self.ensure_section()
                    self.close_list()
                    self.flush_pending_h3()
                    self.emit(f"<h3>{esc(all_short[0])}</h3>")
                    self.emit(render_table(headers, rows))
                    i = j
                    continue

            # ── 4) Single line → pending H3 ───────────────────────────────
            if len(all_short) == 1:
                self.ensure_section()
                self.close_list()
                if is_heading_like(all_short[0]):
                    self._pending_h3 = all_short[0]
                else:
                    self.flush_pending_h3()
                    self.emit_para(all_short[0])
                i = j
                continue

            # ── 5) Multiple short lines – sentence vs. label heuristic ────
            self.ensure_section()
            self.close_list()
            self.flush_pending_h3()
            word_counts = [len(x.split()) for x in all_short]
            avg_words = sum(word_counts) / len(word_counts)
            if avg_words >= 5:
                # Mostly prose sentences → render as paragraphs
                for x in all_short:
                    self.emit(f"<p>{esc(x)}</p>")
            else:
                # Short labels → render as a list
                self.emit("<ul>")
                for x in all_short:
                    self.emit(f"  <li>{esc(x)}</li>")
                self.emit("</ul>")
            i = j

        # ── finalise ─────────────────────────────────────────────────────────
        if in_code and code_buf:
            self.emit(
                f'<pre class="code-block">'
                + "\n".join(esc(l) for l in code_buf)
                + "</pre>"
            )
        self.flush_toc()
        self.close_list()
        self.flush_pending_h3()
        if self._in_section:
            self.emit("</div>")

        return "\n".join(self.out)


# ────────────────────────────────────── file processor ───────────────────────

def process_file(file_path: Path, lang: str, direction: str, report_type: str):
    src = file_path.read_text(encoding="utf-8")

    # Extract page title
    title_m = re.search(r"<title>(.*?)</title>", src)
    page_title = title_m.group(1) if title_m else "ZAP Report"

    # Extract pre content (the main flat-text block)
    pre_m = re.search(r"<pre>\s*(.*?)\s*</pre>", src, re.DOTALL)
    if not pre_m:
        print(f"  ⚠ No <pre> block found: {file_path.name}")
        return

    raw_text = pre_m.group(1)

    accent = ACCENT.get(report_type, "#1565c0")
    font = (
        "'Noto Sans Arabic', 'Noto Sans', 'Segoe UI', sans-serif"
        if lang == "ar"
        else "'Segoe UI', 'Noto Sans', 'DejaVu Sans', sans-serif"
    )

    css = build_css(accent, font)
    conv = Converter(lang, direction, report_type)
    body_html = conv.convert(raw_text)

    output = f"""<!doctype html>
<html lang="{lang}" dir="{direction}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(page_title)}</title>
  <style>{css}
  </style>
</head>
<body>
  <main>
{body_html}
  </main>
</body>
</html>"""

    file_path.write_text(output, encoding="utf-8")
    print(f"  ✓ {file_path.relative_to(BASE)}")


# ──────────────────────────────────────────────────────────────── entry ───────

if __name__ == "__main__":
    print("Converting ZAP report HTML files …")
    for file_path, lang, direction, report_type in FILES:
        if file_path.exists():
            process_file(file_path, lang, direction, report_type)
        else:
            print(f"  ✗ NOT FOUND: {file_path}")
    print("Done.")
