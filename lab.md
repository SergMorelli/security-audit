---
layout: default
title: Lab
permalink: /lab/
lang: en
translation_key: lab
---

<section class="pt-32 pb-20 text-center">
  <h1 class="text-4xl text-cyan-400 mb-6">Security Lab</h1>
  <p class="text-gray-400">Demonstration of IDS systems, attack simulations, and infrastructure setups.</p>
</section>

<!-- ── Filter bar ─────────────────────────────────────────────────── -->
<section class="max-w-6xl mx-auto px-4 pb-8" data-lab-filter>
  <div class="overflow-x-auto">
    <div class="flex min-w-max items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="ids">🛡️ IDS Systems</button>
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="attacks">⚔️ Attack Simulations</button>
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="infrastructure">🖧 Infrastructure</button>
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="defense">🧱 Line of Defense</button>
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="osi">🧅 OSI Layers</button>
    </div>
  </div>
  <div id="labFilterDescription" class="mt-4 rounded-lg bg-slate-900/40 ring-1 ring-cyan-400/20 px-4 py-3">
    <h3 id="labFilterDescriptionTitle" class="text-sm sm:text-base text-cyan-200 font-semibold"></h3>
    <p id="labFilterDescriptionAudience" class="mt-1 text-sm text-gray-300"></p>
    <p id="labFilterDescriptionFocus" class="mt-1 text-sm text-gray-400"></p>
  </div>
</section>

<style>
  .lab-card {
    border: 1px solid rgba(71, 85, 105, 0.65);
    background: linear-gradient(165deg, rgba(8, 14, 28, 0.96), rgba(2, 8, 23, 0.86));
    padding-top: 2.4rem;
    padding-left: 2rem;
    padding-right: 1.25rem;
    padding-bottom: 1.25rem;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }

  .lab-title {
    margin-top: 0.5rem;
    padding-left: 0.5rem;
    transition: color 0.2s ease, text-shadow 0.2s ease;
  }

  .lab-layer-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.2rem 0.65rem;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    border-radius: 9999px;
    border: 1px solid rgba(34, 211, 238, 0.4);
    color: rgb(103, 232, 249);
    background: rgba(34, 211, 238, 0.08);
  }

  .lab-diagram {
    margin-top: 0.5rem;
    padding: 1.1rem 1.25rem;
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 0.6rem;
    background: rgba(2, 8, 23, 0.85);
    color: rgb(165, 243, 252);
    font-size: 0.78rem;
    line-height: 1.5;
    overflow-x: auto;
    white-space: pre;
  }

  .lab-checklist {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.25rem;
  }

  .lab-check-item {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.35rem 0.75rem;
    font-size: 0.75rem;
    border-radius: 9999px;
    border: 1px solid rgba(74, 222, 128, 0.35);
    color: rgb(134, 239, 172);
    background: rgba(74, 222, 128, 0.08);
  }

  .lab-legend {
    margin-top: 0.25rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 0.65rem 1.5rem;
  }

  .lab-legend dt {
    color: rgb(103, 232, 249);
    font-weight: 600;
    font-size: 0.85rem;
  }

  .lab-legend dd {
    margin: 0;
    color: rgb(148, 163, 184);
    font-size: 0.8rem;
    line-height: 1.4;
  }

  .lab-list {
    margin-top: 0.25rem;
    padding-left: 1.1rem;
    list-style: disc;
    color: rgb(148, 163, 184);
    font-size: 0.85rem;
    line-height: 1.6;
  }

  .lab-list li {
    margin-bottom: 0.2rem;
  }

  @media (hover: hover) {
    .lab-card:hover {
      transform: translateY(-6px);
      border-color: rgba(34, 211, 238, 0.85);
      box-shadow: 0 0 0 1px rgba(34, 211, 238, 0.35), 0 0 28px rgba(34, 211, 238, 0.35);
    }

    .lab-card:hover .lab-title {
      color: rgb(34, 211, 238);
      text-shadow: 0 0 16px rgba(34, 211, 238, 0.45);
    }

    [data-lab-category="defense"] .lab-card:hover {
      border-color: rgba(248, 113, 113, 0.95);
      box-shadow: 0 0 0 1px rgba(248, 113, 113, 0.7), 0 0 18px rgba(239, 68, 68, 0.55), 0 0 42px rgba(185, 28, 28, 0.45);
    }

    [data-lab-category="osi"] .lab-card:hover {
      border-color: rgba(192, 132, 252, 0.95);
      box-shadow: 0 0 0 1px rgba(192, 132, 252, 0.7), 0 0 18px rgba(168, 85, 247, 0.55), 0 0 42px rgba(126, 34, 206, 0.45);
    }
  }
