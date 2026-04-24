---
layout: default
title: Документы
permalink: /ru/documents/
lang: ru
translation_key: documents
---

<section class="pt-14 pb-10 md:pt-32 md:pb-20 text-center">
  <h1 class="text-4xl text-cyan-400 mb-6">Документы</h1>
  <p class="text-gray-400">Whitepaper, политики, лицензии и юридическая документация.</p>
</section>

<!-- ── Filter bar ─────────────────────────────────────────────────── -->
<section class="max-w-6xl mx-auto px-4 pb-8" data-docs-filter>
  <div class="overflow-x-auto">
    <div class="flex min-w-max items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="whitepaper">📜 Whitepaper</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="policy">🔒 Политика</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="licenses">⚖️ Лицензии</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="legal">🏷️ Правовые</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="certificates">🏆 Сертификаты</button>
    </div>
  </div>
  <div id="docsFilterDescription" class="mt-4 rounded-lg bg-slate-900/40 ring-1 ring-cyan-400/20 px-4 py-3">
    <h3 id="docsFilterDescriptionTitle" class="text-sm sm:text-base text-cyan-200 font-semibold"></h3>
    <p id="docsFilterDescriptionAudience" class="mt-1 text-sm text-gray-300"></p>
    <p id="docsFilterDescriptionFocus" class="mt-1 text-sm text-gray-400"></p>
  </div>
</section>

<style>
  .doc-card {
    border: 1px solid rgba(71, 85, 105, 0.65);
    background: linear-gradient(165deg, rgba(8, 14, 28, 0.96), rgba(2, 8, 23, 0.86));
    padding-top: 2.4rem;
    padding-left: 2rem;
    padding-right: 1.25rem;
    padding-bottom: 1.25rem;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }
  .doc-title {
    margin-top: 0.5rem;
    padding-left: 0.5rem;
    transition: color 0.2s ease, text-shadow 0.2s ease;
  }
  .doc-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 2.75rem;
    padding: 0.42rem 0.9rem;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border: 1px solid rgba(71, 85, 105, 0.85);
    background: rgba(15, 23, 42, 0.75);
    border-radius: 0.45rem;
  }
  @media (hover: hover) {
    .doc-card:hover {
      transform: translateY(-6px);
      border-color: rgba(34, 211, 238, 0.85);
      box-shadow: 0 0 0 1px rgba(34, 211, 238, 0.35), 0 0 28px rgba(34, 211, 238, 0.35);
    }
    .doc-card:hover .doc-title {
      color: rgb(34, 211, 238);
      text-shadow: 0 0 16px rgba(34, 211, 238, 0.45);
    }
    .doc-link:hover {
      border-color: rgba(34, 211, 238, 0.75);
      color: rgb(165, 243, 252);
      box-shadow: 0 0 14px rgba(34, 211, 238, 0.25);
    }

    [data-doc-category="certificates"] .doc-card:hover {
      border-color: rgba(248, 113, 113, 0.95);
      box-shadow: 0 0 0 1px rgba(248, 113, 113, 0.7), 0 0 18px rgba(239, 68, 68, 0.55), 0 0 42px rgba(185, 28, 28, 0.45);
    }
  }

  .cert-badge {
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

  .cert-action-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.4rem;
    white-space: nowrap;
    width: 9rem;
    min-height: 1.95rem;
    padding: 0.28rem 0.62rem;
    font-size: 0.66rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    border-radius: 0.2rem;
    border: 1px solid rgba(71, 85, 105, 0.7);
    background: rgba(15, 23, 42, 0.75);
    color: rgb(148, 163, 184);
    transition: border-color 0.2s, color 0.2s, background 0.2s;
  }

  .cert-action-btn:hover {
    border-color: rgba(34, 211, 238, 0.7);
    color: rgb(165, 243, 252);
    background: rgba(34, 211, 238, 0.08);
  }

  .cert-action-btn.primary {
    border-color: rgba(34, 211, 238, 0.55);
    color: rgb(103, 232, 249);
    background: rgba(34, 211, 238, 0.1);
  }

  .cert-action-btn.primary:hover {
    background: rgba(34, 211, 238, 0.18);
  }

  .cert-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.2rem;
  }

  @media (max-width: 480px) {
    .cert-action-btn {
      width: 8.5rem;
      min-height: 1.9rem;
    }
  }

  .cert-pdf-preview {
    display: none;
    margin-top: 1.25rem;
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 0.5rem;
    overflow: hidden;
    background: rgba(2, 8, 23, 0.8);
  }

  .cert-pdf-preview.open {
    display: block;
  }
