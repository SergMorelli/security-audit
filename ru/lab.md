---
layout: default
title: Лаборатория
permalink: /ru/lab/
lang: ru
translation_key: lab
---

<section class="pt-32 pb-20 text-center">
  <h1 class="text-4xl text-cyan-400 mb-6">Лаборатория безопасности</h1>
  <p class="text-gray-400">Демонстрация IDS-систем, симуляций атак и инфраструктурных стендов.</p>
</section>

<!-- ── Панель фильтров ────────────────────────────────────────────── -->
<section class="max-w-6xl mx-auto px-4 pb-8" data-lab-filter>
  <div class="overflow-x-auto">
    <div class="flex min-w-max items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="ids">🛡️ IDS-системы</button>
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="attacks">⚔️ Симуляции атак</button>
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="infrastructure">🖧 Инфраструктура</button>
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="defense">🧱 Линия защиты</button>
      <button type="button" class="lab-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="osi">🧅 Уровни OSI</button>
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

<!-- ── Карточки лаборатории ───────────────────────────────────────── -->
<section class="max-w-6xl mx-auto px-4 pb-20 space-y-14">

  <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-x-8 gap-y-10">

    <!-- IDS-системы -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="ids">
      <h3 class="lab-title text-xl font-semibold text-slate-100 leading-tight">Сетевая IDS на базе Suricata</h3>
      <p class="text-xs text-slate-400">Инструменты: Suricata, tcpdump, Wireshark</p>
      <p class="text-sm text-gray-400">Сигнатурное и аномальное обнаружение в реальном времени на симулированном трафике.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="ids">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Проверка правил Snort</h3>
      <p class="text-xs text-slate-400">Инструменты: Snort, PCAP replay</p>
      <p class="text-sm text-gray-400">Пользовательские правила обнаружения, проверенные на образцах известного атакующего трафика.</p>
    </article>

    <!-- Симуляции атак -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="attacks">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Симуляция атак на веб-приложение</h3>
      <p class="text-xs text-slate-400">Инструменты: Burp Suite, OWASP ZAP</p>
      <p class="text-sm text-gray-400">Попытки эксплуатации по категориям OWASP Top 10 на изолированной тестовой цели.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="attacks">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Симуляция фишинга и социальной инженерии</h3>
      <p class="text-xs text-slate-400">Инструменты: GoPhish, собственные шаблоны</p>
      <p class="text-sm text-gray-400">Контролируемая фишинговая кампания для оценки осведомлённости пользователей и фильтрации почты.</p>
    </article>

    <!-- Инфраструктура: архитектура мониторинга и алертинга -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="infrastructure">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Архитектура мониторинга и алертинга</h3>
      <p class="text-xs text-slate-400">Инструменты: Suricata, EveBox, Filebeat, Elasticsearch, Node Exporter, Prometheus, Promtail, Loki, Grafana, Caddy</p>
      <p class="text-sm text-gray-400">Suricata анализирует весь входящий трафик и генерирует только алерты (eve.json) — они передаются в EveBox для разбора аналитиком и в Elasticsearch через Filebeat. Системные метрики и логи проходят через Prometheus/Promtail в Loki и Grafana, формируя live-дашборд SOC, который отдаётся по HTTPS через Caddy.</p>

      <pre class="lab-diagram">                    Internet
                        │
                    Suricata
                        │
           eve.json (только алерты)
                        │
        ┌───────────────┴───────────────┐
        │                               │
     EveBox                        Filebeat
(UI для аналитика)                      │
                                         ▼
                                  Elasticsearch
                                  (только алерты)

Node Exporter ──▶ Prometheus ──┐
                                │