</style>

<!-- ── Lab Cards ──────────────────────────────────────────────────── -->
<section class="max-w-6xl mx-auto px-4 pb-20 space-y-14">

  <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-x-8 gap-y-10">

    <!-- IDS Systems -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="ids">
      <h3 class="lab-title text-xl font-semibold text-slate-100 leading-tight">Suricata Network IDS</h3>
      <p class="text-xs text-slate-400">Tools: Suricata, tcpdump, Wireshark</p>
      <p class="text-sm text-gray-400">Signature and anomaly-based detection lab monitoring simulated traffic in real time.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="ids">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Snort Ruleset Evaluation</h3>
      <p class="text-xs text-slate-400">Tools: Snort, PCAP replay</p>
      <p class="text-sm text-gray-400">Custom detection rules tested against known attack traffic samples.</p>
    </article>

    <!-- Attack Simulations -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="attacks">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Web Application Attack Simulation</h3>
      <p class="text-xs text-slate-400">Tools: Burp Suite, OWASP ZAP</p>
      <p class="text-sm text-gray-400">Exploitation attempts covering OWASP Top 10 categories against an isolated test target.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="attacks">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Simulated Phishing &amp; Social Engineering</h3>
      <p class="text-xs text-slate-400">Tools: GoPhish, custom templates</p>
      <p class="text-sm text-gray-400">Controlled phishing campaign to assess user awareness and email filtering.</p>
    </article>

    <!-- Infrastructure: Monitoring & Alerting Architecture -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="infrastructure">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Monitoring &amp; Alerting Architecture</h3>
      <p class="text-xs text-slate-400">Tools: Suricata, EveBox, Filebeat, Elasticsearch, Node Exporter, Prometheus, Promtail, Loki, Grafana, Caddy</p>
      <p class="text-sm text-gray-400">Suricata inspects all inbound traffic and emits alerts only (eve.json) — forwarded to EveBox for analyst triage and to Elasticsearch via Filebeat. System metrics and logs flow through Prometheus/Promtail into Loki and Grafana for a live SOC dashboard, served over HTTPS via Caddy.</p>

      <pre class="lab-diagram">                    Internet
                        │
                    Suricata
                        │
              eve.json (alerts only)
                        │
        ┌───────────────┴───────────────┐
        │                               │
     EveBox                        Filebeat
(alert analyst UI)                      │
                                         ▼
                                  Elasticsearch
                                  (alerts only)

Node Exporter ──▶ Prometheus ──┐
                                │