</style>

<!-- ── Document Cards ─────────────────────────────────────────────── -->
<section class="max-w-6xl mx-auto px-4 pb-20 space-y-14">
  <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-x-8 gap-y-10">

    <!-- Whitepaper EN -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="whitepaper" data-doc-lang="en">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Whitepaper — English</h3>
      <p class="text-xs text-slate-400">Scope, ownership, rules of engagement for security assessments</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/whitepaper/en/whitepaper-en.pdf" class="doc-link transition">PDF</a>
          <a href="{{ site.baseurl }}/whitepaper/en/whitepaper-en.html" class="doc-link transition">HTML</a>
        </div>
      </div>
    </article>

    <!-- Whitepaper RU -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="whitepaper" data-doc-lang="ru">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Whitepaper — Русский</h3>
      <p class="text-xs text-slate-400">Область аудита, ответственность и правила проведения тестирования</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/whitepaper/ru/whitepaper-ru.pdf" class="doc-link transition">PDF</a>
          <a href="{{ site.baseurl }}/whitepaper/ru/whitepaper-ru.html" class="doc-link transition">HTML</a>
        </div>
      </div>
    </article>

    <!-- Whitepaper AR -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="whitepaper" data-doc-lang="ar">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Whitepaper — العربية</h3>
      <p class="text-xs text-slate-400 font-[Noto_Sans_Arabic,sans-serif]">النطاق، الملكية، وقواعد إجراء تدقيق الأمن السيبراني</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/whitepaper/ar/whitepaper-ar.pdf" class="doc-link transition">PDF</a>
          <a href="{{ site.baseurl }}/whitepaper/ar/whitepaper-ar.html" class="doc-link transition">HTML</a>
        </div>
      </div>
    </article>

    <!-- Privacy Policy RU -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="policy">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Политика конфиденциальности — Тень Архива: Overmind Protocol</h3>
      <p class="text-xs text-slate-400">Политика конфиденциальности игры «Тень Архива: Overmind Protocol»</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/privacy-policy/tenArhivaru/TenArhivaRu.pdf" class="doc-link transition">PDF</a>
          <a href="{{ site.baseurl }}/privacy-policy/tenArhivaru/privacy-policy-tenArhiva-ru.html" class="doc-link transition">HTML</a>
          <a href="https://www.rustore.ru/catalog/app/ru.datadef.tenarhiva" class="doc-link transition" target="_blank" rel="noopener">RuStore</a>
        </div>
      </div>
    </article>

    <!-- License EN -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="licenses" data-doc-lang="en">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Documentation License — English</h3>
      <p class="text-xs text-slate-400">CC BY‑NC 4.0 — Usage terms for reports and templates</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/LICENSE-DOCS-EN.html" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- License RU -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="licenses" data-doc-lang="ru">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Лицензия — Русский</h3>
      <p class="text-xs text-slate-400">CC BY‑NC 4.0 — Условия использования отчётов и шаблонов</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/LICENSE-DOCS-RU.html" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- License AR -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="licenses" data-doc-lang="ar">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">الترخيص — العربية</h3>
      <p class="text-xs text-slate-400 font-[Noto_Sans_Arabic,sans-serif]">CC BY‑NC 4.0 — شروط استخدام التقارير والقوالب</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/LICENSE-DOCS-AR.html" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- Trademarks EN -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="legal" data-doc-lang="en">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Trademarks — English</h3>
      <p class="text-xs text-slate-400">DataDef branding and trademark notice</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/TRADEMARKS-EN.html" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- Trademarks RU -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="legal" data-doc-lang="ru">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Товарные знаки — Русский</h3>
      <p class="text-xs text-slate-400">Уведомление о торговой марке DataDef</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/TRADEMARKS-RU.html" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- Trademarks AR -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="legal" data-doc-lang="ar">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">العلامات التجارية — العربية</h3>
      <p class="text-xs text-slate-400 font-[Noto_Sans_Arabic,sans-serif]">إشعار العلامة التجارية لـ DataDef</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/TRADEMARKS-AR.html" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- Certificates entry -->
    <div class="doc-filter-item col-span-full" data-doc-category="certificates">
      <div class="doc-card rounded-xl p-6">

        <div class="flex items-center justify-between flex-wrap gap-3 mb-5">
          <span class="cert-badge">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=coursera.org" alt="Coursera" class="w-4 h-4 rounded-sm">
            Coursera
          </span>
          <div class="flex items-center gap-2">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg" alt="IBM" class="rounded-sm bg-white/95" style="width:46px;height:23px;max-width:46px;max-height:23px;object-fit:contain;display:block;" title="IBM (International Business Machines)">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=credly.com" alt="Credly" class="w-7 h-7 rounded-sm" title="Credly">
          </div>
        </div>

        <h3 class="doc-title text-xl font-bold text-white mb-3 leading-snug">
          IT Fundamentals for Cybersecurity
        </h3>

        <ul class="text-sm text-gray-400 leading-relaxed mb-5 list-disc list-inside space-y-1">
          <li>Introduction to Cybersecurity Tools &amp; Cyberattacks</li>
          <li>Operating Systems: Overview, Administration, and Security</li>
          <li>Cybersecurity Compliance Framework, Standards &amp; Regulations</li>
          <li>Computer Networks and Network Security</li>
        </ul>

        <div class="border-t border-slate-700/60 mb-3"></div>

        <div class="cert-actions">
          <a href="https://www.credly.com/badges/1b730c34-a8b6-4d97-8232-af097c3cb48e/public_url" target="_blank" rel="noopener noreferrer" class="cert-action-btn primary">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 4v5c0 5-3.5 8-7 9-3.5-1-7-4-7-9V7l7-4z"/></svg>
            Badge Credly
          </a>
          <a href="https://coursera.org/share/a316fe91058dde6567813a3f3a316753" target="_blank" rel="noopener noreferrer" class="cert-action-btn">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            Verify on Coursera
          </a>
          <button type="button" class="cert-action-btn"
            onclick="var p=this.closest('.doc-card').querySelector('.cert-pdf-preview');var o=p.classList.toggle('open');this.textContent=o?'\u25b2 Hide Preview':'\u25bc Preview PDF';"
          >
            &#9660; Preview PDF
          </button>
        </div>

        <div class="cert-pdf-preview">
          <iframe src="{{ '/sertificate/Coursera 5N2LNGY9T8KH.pdf' | relative_url }}" class="w-full" style="height:520px;" title="Certificate PDF preview" loading="lazy"></iframe>
        </div>

      </div>

      <div class="doc-card rounded-xl p-6 mt-6">

        <div class="flex items-center justify-between flex-wrap gap-3 mb-5">
          <span class="cert-badge">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=coursera.org" alt="Coursera" class="w-4 h-4 rounded-sm">
            Coursera
          </span>
          <img src="https://logo.clearbit.com/eccouncil.org" alt="EC-Council" class="rounded-sm bg-white px-1 py-0.5" style="width:80px;height:40px;max-width:80px;max-height:40px;object-fit:contain;display:block;" title="EC-Council" onerror="this.onerror=null;this.src='https://www.google.com/s2/favicons?sz=128&domain=eccouncil.org';this.className='rounded-sm bg-white';this.style='width:40px;height:40px;max-width:40px;max-height:40px;object-fit:contain;display:block;';">
        </div>

        <h3 class="doc-title text-xl font-bold text-white mb-3 leading-snug">
          Cybersecurity Attack and Defense Fundamentals
        </h3>

        <ul class="text-sm text-gray-400 leading-relaxed mb-5 list-disc list-inside space-y-1">
          <li>Ethical Hacking Essentials (EHE)</li>
          <li>Network Defense Essentials (NDE)</li>
          <li>Digital Forensics Essentials (DFE)</li>
        </ul>

        <div class="border-t border-slate-700/60 mb-3"></div>

        <div class="cert-actions">
          <a href="https://coursera.org/share/cde0e4bf442d944f2ae3e98f72d0574d" target="_blank" rel="noopener noreferrer" class="cert-action-btn primary">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            Verify on Coursera
          </a>
          <button type="button" class="cert-action-btn"
            onclick="var p=this.closest('.doc-card').querySelector('.cert-pdf-preview');var o=p.classList.toggle('open');this.textContent=o?'\u25b2 Hide Preview':'\u25bc Preview PDF';"
          >
            &#9660; Preview PDF
          </button>
        </div>

        <div class="cert-pdf-preview">
          <iframe src="{{ '/sertificate/Coursera 80C2FPT2K0QG.pdf' | relative_url }}" class="w-full" style="height:520px;" title="Certificate PDF preview" loading="lazy"></iframe>
        </div>

      </div>

      <div class="doc-card rounded-xl p-6 mt-6">

        <div class="flex items-center justify-between flex-wrap gap-3 mb-5">
          <span class="cert-badge">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=coursera.org" alt="Coursera" class="w-4 h-4 rounded-sm">
            Coursera
          </span>
          <div class="flex items-center gap-2">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=google.com" alt="Google" class="w-7 h-7 rounded-sm" title="Google">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=credly.com" alt="Credly" class="w-7 h-7 rounded-sm" title="Credly">
          </div>
        </div>

        <h3 class="doc-title text-xl font-bold text-white mb-3 leading-snug">
          Google Cybersecurity
        </h3>

        <ul class="text-sm text-gray-400 leading-relaxed mb-5 list-disc list-inside space-y-1">
          <li>Foundations of Cybersecurity</li>
          <li>Play It Safe: Manage Security Risks</li>
          <li>Connect and Protect: Networks and Network Security</li>
          <li>Tools of the Trade: Linux and SQL</li>
          <li>Assets, Threats, and Vulnerabilities</li>
          <li>Sound the Alarm: Detection and Response</li>
          <li>Automate Cybersecurity Tasks with Python</li>
          <li>Put It to Work: Prepare for Cybersecurity Jobs</li>
        </ul>

        <div class="border-t border-slate-700/60 mb-3"></div>

        <div class="cert-actions">
          <a href="https://www.credly.com/badges/4899c982-6381-473b-915e-4479222f0cc4/public_url" target="_blank" rel="noopener noreferrer" class="cert-action-btn primary">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 4v5c0 5-3.5 8-7 9-3.5-1-7-4-7-9V7l7-4z"/></svg>
            Badge Credly
          </a>
          <a href="https://coursera.org/share/687ca5118a74e9887b0189e0e757b135" target="_blank" rel="noopener noreferrer" class="cert-action-btn">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            Verify on Coursera
          </a>
          <button type="button" class="cert-action-btn"
            onclick="var p=this.closest('.doc-card').querySelector('.cert-pdf-preview');var o=p.classList.toggle('open');this.textContent=o?'\u25b2 Hide Preview':'\u25bc Preview PDF';"
          >
            &#9660; Preview PDF
          </button>
        </div>

        <div class="cert-pdf-preview">
          <iframe src="{{ '/sertificate/Coursera A7MUSAOT3OJ0.pdf' | relative_url }}" class="w-full" style="height:520px;" title="Certificate PDF preview" loading="lazy"></iframe>
        </div>

      </div>

      <div class="doc-card rounded-xl p-6 mt-6">

        <div class="flex items-center justify-between flex-wrap gap-3 mb-5">
          <span class="cert-badge">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=coursera.org" alt="Coursera" class="w-4 h-4 rounded-sm">
            Coursera
          </span>
          <div class="flex items-center gap-2">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=microsoft.com" alt="Microsoft" class="w-7 h-7 rounded-sm" title="Microsoft">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=credly.com" alt="Credly" class="w-7 h-7 rounded-sm" title="Credly">
          </div>
        </div>

        <h3 class="doc-title text-xl font-bold text-white mb-3 leading-snug">
          Microsoft Cybersecurity Analyst
        </h3>

        <ul class="text-sm text-gray-400 leading-relaxed mb-5 list-disc list-inside space-y-1">
          <li>Introduction to Computers and Operating Systems and Security</li>
          <li>Introduction to Networking and Cloud Computing</li>
          <li>Cybersecurity Threat Vectors and Mitigation</li>
          <li>Cybersecurity Identity and Access Solutions using Azure AD</li>
          <li>Cybersecurity Solutions and Microsoft Defender</li>
          <li>Cybersecurity Tools and Technologies</li>
          <li>Cybersecurity Management and Compliance</li>
          <li>Advanced Cybersecurity Concepts and Capstone Project</li>
        </ul>

        <div class="border-t border-slate-700/60 mb-3"></div>

        <div class="cert-actions">
          <a href="https://www.credly.com/badges/b4529e87-f355-44e2-9b55-2f6f9d5e9a2a" target="_blank" rel="noopener noreferrer" class="cert-action-btn primary">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 4v5c0 5-3.5 8-7 9-3.5-1-7-4-7-9V7l7-4z"/></svg>
            Badge Credly
          </a>
          <a href="https://coursera.org/share/c628b3add4065861f249ac0ce62e02d6" target="_blank" rel="noopener noreferrer" class="cert-action-btn">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            Verify on Coursera
          </a>
          <button type="button" class="cert-action-btn"
            onclick="var p=this.closest('.doc-card').querySelector('.cert-pdf-preview');var o=p.classList.toggle('open');this.textContent=o?'\u25b2 Hide Preview':'\u25bc Preview PDF';"
          >
            &#9660; Preview PDF
          </button>
        </div>

        <div class="cert-pdf-preview">
          <iframe src="{{ '/sertificate/Coursera KLBK3U18FQHA.pdf' | relative_url }}" class="w-full" style="height:520px;" title="Certificate PDF preview" loading="lazy"></iframe>
        </div>

      </div>

      <div class="doc-card rounded-xl p-6 mt-6">

        <div class="flex items-center justify-between flex-wrap gap-3 mb-5">
          <span class="cert-badge">
            <img src="https://www.google.com/s2/favicons?sz=32&domain=coursera.org" alt="Coursera" class="w-4 h-4 rounded-sm">
            Coursera
          </span>
          <img src="https://logo.clearbit.com/learnkarts.com" alt="Learnkarts" class="rounded-sm bg-white px-1 py-0.5" style="width:68px;height:34px;max-width:68px;max-height:34px;object-fit:contain;display:block;" title="Learnkarts" onerror="this.onerror=null;this.src='https://www.google.com/s2/favicons?sz=128&domain=learnkarts.com';this.className='rounded-sm bg-white';this.style='width:40px;height:40px;max-width:40px;max-height:40px;object-fit:contain;display:block;';">
        </div>

        <h3 class="doc-title text-xl font-bold text-white mb-3 leading-snug">
          Ethical Hacking
        </h3>

        <ul class="text-sm text-gray-400 leading-relaxed mb-5 list-disc list-inside space-y-1">
          <li>Ethical Hacking Fundamentals</li>
          <li>System &amp; Network Security Essentials</li>
          <li>Advanced Ethical Hacking &amp; Cybersecurity</li>
          <li>Ethical Hacking Practice Project &amp; Questions</li>
        </ul>

        <div class="border-t border-slate-700/60 mb-3"></div>

        <div class="cert-actions">
          <a href="https://coursera.org/share/0d934c9e95db8ea390fa9085e7a7fcfc" target="_blank" rel="noopener noreferrer" class="cert-action-btn primary">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            Verify on Coursera
          </a>
          <button type="button" class="cert-action-btn"
            onclick="var p=this.closest('.doc-card').querySelector('.cert-pdf-preview');var o=p.classList.toggle('open');this.textContent=o?'\u25b2 Hide Preview':'\u25bc Preview PDF';"
          >
            &#9660; Preview PDF
          </button>
        </div>

        <div class="cert-pdf-preview">
          <iframe src="{{ '/sertificate/Coursera PSYSKZY1K3EC.pdf' | relative_url }}" class="w-full" style="height:520px;" title="Certificate PDF preview" loading="lazy"></iframe>
        </div>

      </div>
    </div>

  </div>
