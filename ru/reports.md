---
layout: default
title: Отчеты
permalink: /ru/reports/
lang: ru
translation_key: reports
---

<section class="pt-32 pb-20 text-center">
  <h1 class="text-4xl text-cyan-400 mb-6">Отчеты по безопасности</h1>
  <p class="text-gray-400">Коллекция результатов сканирования и тестирования на проникновение.</p>
</section>

<section class="max-w-6xl mx-auto px-4 pb-8" data-reports-filter>
  <div class="overflow-x-auto">
    <div class="flex min-w-max items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="report-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 bg-gradient-to-r from-cyan-500/25 to-fuchsia-500/15 shadow-[0_0_16px_rgba(34,211,238,0.25)]" data-filter="all">🌐 Все</button>
      <button type="button" class="report-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="technical">🛠 Технические</button>
      <button type="button" class="report-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="management">📋 Управленческие</button>
      <button type="button" class="report-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="executive">🏛 Executive</button>
      <button type="button" class="report-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="comprehensive">📚 Comprehensive</button>
    </div>
  </div>
  <div id="reportsFilterDescription" class="mt-4 rounded-lg bg-slate-900/40 ring-1 ring-cyan-400/20 px-4 py-3">
    <h3 id="reportsFilterDescriptionTitle" class="text-sm sm:text-base text-cyan-200 font-semibold"></h3>
    <p id="reportsFilterDescriptionAudience" class="mt-1 text-sm text-gray-300"></p>
    <p id="reportsFilterDescriptionFocus" class="mt-1 text-sm text-gray-400"></p>
  </div>
</section>

{% assign reportLang = page.lang | default: 'ru' %}

<style>
  .soc-card {
    border: 1px solid rgba(71, 85, 105, 0.65);
    background: linear-gradient(165deg, rgba(8, 14, 28, 0.96), rgba(2, 8, 23, 0.86));
    padding-top: 2.4rem;
    padding-left: 2rem;
    padding-right: 1.25rem;
    padding-bottom: 1.25rem;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }

  .soc-card:hover {
    transform: translateY(-6px);
    border-color: rgba(34, 211, 238, 0.85);
    box-shadow: 0 0 0 1px rgba(34, 211, 238, 0.35), 0 0 28px rgba(34, 211, 238, 0.35);
  }

  .soc-title {
    margin-top: 0.5rem;
    padding-left: 0.5rem;
    transition: color 0.2s ease, text-shadow 0.2s ease;
  }

  .soc-card:hover .soc-title {
    color: rgb(34, 211, 238);
    text-shadow: 0 0 16px rgba(34, 211, 238, 0.45);
  }

  .report-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.42rem 0.9rem;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border: 1px solid rgba(71, 85, 105, 0.85);
    background: rgba(15, 23, 42, 0.75);
    border-radius: 0.45rem;
  }

  .report-link:hover {
    border-color: rgba(34, 211, 238, 0.75);
    color: rgb(165, 243, 252);
    box-shadow: 0 0 14px rgba(34, 211, 238, 0.25);
  }
</style>

<section class="max-w-6xl mx-auto px-4 pb-20 space-y-14">
  <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-x-8 gap-y-10">
    <article class="report-filter-item soc-card rounded-xl flex flex-col gap-4" data-report-category="technical">
      <h3 class="soc-title text-xl font-semibold text-slate-100 leading-tight">Аудит инфраструктуры</h3>
      <p class="text-xs text-slate-400">Инструменты: Nmap, SSLScan, OpenSSL</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/reports/technical/{{ reportLang }}/technical-report-{{ reportLang }}.pdf" class="report-link transition">PDF</a>
          <a href="{{ site.baseurl }}/reports/technical/{{ reportLang }}/reports-technical-{{ reportLang }}.html" class="report-link transition">HTML</a>
        </div>
      </div>
    </article>

    <article class="report-filter-item soc-card rounded-xl flex flex-col gap-4" data-report-category="technical">
      <h3 class="soc-title text-lg font-semibold text-slate-100 leading-tight">Скан уязвимостей веб-приложения</h3>
      <p class="text-xs text-slate-400">Инструменты: OWASP ZAP, Passive/Active Scan Rules</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/zap-reports/technical/{{ reportLang }}/zapreports-technical-{{ reportLang }}.pdf" class="report-link transition">PDF</a>
          <a href="{{ site.baseurl }}/zap-reports/technical/{{ reportLang }}/zap-reports-technical-{{ reportLang }}.html" class="report-link transition">HTML</a>
        </div>
      </div>
    </article>

    <article class="report-filter-item soc-card rounded-xl flex flex-col gap-4" data-report-category="comprehensive">
      <h3 class="soc-title text-lg font-semibold text-slate-100 leading-tight">Скан безопасности веб-сервера</h3>
      <p class="text-xs text-slate-400">Инструменты: Nikto, HTTP Header Checks</p>
      <div class="border-t border-slate-700/60 pt-3">
        <div class="flex items-center gap-3 text-sm font-mono text-slate-300">
          <a href="{{ site.baseurl }}/nikto-report/comprehensive/{{ reportLang }}/niktoreport-comprehensive-{{ reportLang }}.pdf" class="report-link transition">PDF</a>
          <a href="{{ site.baseurl }}/nikto-report/comprehensive/{{ reportLang }}/nikto-report-general-{{ reportLang }}.html" class="report-link transition">HTML</a>
        </div>
      </div>
    </article>
  </div>
</section>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    var filterRoot = document.querySelector('[data-reports-filter]');
    if (!filterRoot) {
      return;
    }

    var buttons = Array.prototype.slice.call(filterRoot.querySelectorAll('.report-filter-button'));
    var sections = Array.prototype.slice.call(document.querySelectorAll('.report-filter-item'));
    var descriptionTitle = document.getElementById('reportsFilterDescriptionTitle');
    var descriptionAudience = document.getElementById('reportsFilterDescriptionAudience');
    var descriptionFocus = document.getElementById('reportsFilterDescriptionFocus');

    var descriptions = {
      all: {
        title: 'Все отчеты',
        audience: 'Обзор всех карточек отчетов в одном месте.',
        focus: 'Фокус: каждая карточка содержит ссылки на PDF и HTML-версию отчета для текущего языка.'
      },
      comprehensive: {
        title: 'Comprehensive / Комплексный / شامل',
        audience: 'Широкий обзор отчетов для EN / RU / AR.',
        focus: 'Фокус: полный охват и сводный уровень результатов.'
      },
      technical: {
        title: 'Technical / Технический / تقني',
        audience: 'Для инженеров, администраторов и SOC-аналитиков.',
        focus: 'Фокус: прямые ссылки на технические PDF и HTML.'
      },
      management: {
        title: 'Management / Менеджмент / إداري',
        audience: 'Для менеджеров и руководителей команд.',
        focus: 'Фокус: управленческий контекст, риски и приоритеты.'
      },
      executive: {
        title: 'Executive / Исполнительный / تنفيذي',
        audience: 'Для руководства и стейкхолдеров.',
        focus: 'Фокус: стратегический и бизнес-уровень представления.'
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
        var matches = category === 'all' || section.getAttribute('data-report-category') === category;
        section.hidden = !matches;
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

    setFilter('all');
  });
</script>