System logs ─▶ Promtail ─▶ Loki ┤
                                ▼
                            Grafana
                     (LIVE SOC Dashboard)
                                │
                              Caddy
                         (HTTPS access)</pre>

      <div class="lab-checklist">
        <span class="lab-check-item">✅ VPS ~4 GB RAM</span>
        <span class="lab-check-item">✅ Suricata as IDS</span>
        <span class="lab-check-item">✅ Sleek cyberpunk dashboard</span>
        <span class="lab-check-item">✅ LIVE attack map in Grafana</span>
        <span class="lab-check-item">✅ No nginx → Caddy</span>
        <span class="lab-check-item">✅ Minimal overhead</span>
        <span class="lab-check-item">✅ 100% free</span>
      </div>

      <dl class="lab-legend">
        <div><dt>Suricata</dt><dd>Network IDS/IPS engine that inspects traffic and generates alerts (eve.json).</dd></div>
        <div><dt>EveBox</dt><dd>Web UI for analysts to triage and investigate Suricata alerts.</dd></div>
        <div><dt>Filebeat</dt><dd>Lightweight log shipper that forwards eve.json alerts to Elasticsearch.</dd></div>
        <div><dt>Elasticsearch</dt><dd>Indexes alerts only, keeping storage and resource usage minimal.</dd></div>
        <div><dt>Node Exporter</dt><dd>Exposes host-level system metrics (CPU, RAM, disk) for Prometheus.</dd></div>
        <div><dt>Prometheus</dt><dd>Time-series database that scrapes and stores system metrics.</dd></div>
        <div><dt>Promtail</dt><dd>Agent that ships system logs to Loki.</dd></div>
        <div><dt>Loki</dt><dd>Lightweight, label-indexed log aggregation system built for Grafana.</dd></div>
        <div><dt>Grafana</dt><dd>Visualizes metrics, logs, and alerts as a live SOC dashboard.</dd></div>
        <div><dt>Caddy</dt><dd>Reverse proxy providing automatic HTTPS for the dashboard — no nginx needed.</dd></div>
      </dl>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="infrastructure">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Segmented Lab Network</h3>
      <p class="text-xs text-slate-400">Tools: pfSense, VLANs, virtualization</p>
      <p class="text-sm text-gray-400">VLAN-based network segmentation isolating attacker, target, and monitoring zones.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="infrastructure">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Virtualized SOC Stack</h3>
      <p class="text-xs text-slate-400">Tools: Proxmox/VirtualBox, ELK stack</p>
      <p class="text-sm text-gray-400">Self-hosted monitoring and log aggregation stack for lab telemetry.</p>
    </article>

    <!-- Line of Defense -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Layer 1 · Firewall</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Perimeter Firewall</h3>
      <p class="text-sm text-gray-400">First line of defense — filters traffic at the network perimeter based on rules and zones.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Layer 2 · WAF</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Web Application Firewall</h3>
      <p class="text-sm text-gray-400">Inspects HTTP/S traffic to block common web attacks (SQLi, XSS, and more) before they reach the application.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Layer 3 · IDS/IPS</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Intrusion Detection / Prevention</h3>
      <p class="text-sm text-gray-400">Monitors and blocks malicious network activity that bypasses the perimeter.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Layer 4 · EDR</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Endpoint Detection &amp; Response</h3>
      <p class="text-sm text-gray-400">Provides host-level visibility and response for threats that reach endpoints.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Layer 5 · SIEM</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">SIEM &amp; Log Correlation</h3>
      <p class="text-sm text-gray-400">Centralizes logs across all layers for correlation, alerting, and incident response.</p>
    </article>

    <!-- OSI Layers -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L1 · Physical</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Physical Layer Security</h3>
      <p class="text-sm text-gray-400">Protects the physical medium and physical access to equipment.</p>
      <ul class="lab-list">
        <li>Physical security of server/patch rooms (locks, access control systems, biometrics, cameras)</li>
        <li>Rack access control (lockable cabinets, tamper sensors)</li>
        <li>Cable protection (shielded twisted pair / fiber optics, concealed routing, anti-vandal conduits)</li>
        <li>TEMPEST / electromagnetic emission shielding</li>
        <li>Disabling unused switch ports</li>
        <li>Physical destruction or secure disposal of storage media</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L2 · Data Link</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Data Link Layer Security</h3>
      <p class="text-sm text-gray-400">Protects frames, MAC addresses, and switching.</p>
      <ul class="lab-list">
        <li>Port Security (limiting the number of MAC addresses per port)</li>
        <li>Dynamic ARP Inspection (DAI) + DHCP Snooping</li>
        <li>802.1X (device authentication at the port)</li>
        <li>MAC Filtering / Sticky MAC</li>
        <li>Private VLAN / Isolated VLAN</li>
        <li>Protection against MAC flooding (storm control)</li>
        <li>Data link layer encryption (MACsec)</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L3 · Network</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Network Layer Security</h3>
      <p class="text-sm text-gray-400">Protects routing and IP traffic.</p>
      <ul class="lab-list">
        <li>Firewalls with IP-based filtering</li>
        <li>Access Control Lists (ACL) on routers</li>
        <li>Network segmentation (VLANs + routing between them)</li>
        <li>Anti-spoofing (uRPF — Unicast Reverse Path Forwarding)</li>
        <li>Routing protocol protection (MD5/HMAC authentication for OSPF, BGP, EIGRP)</li>
        <li>Rate-limiting / IP-level DDoS protection</li>
        <li>IPSec (tunnel mode)</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L4 · Transport</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Transport Layer Security</h3>
      <p class="text-sm text-gray-400">Protects TCP/UDP sessions and ports.</p>
      <ul class="lab-list">
        <li>Stateful firewall (connection state tracking)</li>
        <li>Port and protocol filtering</li>
        <li>SYN Cookies / SYN flood protection</li>
        <li>Rate limiting by connection count</li>
        <li>TCP Wrappers</li>
        <li>Blocking known malicious ports</li>
        <li>TLS/SSL (partially overlaps with L4–L7)</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L5 · Session</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Session Layer Security</h3>
      <p class="text-sm text-gray-400">Protects session establishment and management.</p>
      <ul class="lab-list">
        <li>Session control and limits (timeout, max sessions)</li>
        <li>Session hijacking protection (random session IDs, binding to IP/User-Agent)</li>
        <li>RPC filtering and restriction of remote calls</li>
        <li>NetBIOS / SMB session protection</li>
        <li>VPN tunnels with session authentication</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L6 · Presentation</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Presentation Layer Security</h3>
      <p class="text-sm text-gray-400">Protects data format, encryption, and encoding.</p>
      <ul class="lab-list">
        <li>Data encryption (TLS, SSL, AES, etc.)</li>
        <li>Format validation (JSON, XML, ASN.1)</li>
        <li>Protection against encoding attacks (UTF-7, double encoding, etc.)</li>
        <li>Certificates and PKI (certificate chain verification)</li>
        <li>Compression and its safe handling (protection against compression bombs)</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L7 · Application</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Application Layer Security</h3>
      <p class="text-sm text-gray-400">Protects the applications themselves and top-level protocols.</p>
      <ul class="lab-list">
        <li>Web Application Firewall (WAF)</li>
        <li>Input validation / sanitization</li>
        <li>OWASP Top 10 protection (SQLi, XSS, CSRF, RCE, etc.)</li>
        <li>Application-level antivirus / anti-malware</li>
        <li>Application Control / URL Filtering</li>
        <li>DNS Security (DNSSEC, DNS Filtering, Response Policy Zones)</li>
        <li>API gateway with authentication and rate-limiting</li>
        <li>EDR / XDR (host-level application behavior)</li>
        <li>SIEM + application log correlation</li>
      </ul>
    </article>
  </div>