</section>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    var filterRoot = document.querySelector('[data-docs-filter]');
    if (!filterRoot) return;

    var buttons = Array.prototype.slice.call(filterRoot.querySelectorAll('.doc-filter-button'));
    var items = Array.prototype.slice.call(document.querySelectorAll('.doc-filter-item'));
    var descriptionTitle    = document.getElementById('docsFilterDescriptionTitle');
    var descriptionAudience = document.getElementById('docsFilterDescriptionAudience');
    var descriptionFocus    = document.getElementById('docsFilterDescriptionFocus');

    function resolvePageLang() {
      var langFromFrontMatter = ('{{ page.lang | default: "" }}' || '').trim().toLowerCase();
      if (langFromFrontMatter) return langFromFrontMatter;

      var match = window.location.pathname.match(/^\/(ru|ar)(?:\/|$)/i);
      return match ? match[1].toLowerCase() : 'en';
    }

    var pageLang = resolvePageLang();
    var descriptions = {
      whitepaper: {
        title:    'Вводные документы',
        audience: 'Для аудиторов, клиентов и команд безопасности.',
        focus:    'Область аудита, ответственность и правила проведения тестирования.'
      },
      policy: {
        title:    'Политика',
        audience: 'Для заинтересованных сторон и команд по соблюдению требований.',
        focus:    'Политика конфиденциальности: обработка данных, хранение и права пользователей.'
      },
      licenses: {
        title:    'Лицензии',
        audience: 'Для всех, кто использует или распространяет материалы проекта.',
        focus:    'CC BY‑NC 4.0 — условия использования отчётов, шаблонов и документации.'
      },
      legal: {
        title:    'Правовые документы',
        audience: 'Для партнёров, СМИ и третьих сторон, ссылающихся на бренд.',
        focus:    'Уведомления о торговых марках и руководство по использованию бренда DataDef.'
      },
      certificates: {
        title:    'Мои сертификаты',
        audience: 'Подтверждённые профессиональные квалификации и сертификаты.',
        focus:    'Признанные отраслью сертификаты в области кибербезопасности и информационной безопасности.'
      }
    };

    function setFilter(category) {
      buttons.forEach(function (btn) {
        var active = btn.getAttribute('data-filter') === category;
        btn.classList.toggle('bg-gradient-to-r',                        active);
        btn.classList.toggle('from-cyan-500/25',                        active);
        btn.classList.toggle('to-fuchsia-500/15',                       active);
        btn.classList.toggle('text-cyan-100',                           active);
        btn.classList.toggle('shadow-[0_0_16px_rgba(34,211,238,0.25)]', active);
        btn.classList.toggle('text-slate-300',   !active);
        btn.classList.toggle('hover:bg-white/5', !active);
      });

      items.forEach(function (item) {
        var itemLang = (item.getAttribute('data-doc-lang') || '').trim().toLowerCase();
        var matches = (category === 'whitepaper' || category === 'licenses' || category === 'legal')
            ? item.getAttribute('data-doc-category') === category && itemLang === pageLang
            : item.getAttribute('data-doc-category') === category;
        item.hidden = !matches;
        item.style.display = matches ? '' : 'none';
      });

      if (descriptions[category]) {
        descriptionTitle.textContent    = descriptions[category].title;
        descriptionAudience.textContent = descriptions[category].audience;
        descriptionFocus.textContent    = descriptions[category].focus;
      }
    }

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () { setFilter(btn.getAttribute('data-filter')); });
    });

    if (buttons.length > 0) {
      setFilter(buttons[0].getAttribute('data-filter'));
    }
  });
</script>