Системные логи ─▶ Promtail ─▶ Loki ┤
                                ▼
                            Grafana
                   (LIVE-дашборд SOC)
                                │
                              Caddy
                        (доступ по HTTPS)</pre>

      <div class="lab-checklist">
        <span class="lab-check-item">✅ VPS ~4 ГБ RAM</span>
        <span class="lab-check-item">✅ Suricata в роли IDS</span>
        <span class="lab-check-item">✅ стильный cyberpunk-дашборд</span>
        <span class="lab-check-item">✅ LIVE-карта атак в Grafana</span>
        <span class="lab-check-item">✅ без nginx → Caddy</span>
        <span class="lab-check-item">✅ минимальный overhead</span>
        <span class="lab-check-item">✅ всё бесплатно</span>
      </div>

      <dl class="lab-legend">
        <div><dt>Suricata</dt><dd>Сетевой IDS/IPS-движок, анализирующий трафик и генерирующий алерты (eve.json).</dd></div>
        <div><dt>EveBox</dt><dd>Веб-интерфейс для разбора и расследования алертов Suricata аналитиком.</dd></div>
        <div><dt>Filebeat</dt><dd>Лёгкий агент доставки логов, пересылающий алерты eve.json в Elasticsearch.</dd></div>
        <div><dt>Elasticsearch</dt><dd>Индексирует только алерты, что минимизирует нагрузку на хранилище и ресурсы.</dd></div>
        <div><dt>Node Exporter</dt><dd>Предоставляет системные метрики хоста (CPU, RAM, диск) для Prometheus.</dd></div>
        <div><dt>Prometheus</dt><dd>База данных временных рядов, собирающая и хранящая системные метрики.</dd></div>
        <div><dt>Promtail</dt><dd>Агент, пересылающий системные логи в Loki.</dd></div>
        <div><dt>Loki</dt><dd>Лёгкая система агрегации логов с индексацией по меткам, нативная для Grafana.</dd></div>
        <div><dt>Grafana</dt><dd>Визуализирует метрики, логи и алерты в виде live-дашборда SOC.</dd></div>
        <div><dt>Caddy</dt><dd>Reverse-proxy, обеспечивающий автоматический HTTPS для дашборда — без nginx.</dd></div>
      </dl>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="infrastructure">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Сегментированная лабораторная сеть</h3>
      <p class="text-xs text-slate-400">Инструменты: pfSense, VLAN, виртуализация</p>
      <p class="text-sm text-gray-400">Сегментация сети через VLAN, изолирующая зоны атакующего, цели и мониторинга.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="infrastructure">
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Виртуализированный стек SOC</h3>
      <p class="text-xs text-slate-400">Инструменты: Proxmox/VirtualBox, ELK stack</p>
      <p class="text-sm text-gray-400">Собственный стек мониторинга и агрегации логов для телеметрии лаборатории.</p>
    </article>

    <!-- Линия защиты -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Уровень 1 · Firewall</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Периметровый межсетевой экран</h3>
      <p class="text-sm text-gray-400">Первая линия защиты — фильтрует трафик на периметре сети на основе правил и зон.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Уровень 2 · WAF</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Web Application Firewall</h3>
      <p class="text-sm text-gray-400">Анализирует HTTP/S-трафик и блокирует распространённые веб-атаки (SQLi, XSS и др.) до входа в приложение.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Уровень 3 · IDS/IPS</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Обнаружение и предотвращение вторжений</h3>
      <p class="text-sm text-gray-400">Отслеживает и блокирует вредоносную активность, обошедшую периметр.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Уровень 4 · EDR</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Endpoint Detection &amp; Response</h3>
      <p class="text-sm text-gray-400">Обеспечивает видимость и реагирование на угрозы на уровне конечных устройств.</p>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4" data-lab-category="defense">
      <span class="lab-layer-badge">Уровень 5 · SIEM</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">SIEM и корреляция логов</h3>
      <p class="text-sm text-gray-400">Централизует логи со всех уровней для корреляции, оповещений и реагирования на инциденты.</p>
    </article>

    <!-- Уровни OSI -->
    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L1 · Physical</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Layer 1 — Physical (Физический)</h3>
      <p class="text-sm text-gray-400">Защита носителя и физического доступа к оборудованию.</p>
      <ul class="lab-list">
        <li>Физическая охрана серверных и кроссовых (замки, СКУД, биометрия, камеры)</li>
        <li>Контроль доступа в стойки (запираемые шкафы, тампер-сенсоры)</li>
        <li>Защита кабелей (экранированная витая пара / оптоволокно, скрытая прокладка, антивандальные короба)</li>
        <li>TEMPEST / экранирование от электромагнитных излучений</li>
        <li>Отключение неиспользуемых портов на коммутаторах</li>
        <li>Физическое уничтожение или безопасная утилизация носителей</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L2 · Data Link</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Layer 2 — Data Link (Канальный)</h3>
      <p class="text-sm text-gray-400">Защита на уровне кадров, MAC-адресов и коммутации.</p>
      <ul class="lab-list">
        <li>Port Security (ограничение количества MAC на порте)</li>
        <li>Dynamic ARP Inspection (DAI) + DHCP Snooping</li>
        <li>802.1X (аутентификация устройств на порте)</li>
        <li>MAC Filtering / Sticky MAC</li>
        <li>Private VLAN / Isolated VLAN</li>
        <li>Защита от MAC Flooding (storm control)</li>
        <li>Шифрование на канальном уровне (MACsec)</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L3 · Network</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Layer 3 — Network (Сетевой)</h3>
      <p class="text-sm text-gray-400">Защита маршрутизации и IP-трафика.</p>
      <ul class="lab-list">
        <li>Межсетевые экраны (Firewall) с фильтрацией по IP</li>
        <li>Access Control Lists (ACL) на маршрутизаторах</li>
        <li>Сегментация сети (VLAN + роутинг между ними)</li>
        <li>Anti-spoofing (uRPF — Unicast Reverse Path Forwarding)</li>
        <li>Защита протоколов маршрутизации (MD5/HMAC-аутентификация OSPF, BGP, EIGRP)</li>
        <li>Rate-limiting / защита от DDoS на уровне IP</li>
        <li>IPSec (в туннельном режиме)</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L4 · Transport</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Layer 4 — Transport (Транспортный)</h3>
      <p class="text-sm text-gray-400">Защита TCP/UDP-сессий и портов.</p>
      <ul class="lab-list">
        <li>Stateful Firewall (отслеживание состояния соединений)</li>
        <li>Фильтрация по портам и протоколам</li>
        <li>SYN Cookies / защита от SYN Flood</li>
        <li>Rate limiting по количеству соединений</li>
        <li>TCP Wrappers</li>
        <li>Блокировка известных вредоносных портов</li>
        <li>TLS/SSL (частично пересекается с L4–L7)</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L5 · Session</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Layer 5 — Session (Сеансовый)</h3>
      <p class="text-sm text-gray-400">Защита установления и управления сеансами.</p>
      <ul class="lab-list">
        <li>Контроль и ограничение сессий (timeout, max sessions)</li>
        <li>Защита от Session Hijacking (случайные Session ID, привязка к IP/User-Agent)</li>
        <li>RPC-фильтры и ограничение удалённых вызовов</li>
        <li>Защита NetBIOS / SMB-сессий</li>
        <li>VPN-туннели с аутентификацией сессии</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L6 · Presentation</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Layer 6 — Presentation (Представления)</h3>
      <p class="text-sm text-gray-400">Защита формата данных, шифрования и кодирования.</p>
      <ul class="lab-list">
        <li>Шифрование данных (TLS, SSL, AES и т.д.)</li>
        <li>Проверка и валидация форматов (JSON, XML, ASN.1)</li>
        <li>Защита от атак на кодировки (UTF-7, double encoding и т.п.)</li>
        <li>Сертификаты и PKI (проверка цепочки сертификатов)</li>
        <li>Сжатие и его безопасная обработка (защита от compression bombs)</li>
      </ul>
    </article>

    <article class="lab-filter-item lab-card rounded-xl flex flex-col gap-4 col-span-full" data-lab-category="osi">
      <span class="lab-layer-badge">OSI L7 · Application</span>
      <h3 class="lab-title text-lg font-semibold text-slate-100 leading-tight">Layer 7 — Application (Прикладной)</h3>
      <p class="text-sm text-gray-400">Защита самих приложений и протоколов верхнего уровня.</p>
      <ul class="lab-list">
        <li>Web Application Firewall (WAF)</li>
        <li>Input validation / sanitization</li>
        <li>Защита от OWASP Top 10 (SQLi, XSS, CSRF, RCE и т.д.)</li>
        <li>Антивирус / антималварь на уровне приложений</li>
        <li>Application Control / URL Filtering</li>
        <li>DNS Security (DNSSEC, DNS Filtering, Response Policy Zones)</li>
        <li>API Gateway с аутентификацией и rate-limiting</li>
        <li>EDR / XDR (поведение приложений на хосте)</li>
        <li>SIEM + корреляция логов приложений</li>
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
        title: 'IDS-системы',
        audience: 'Для аналитиков SOC и blue-team инженеров, оценивающих покрытие обнаружения.',
        focus: 'Фокус: обнаружение сетевых вторжений в реальном времени и разбор оповещений.'
      },
      attacks: {
        title: 'Симуляции атак',
        audience: 'Для red-team упражнений и проверки уязвимостей.',
        focus: 'Фокус: контролируемое наступательное тестирование целей лаборатории для проверки защиты.'
      },
      infrastructure: {
        title: 'Инфраструктура',
        audience: 'Для инженеров, создающих и укрепляющих лабораторные среды.',
        focus: 'Фокус: сегментация сети, виртуализация и настройка стека мониторинга.'
      },
      defense: {
        title: 'Линия защиты',
        audience: 'Многоуровневые меры защиты по принципу эшелонированной обороны (defense-in-depth).',
        focus: 'Фокус: каждый уровень (Firewall → WAF → IDS/IPS → EDR → SIEM) снижает остаточный риск.'
      },
      osi: {
        title: 'Уровни OSI',
        audience: 'Для инженеров, сопоставляющих меры защиты с моделью OSI.',
        focus: 'Фокус: меры защиты по всем 7 уровням OSI — от физического до прикладного.'
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