</section>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    var filterRoot = document.querySelector('[data-lab-filter]');
    if (!filterRoot) {
      return;
    }

    var buttons = Array.prototype.slice.call(filterRoot.querySelectorAll('.lab-filter-button'));
    var sections = Array.prototype.slice.call(document.querySelectorAll('.lab-filter-item'));
    var descriptionTitle = document.getElementById('labFilterDescriptionTitle');
    var descriptionAudience = document.getElementById('labFilterDescriptionAudience');
    var descriptionFocus = document.getElementById('labFilterDescriptionFocus');

    var descriptions = {
      ids: {
        title: 'IDS Systems',
        audience: 'For SOC analysts and blue-team engineers evaluating detection coverage.',
        focus: 'Focus: real-time network intrusion detection and alert triage.'
      },
      attacks: {
        title: 'Attack Simulations',
        audience: 'For red-team exercises and vulnerability validation.',
        focus: 'Focus: controlled offensive testing against lab targets to validate defenses.'
      },
      infrastructure: {
        title: 'Infrastructure',
        audience: 'For engineers building and hardening lab environments.',
        focus: 'Focus: segmented networks, virtualization, and monitoring stack setup.'
      },
      defense: {
        title: 'Line of Defense',
        audience: 'Layered security controls modeled after defense-in-depth principles.',
        focus: 'Focus: each layer (Firewall → WAF → IDS/IPS → EDR → SIEM) reduces residual risk.'
      },
      osi: {
        title: 'OSI Layers',
        audience: 'For engineers mapping security controls to the OSI reference model.',
        focus: 'Focus: protective measures organized across all 7 OSI layers, from physical to application.'
      }
    };

    function setFilter(category) {
      buttons.forEach(function (button) {
        var isActive = button.getAttribute('data-filter') === category;
        button.classList.toggle('bg-gradient-to-r', isActive);
        button.classList.toggle('from-cyan-500/25', isActive);
        button.classList.toggle('to-fuchsia-500/15', isActive);
        button.classList.toggle('text-cyan-100', isActive);
        button.classList.toggle('shadow-[0_0_16px_rgba(34,211,238,0.25)]', isActive);
        button.classList.toggle('text-slate-300', !isActive);
        button.classList.toggle('hover:bg-white/5', !isActive);
      });

      sections.forEach(function (section) {
        var matches = section.getAttribute('data-lab-category') === category;
        section.style.display = matches ? '' : 'none';
      });

      if (descriptionTitle && descriptionAudience && descriptionFocus && descriptions[category]) {
        descriptionTitle.textContent = descriptions[category].title;
        descriptionAudience.textContent = descriptions[category].audience;
        descriptionFocus.textContent = descriptions[category].focus;
      }
    }

    buttons.forEach(function (button) {
      button.addEventListener('click', function () {
        setFilter(button.getAttribute('data-filter'));
      });
    });

    if (buttons.length > 0) {
      setFilter(buttons[0].getAttribute('data-filter'));
    }
  });
</script>
