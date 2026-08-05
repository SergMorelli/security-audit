---
layout: default
title: حول
permalink: /ar/about/
lang: ar
translation_key: about
---

<section class="max-w-6xl mx-auto px-4 pt-32 pb-12" dir="rtl">
  <div class="max-w-4xl rounded-xl border border-cyan-400/10 bg-slate-950/35 px-4 py-5 backdrop-blur-sm mr-auto sm:px-6">
    <p class="text-right text-gray-300 text-base sm:text-lg leading-8">أصمم وأنفذ حلولًا للأمن المعلوماتي تتوافق مع العمليات التجارية الفعلية، لا مع النماذج النظرية المجردة.</p>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 pb-8" data-about-filter dir="rtl">
  <div class="overflow-visible">
    <div class="flex flex-wrap items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="about-filter-button rounded-md px-4 py-2 text-right text-xs uppercase tracking-[0.08em] text-slate-300 bg-gradient-to-r from-cyan-500/25 to-fuchsia-500/15 shadow-[0_0_16px_rgba(34,211,238,0.25)] sm:text-sm" data-filter="page">📘 حول الصفحة</button>
      <button type="button" class="about-filter-button rounded-md px-4 py-2 text-right text-xs uppercase tracking-[0.08em] text-slate-300 hover:text-cyan-200 hover:bg-white/5 sm:text-sm" data-filter="me">👤 نبذة عني</button>
      <button type="button" class="about-filter-button rounded-md px-4 py-2 text-right text-xs uppercase tracking-[0.08em] text-slate-300 hover:text-cyan-200 hover:bg-white/5 sm:text-sm" data-filter="links">🔗 الروابط / القنوات</button>
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

  .about-lead {
    position: relative;
    padding-right: 1.25rem;
  }

  .about-lead::before {
    content: '';
    position: absolute;
    right: 0;
    top: 0.15rem;
    bottom: 0.15rem;
    width: 2px;
    border-radius: 999px;
    background: linear-gradient(180deg, rgba(34, 211, 238, 0.95), rgba(168, 85, 247, 0.55));
    box-shadow: 0 0 14px rgba(34, 211, 238, 0.3);
  }

  .about-panel {
    border: 1px solid rgba(34, 211, 238, 0.12);
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.72), rgba(2, 6, 23, 0.4));
    border-radius: 1rem;
    padding: 1.15rem 1.1rem 1.2rem;
  }

  .about-section-heading {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    width: fit-content;
    padding: 0.5rem 0.9rem;
    border: 1px solid rgba(34, 211, 238, 0.28);
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(8, 47, 73, 0.9), rgba(30, 41, 59, 0.78));
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.03), 0 0 20px rgba(34, 211, 238, 0.12);
    color: rgb(165, 243, 252);
    letter-spacing: 0.16em;
  }

  .about-section-heading::before {
    content: none;
  }

  .about-list {
    list-style: none;
    padding-right: 0;
  }

  .about-list li {
    position: relative;
    padding-right: 1.35rem;
  }

  .about-list li::before {
    content: '';
    position: absolute;
    right: 0;
    top: 0.8rem;
    width: 0.45rem;
    height: 0.45rem;
    border-radius: 999px;
    background: rgba(34, 211, 238, 0.9);
    box-shadow: 0 0 12px rgba(34, 211, 238, 0.28);
  }

  .about-link-block {
    padding-right: 0.95rem;
    border-right: 1px solid rgba(148, 163, 184, 0.24);
  }

  .about-social-row {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    flex-wrap: wrap;
  }

  .about-social-meta {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    color: rgb(241, 245, 249);
    font-weight: 600;
  }

  .about-social-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 2rem;
    height: 2rem;
    padding: 0 0.45rem;
    border-radius: 0.6rem;
    font-size: 0.7rem;
    line-height: 1;
    letter-spacing: 0.06em;
    border: 1px solid rgba(148, 163, 184, 0.24);
    background: rgba(15, 23, 42, 0.78);
    color: rgb(226, 232, 240);
  }

  .about-social-badge--mail {
    background: rgba(14, 165, 233, 0.14);
    border-color: rgba(14, 165, 233, 0.28);
    color: rgb(125, 211, 252);
  }

  .about-social-badge--gh {
    background: rgba(148, 163, 184, 0.14);
    border-color: rgba(148, 163, 184, 0.3);
    color: rgb(226, 232, 240);
  }

  .about-social-badge--blog {
    background: rgba(168, 85, 247, 0.14);
    border-color: rgba(168, 85, 247, 0.28);
    color: rgb(216, 180, 254);
  }

  .about-social-badge--in {
    background: rgba(37, 99, 235, 0.14);
    border-color: rgba(37, 99, 235, 0.28);
    color: rgb(147, 197, 253);
  }

  .about-social-link {
    color: rgb(103, 232, 249);
    text-decoration: underline;
    text-underline-offset: 4px;
    overflow-wrap: anywhere;
  }

  .about-social-link:hover {
    color: rgb(165, 243, 252);
  }

  .about-body {
    gap: 1.9rem;
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

  @media (max-width: 640px) {
    .about-card {
      padding-top: 1.5rem;
      padding-left: 1.1rem;
      padding-right: 1.1rem;
      padding-bottom: 1.2rem;
    }

    .about-panel {
      padding: 1rem;
    }

    .about-section-heading {
      padding: 0.45rem 0.75rem;
      letter-spacing: 0.1em;
    }

    .about-link-block {
      padding-right: 0.8rem;
    }

    .about-social-row {
      align-items: flex-start;
      flex-direction: column;
      gap: 0.65rem;
    }
  }
</style>

<section class="max-w-6xl mx-auto px-4 pb-20" dir="rtl">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-8">
    <article class="about-filter-item about-card rounded-xl flex flex-col gap-4 text-right" data-about-category="page">
      <p class="text-sm text-slate-400">الغرض من هذا القسم ونطاقه ضمن ملف تدقيق الأمن السيبراني.</p>
    </article>

    <article class="about-filter-item about-card rounded-xl flex flex-col about-body text-right" data-about-category="me">
      <div class="about-lead space-y-5 text-sm leading-8 text-slate-300">
        <p>أصمم وأنفذ حلولًا للأمن المعلوماتي تتوافق مع العمليات التجارية الفعلية، لا مع النماذج النظرية المجردة.</p>
        <p>أركّز على بناء أنظمة مرنة، لا على مجرد معالجة الثغرات. وأجمع بين الضوابط التقنية والممارسات الإدارية لضمان أن تكون القرارات الأمنية قابلة للتوسع، واضحة للإدارة، وقابلة للدفاع عنها على مستوى الحوكمة.</p>
        <p>لدي خبرة عملية مع بنى تحتية صناعية، حيث تتحول الأعطال التقنية مباشرة إلى أثر مالي وتشغيلي. وقد شكّل ذلك منهجًا عمليًا لدي: كل إجراء أمني يجب أن يبرر كلفته، وكل معمارية يجب أن تتحمل الفشل.</p>
        <p>أنا لا أبحث عن أمن مثالي، بل أبني أنظمة تستمر في العمل تحت الضغط.</p>
      </div>

      <div class="about-panel space-y-4">
        <h4 class="about-section-heading text-sm font-semibold uppercase tracking-[0.12em] text-cyan-300">النهج</h4>
        <ul class="about-list space-y-4 text-sm leading-8 text-slate-300">
          <li>أبحث عن نقاط ضعف غير تقليدية في النظام وفي الأعمال لاكتشاف المخاطر قبل أن تتحول إلى حوادث وخسائر.</li>
          <li>أسترشد بنظرية المخاطر الاحتمالية وأقيّم التهديدات وفق احتمال التحقق، وحجم الأثر، وقدرة النظام على امتصاص الفشل.</li>
          <li>الأمن عملية تكرارية. إذا لم تنجح الاستراتيجية، تُعاد صياغتها بدل الدفاع عنها.</li>
          <li>أستخدم الذكاء الاصطناعي كأداة تعزيز، لا كبديل عن الحكم الهندسي.</li>
          <li>أعطي الأولوية للرؤية، وقابلية التدقيق، وتحمل الأعطال بدل الاكتفاء بالامتثال الشكلي.</li>
        </ul>
      </div>

      <div class="about-panel space-y-4">
        <h4 class="about-section-heading text-sm font-semibold uppercase tracking-[0.12em] text-cyan-300">نماذج من العمل</h4>
        <div class="space-y-6 text-sm leading-8 text-slate-300">
          <div class="about-link-block">
            <p class="font-medium text-slate-100">نماذج التقارير:</p>
            <a class="text-cyan-300 hover:text-cyan-200 underline underline-offset-4 break-all" href="/ar/reports/">/ar/reports/</a>
          </div>
          <div class="about-link-block">
            <p class="font-medium text-slate-100">إطلاق تطبيق جوال خلال 3 أشهر من الفكرة إلى الإنتاج:</p>
            <p>Kotlin / Jetpack / Snyk / SonarCloud</p>
            <a class="text-cyan-300 hover:text-cyan-200 underline underline-offset-4 break-all" href="https://www.rustore.ru/catalog/app/ru.datadef.tenarhiva" target="_blank" rel="noopener noreferrer">https://www.rustore.ru/catalog/app/ru.datadef.tenarhiva</a>
            <p class="text-slate-400">إصدار Google Play قيد التنفيذ.</p>
          </div>
        </div>
      </div>

      <div class="about-panel space-y-4">
        <h4 class="about-section-heading text-sm font-semibold uppercase tracking-[0.12em] text-cyan-300">المجالات الأساسية</h4>
        <ul class="about-list space-y-4 text-sm leading-8 text-slate-300">
          <li>معمارية أمن المعلومات</li>
          <li>تقييم المخاطر والتدقيق</li>
          <li>ممارسات التطوير الآمن</li>
          <li>التحقيق الرقمي والتشفير (تركيز مستمر)</li>
        </ul>
      </div>
    </article>

    <article class="about-filter-item about-card rounded-xl flex flex-col about-body text-right" data-about-category="links">
      <div class="about-panel space-y-4">
        <h4 class="about-section-heading text-sm font-semibold uppercase tracking-[0.12em] text-cyan-300">الروابط / القنوات</h4>
        <p class="text-sm leading-8 text-slate-300">روابط وقنوات عامة يمكن استخدامها للتواصل، والوصول إلى المشاريع، ومراجعة أمثلة العمل.</p>
      </div>

      <div class="about-panel space-y-6 text-sm leading-8 text-slate-300">
        <div class="about-link-block">
          <div class="about-social-row">
            <div class="about-social-meta">
              <span class="about-social-badge about-social-badge--mail" aria-hidden="true">@</span>
              <span>البريد الإلكتروني</span>
            </div>
            <a class="about-social-link" href="mailto:blackIce6573@DataDef.ae">blackIce6573@DataDef.ae</a>
          </div>
        </div>
        <div class="about-link-block">
          <div class="about-social-row">
            <div class="about-social-meta">
              <span class="about-social-badge about-social-badge--blog" aria-hidden="true">BL</span>
              <span>المدونة</span>
            </div>
            <a class="about-social-link" href="https://datadef.ae/blog/" target="_blank" rel="noopener noreferrer">datadef.ae/blog/</a>
          </div>
        </div>
        <div class="about-link-block">
          <div class="about-social-row">
            <div class="about-social-meta">
              <span class="about-social-badge about-social-badge--in" aria-hidden="true">in</span>
              <span>LinkedIn</span>
            </div>
            <a class="about-social-link" href="https://www.linkedin.com/in/novikov-def/" target="_blank" rel="noopener noreferrer">linkedin.com/in/novikov-def/</a>
          </div>
        </div>
      </div>
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
        title: '',
        audience: 'للزوار الذين يحتاجون إلى فهم سياق هذا القسم.',
        focus: 'التركيز: ما الذي تحتويه الصفحة ولماذا أُنشئت.'
      },
      me: {
        title: '',
        audience: 'للفرق وأصحاب المصلحة الذين يراجعون الملف الشخصي.',
        focus: 'التركيز: الخبرة والتخصص والخلفية في الأمن السيبراني.'
      },
      links: {
        title: '',
        audience: 'للزوار الذين يريدون الوصول السريع إلى القنوات العامة وروابط المشاريع.',
        focus: 'التركيز: وسائل التواصل، GitHub، وروابط المشاريع الخارجية.'
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
        descriptionTitle.style.display = descriptions[category].title ? '' : 'none';
        descriptionAudience.textContent = descriptions[category].audience;
        descriptionFocus.textContent = descriptions[category].focus;
      }
    }

    buttons.forEach(function (button) {
      button.addEventListener('click', function () {
        setFilter(button.getAttribute('data-filter'));
      });
    });

    setFilter('me');
  });
</script>
