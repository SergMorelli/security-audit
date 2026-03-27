---
layout: default
title: التقارير
permalink: /ar/reports/
lang: ar
translation_key: reports
---

<section class="pt-32 pb-20 text-center">
  <h1 class="text-4xl text-cyan-400 mb-6">تقارير الأمن</h1>
  <p class="text-gray-400">مجموعة من تقارير فحص الثغرات واختبارات الاختراق.</p>
</section>

<section class="max-w-6xl mx-auto px-4 pb-8" data-reports-filter>
  <div class="overflow-x-auto">
    <div class="flex min-w-max items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="report-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 bg-gradient-to-r from-cyan-500/25 to-fuchsia-500/15 shadow-[0_0_16px_rgba(34,211,238,0.25)]" data-filter="all">🌐 All</button>
      <button type="button" class="report-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="technical">🛠 Technical</button>
      <button type="button" class="report-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="management">📋 Management</button>
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

# 🔐 نماذج تقارير التدقيق الأمني
### Multilingual RU / EN / AR
---

# Nmap
# SSLScan
# OpenSSL
# OWASP ZAP
# Nikto
---

# 🛠 التقارير / Reports / Отчеты

<div class="report-filter-item" data-report-category="technical" markdown="1">

## 🛠️ التقرير الفني

مخصص للمهندسين ومديري الأنظمة ومحللي SOC.
التركيز: نتائج تفصيلية، مراجع CVE، أوامر، إعدادات وسكربتات.

### 🔗 المستندات
- [English]({{ site.baseurl }}/reports/technical/en/)
- [Русская версия]({{ site.baseurl }}/reports/technical/ru/)
- [النسخة العربية]({{ site.baseurl }}/reports/technical/ar/)

</div>

---

<div class="report-filter-item" data-report-category="management" markdown="1">

## 📋 التقرير الإداري

مخصص لمديري تقنية المعلومات والأمن وقادة المشاريع.
التركيز: مصفوفة المخاطر، ترتيب الأولويات (P0–P3)، الامتثال وخطط المعالجة.

### 🔗 المستندات
- [English]({{ site.baseurl }}/reports/management/en/)
- [Русская версия]({{ site.baseurl }}/reports/management/ru/)
- [النسخة العربية]({{ site.baseurl }}/reports/management/ar/)

</div>

---

<div class="report-filter-item" data-report-category="executive" markdown="1">

## 🏛️ التقرير التنفيذي

مخصص للمديرين التنفيذيين.
التركيز: مخاطر الأعمال، الأثر المالي، عائد الاستثمار في الأمن ومؤشرات الأداء.

### 🔗 المستندات
- [English]({{ site.baseurl }}/reports/executive/en/)
- [Русская версия]({{ site.baseurl }}/reports/executive/ru/)
- [النسخة العربية]({{ site.baseurl }}/reports/executive/ar/)

</div>

---

# 🕷️ تقارير فحص ثغرات تطبيقات الويب / Web Application Vulnerability Scan Reports / Отчеты сканирования уязвимостей веб-приложений

<div class="report-filter-item" data-report-category="comprehensive" markdown="1">

## 📚 Comprehensive Reports

- 🇷🇺 [RU]({{ site.baseurl }}/zap-reports/comprehensive/ru/) | 🇬🇧 [EN]({{ site.baseurl }}/zap-reports/comprehensive/en/) | 🇸🇦 [AR]({{ site.baseurl }}/zap-reports/comprehensive/ar/)

</div>

<div class="report-filter-item" data-report-category="technical" markdown="1">

## 🛠 Technical Reports
- 🇷🇺 [RU]({{ site.baseurl }}/zap-reports/technical/ru/)
- 🇬🇧 [EN]({{ site.baseurl }}/zap-reports/technical/en/)
- 🇸🇦 [AR]({{ site.baseurl }}/zap-reports/technical/ar/)

</div>

<div class="report-filter-item" data-report-category="management" markdown="1">

## 📋 Management Reports

- 🇷🇺 [RU]({{ site.baseurl }}/zap-reports/management/ru/)
- 🇬🇧 [EN]({{ site.baseurl }}/zap-reports/management/en/)
- 🇸🇦 [AR]({{ site.baseurl }}/zap-reports/management/ar/)

</div>

<div class="report-filter-item" data-report-category="executive" markdown="1">

## 🏛 Executive Reports

- 🇷🇺 [RU]({{ site.baseurl }}/zap-reports/executive/ru/)
- 🇬🇧 [EN]({{ site.baseurl }}/zap-reports/executive/en/)
- 🇸🇦 [AR]({{ site.baseurl }}/zap-reports/executive/ar/)

</div>

# 🕷️ تقرير Nikto / Nikto Scan Report / Отчет сканирования Nikto

<div class="report-filter-item" data-report-category="comprehensive" markdown="1">

## 📚 Comprehensive Reports

🇷🇺 [RU]({{ site.baseurl }}/nikto-report/comprehensive/ru/) | 🇬🇧 [EN]({{ site.baseurl }}/nikto-report/comprehensive/en/) | 🇸🇦 [AR]({{ site.baseurl }}/nikto-report/comprehensive/ar/)

</div>

---

إذا كان لديك أي أسئلة حول بنية التقارير، افتح issue في المستودع.

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
        title: 'جميع التقارير',
        audience: 'نظرة عامة على جميع فئات التقارير في مكان واحد.',
        focus: 'التركيز: استعراض التقارير الفنية والإدارية والتنفيذية والشاملة معاً.'
      },
      technical: {
        title: 'التقرير الفني',
        audience: 'مخصص للمهندسين ومديري الأنظمة ومحللي SOC.',
        focus: 'التركيز: نتائج تفصيلية، مراجع CVE، أوامر، إعدادات وسكربتات.'
      },
      management: {
        title: 'التقرير الإداري',
        audience: 'مخصص لمديري تقنية المعلومات والأمن وقادة المشاريع.',
        focus: 'التركيز: مصفوفة المخاطر، ترتيب الأولويات (P0-P3)، مراجع الامتثال والجداول الزمنية للمعالجة.'
      },
      executive: {
        title: 'التقرير التنفيذي',
        audience: 'مخصص للرؤساء التنفيذيين CTO وCISO وأعضاء مجلس الإدارة.',
        focus: 'التركيز: مخاطر الأعمال، الأثر المالي، عائد الاستثمار في الأمن ومؤشرات الأداء الاستراتيجية.'
      },
      comprehensive: {
        title: 'التقرير الشامل',
        audience: 'مخصص لمراجعة شاملة للثغرات عبر الأنظمة وتطبيقات الويب.',
        focus: 'التركيز: نتائج الفحوصات المجمعة، الأدلة الأساسية، ولقطات تغطية شاملة من البداية للنهاية.'
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
