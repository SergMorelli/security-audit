---
layout: default
title: حول
permalink: /ar/about/
lang: ar
translation_key: about
---

<section class="pt-32 pb-20 text-center">
  <h1 class="text-4xl text-cyan-400 mb-6">حول</h1>
  <p class="text-gray-400">اختصاصي أمن يركز على اختبار الاختراق والدفاع عن البنية التحتية.</p>
</section>

<section class="max-w-6xl mx-auto px-4 pb-8" data-about-filter dir="rtl">
  <div class="overflow-x-auto">
    <div class="flex min-w-max items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="about-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 bg-gradient-to-r from-cyan-500/25 to-fuchsia-500/15 shadow-[0_0_16px_rgba(34,211,238,0.25)]" data-filter="page">📘 حول الصفحة</button>
      <button type="button" class="about-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="me">👤 نبذة عني</button>
    </div>
  </div>
  <div id="aboutFilterDescription" class="mt-4 rounded-lg bg-slate-900/40 ring-1 ring-cyan-400/20 px-4 py-3 text-right">
    <h3 id="aboutFilterDescriptionTitle" class="text-sm sm:text-base text-cyan-200 font-semibold"></h3>
    <p id="aboutFilterDescriptionAudience" class="mt-1 text-sm text-gray-300"></p>
    <p id="aboutFilterDescriptionFocus" class="mt-1 text-sm text-gray-400"></p>
  </div>
</section>

<style>
  .about-card {
    border: 1px solid rgba(71, 85, 105, 0.65);
    background: linear-gradient(165deg, rgba(8, 14, 28, 0.96), rgba(2, 8, 23, 0.86));
    padding-top: 2rem;
    padding-left: 1.5rem;
    padding-right: 1.25rem;
    padding-bottom: 1.4rem;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }

  .about-title {
    margin-top: 0.45rem;
    transition: color 0.2s ease, text-shadow 0.2s ease;
  }

  @media (hover: hover) {
    .about-card:hover {
      transform: translateY(-6px);
      border-color: rgba(34, 211, 238, 0.85);
      box-shadow: 0 0 0 1px rgba(34, 211, 238, 0.35), 0 0 28px rgba(34, 211, 238, 0.35);
    }

    .about-card:hover .about-title {
      color: rgb(34, 211, 238);
      text-shadow: 0 0 16px rgba(34, 211, 238, 0.45);
    }
  }
</style>

<section class="max-w-6xl mx-auto px-4 pb-20" dir="rtl">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-8">
    <article class="about-filter-item about-card rounded-xl flex flex-col gap-4 text-right" data-about-category="page">
      <h3 class="about-title text-xl font-semibold text-slate-100 leading-tight">حول الصفحة</h3>
      <p class="text-sm text-slate-400">الغرض من هذا القسم ونطاقه ضمن ملف تدقيق الأمن السيبراني.</p>
    </article>

    <article class="about-filter-item about-card rounded-xl flex flex-col gap-4 text-right" data-about-category="me">
      <h3 class="about-title text-xl font-semibold text-slate-100 leading-tight">نبذة عني</h3>
      <p class="text-sm text-slate-400">ملف مهني مختصر يتضمن مجالات التركيز والخبرة في الأمن السيبراني.</p>
    </article>
  </div>
</section>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    var filterRoot = document.querySelector('[data-about-filter]');
    if (!filterRoot) {
      return;
    }

    var buttons = Array.prototype.slice.call(filterRoot.querySelectorAll('.about-filter-button'));
    var sections = Array.prototype.slice.call(document.querySelectorAll('.about-filter-item'));
    var descriptionTitle = document.getElementById('aboutFilterDescriptionTitle');
    var descriptionAudience = document.getElementById('aboutFilterDescriptionAudience');
    var descriptionFocus = document.getElementById('aboutFilterDescriptionFocus');

    var descriptions = {
      page: {
        title: 'حول الصفحة',
        audience: 'للزوار الذين يحتاجون إلى فهم سياق هذا القسم.',
        focus: 'التركيز: ما الذي تحتويه الصفحة ولماذا أُنشئت.'
      },
      me: {
        title: 'نبذة عني',
        audience: 'للفرق وأصحاب المصلحة الذين يراجعون الملف الشخصي.',
        focus: 'التركيز: الخبرة والتخصص والخلفية في الأمن السيبراني.'
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
        var matches = section.getAttribute('data-about-category') === category;
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

    setFilter('page');
  });
</script>
