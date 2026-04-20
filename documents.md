---
layout: default
title: Documents
permalink: /documents/
lang: en
translation_key: documents
---

<section class="pt-14 pb-10 md:pt-32 md:pb-20 text-center">
  <h1 class="text-4xl text-cyan-400 mb-6">Documents</h1>
  <p class="text-gray-400">Whitepapers, policies, licenses, and legal documentation.</p>
</section>

<!-- ── Filter bar ─────────────────────────────────────────────────── -->
<section class="max-w-6xl mx-auto px-4 pb-8" data-docs-filter>
  <div class="overflow-x-auto">
    <div class="flex min-w-max items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 bg-gradient-to-r from-cyan-500/25 to-fuchsia-500/15 shadow-[0_0_16px_rgba(34,211,238,0.25)]" data-filter="all">🌐 All</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="whitepaper">📜 Whitepaper</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="policy">🔒 Policy</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="licenses">⚖️ Licenses</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="legal">🏷️ Legal</button>
      <button type="button" class="doc-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="certificates">🏆 Certificates</button>
    </div>
  </div>
  <div id="docsFilterDescription" class="mt-4 rounded-lg bg-slate-900/40 ring-1 ring-cyan-400/20 px-4 py-3">
    <h3 id="docsFilterDescriptionTitle" class="text-sm sm:text-base text-cyan-200 font-semibold"></h3>
    <p id="docsFilterDescriptionAudience" class="mt-1 text-sm text-gray-300"></p>
    <p id="docsFilterDescriptionFocus" class="mt-1 text-sm text-gray-400"></p>
  </div>
</section>

{% assign docLang = page.lang | default: 'en' %}

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

    <!-- Privacy Policy EN -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="policy">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Privacy Policy — Shadow Archive</h3>
      <p class="text-xs text-slate-400">Privacy Policy for the Shadow Archive game</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/privacy-policy/tenArhivaru/TenArhivaRu.pdf" class="doc-link transition">PDF</a>
          <a href="{{ site.baseurl }}/privacy-policy/tenArhivaru/privacy-policy-tenArhiva-en.html" class="doc-link transition">HTML</a>
        </div>
      </div>
    </article>

    <!-- License EN -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="licenses">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Documentation License — English</h3>
      <p class="text-xs text-slate-400">CC BY‑NC 4.0 — Usage terms for reports and templates</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/LICENSE-DOCS-EN.md" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- License RU -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="licenses">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Лицензия — Русский</h3>
      <p class="text-xs text-slate-400">CC BY‑NC 4.0 — Условия использования отчётов и шаблонов</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/LICENSE-DOCS-RU.md" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- License AR -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="licenses">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">الترخيص — العربية</h3>
      <p class="text-xs text-slate-400 font-[Noto_Sans_Arabic,sans-serif]">CC BY‑NC 4.0 — شروط استخدام التقارير والقوالب</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/LICENSE-DOCS-AR.md" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- Trademarks EN -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="legal">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Trademarks — English</h3>
      <p class="text-xs text-slate-400">DataDef branding and trademark notice</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/TRADEMARKS-EN.md" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- Trademarks RU -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="legal">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Товарные знаки — Русский</h3>
      <p class="text-xs text-slate-400">Уведомление о торговой марке DataDef</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/TRADEMARKS-RU.md" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- Trademarks AR -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="legal">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">العلامات التجارية — العربية</h3>
      <p class="text-xs text-slate-400 font-[Noto_Sans_Arabic,sans-serif]">إشعار العلامة التجارية لـ DataDef</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/licenses/TRADEMARKS-AR.md" class="doc-link transition">View</a>
        </div>
      </div>
    </article>

    <!-- Certificate 1 -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="certificates">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Certificate — English</h3>
      <p class="text-xs text-slate-400">Professional cybersecurity certification</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="#" class="doc-link transition">PDF</a>
        </div>
      </div>
    </article>

    <!-- Certificate 2 -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="certificates">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">Сертификат — Русский</h3>
      <p class="text-xs text-slate-400">Профессиональный сертификат в области кибербезопасности</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="#" class="doc-link transition">PDF</a>
        </div>
      </div>
    </article>

    <!-- Certificate 3 -->
    <article class="doc-filter-item doc-card rounded-xl flex flex-col gap-4" data-doc-category="certificates">
      <h3 class="doc-title text-xl font-semibold text-slate-100 leading-tight">الشهادة — العربية</h3>
      <p class="text-xs text-slate-400 font-[Noto_Sans_Arabic,sans-serif]">شهادة احترافية في الأمن السيبراني</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="#" class="doc-link transition">PDF</a>
        </div>
      </div>
    </article>

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
      all: {
        title:    'All Documents',
        audience: 'Overview of all available documents in one place.',
        focus:    'Focus: whitepapers, privacy policies, license texts, trademark notices, and certificates.'
      },
      whitepaper: {
        title:    'Whitepaper',
        audience: 'Introductory white papers that define the environment, ownership, scope, and rules of engagement for security assessments and penetration testing. Intended for auditors, clients, and security teams preparing for an engagement.',
        focus:    'Focus: define system ownership and responsibilities · establish scope and testing boundaries · describe allowed and prohibited activities · provide emergency contacts and escalation rules · ensure legal and operational safety · align expectations between the organization and the testing team.'
      },

      policy: {
        title:    'Policy',
        audience: 'For stakeholders, data subjects, and compliance teams.',
        focus:    'Focus: privacy policy covering data handling, retention, and user rights.'
      },
      licenses: {
        title:    'Licenses',
        audience: 'For anyone using or redistributing project materials.',
        focus:    'Focus: CC BY‑NC 4.0 terms for reports, templates, and documentation.'
      },
      legal: {
        title:    'Legal',
        audience: 'For partners, media, and third parties referencing the brand.',
        focus:    'Focus: trademark notices and brand usage guidelines for DataDef Information Security.'
      },
      certificates: {
        title:    'Certificates',
        audience: 'Verified professional credentials and certifications.',
        focus:    'Focus: industry-recognized certifications in cybersecurity and information security.'
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
        var matches = category === 'all'
          ? true
          : category === 'whitepaper'
            ? item.getAttribute('data-doc-category') === 'whitepaper' && itemLang === pageLang
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

    setFilter('all');
  });
</script>

