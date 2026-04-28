---
layout: default
title: About
permalink: /about/
lang: en
translation_key: about
---

<section class="max-w-6xl mx-auto px-4 pt-32 pb-12">
  <div class="max-w-4xl rounded-xl border border-cyan-400/10 bg-slate-950/35 px-6 py-5 backdrop-blur-sm">
    <p class="text-left text-gray-300 text-base sm:text-lg leading-8">I design and implement information security solutions that align with real business operations, not theoretical models.</p>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 pb-8" data-about-filter>
  <div class="overflow-x-auto">
    <div class="flex min-w-max items-center gap-2 rounded-xl p-2 bg-slate-900/45 ring-1 ring-cyan-400/20 backdrop-blur-md shadow-[0_0_30px_rgba(34,211,238,0.14)]">
      <button type="button" class="about-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 bg-gradient-to-r from-cyan-500/25 to-fuchsia-500/15 shadow-[0_0_16px_rgba(34,211,238,0.25)]" data-filter="page">📘 About this page</button>
      <button type="button" class="about-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="me">👤 About me</button>
    </div>
  </div>
  <div id="aboutFilterDescription" class="mt-4 rounded-lg bg-slate-900/40 ring-1 ring-cyan-400/20 px-4 py-3">
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
    padding-left: 1.25rem;
  }

  .about-lead::before {
    content: '';
    position: absolute;
    left: 0;
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
  }

  .about-section-heading::before {
    content: '';
    width: 0.7rem;
    height: 0.7rem;
    border-radius: 999px;
    background: radial-gradient(circle, rgba(34, 211, 238, 0.95) 0%, rgba(34, 211, 238, 0.15) 70%);
    box-shadow: 0 0 16px rgba(34, 211, 238, 0.35);
  }

  .about-list {
    list-style: none;
    padding-left: 0;
  }

  .about-list li {
    position: relative;
    padding-left: 1.35rem;
  }

  .about-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0.8rem;
    width: 0.45rem;
    height: 0.45rem;
    border-radius: 999px;
    background: rgba(34, 211, 238, 0.9);
    box-shadow: 0 0 12px rgba(34, 211, 238, 0.28);
  }

  .about-link-block {
    padding-left: 0.95rem;
    border-left: 1px solid rgba(148, 163, 184, 0.24);
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
</style>

<section class="max-w-6xl mx-auto px-4 pb-20">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-8">
    <article class="about-filter-item about-card rounded-xl flex flex-col gap-4" data-about-category="page">
      <p class="text-sm text-slate-400">Purpose and scope of this section in the security audit portfolio.</p>
    </article>

    <article class="about-filter-item about-card rounded-xl flex flex-col about-body" data-about-category="me">
      <div class="about-lead space-y-5 text-sm leading-8 text-slate-300">
        <p>I design and implement information security solutions that align with real business operations, not theoretical models.</p>
        <p>My focus is on building resilient systems, not just patching vulnerabilities. I combine technical controls with governance practices to ensure that security decisions scale, remain transparent, and are defensible at the management level.</p>
        <p>I have hands-on experience working with industrial infrastructure, where system failures translate directly into financial and operational impact. This shaped a pragmatic approach: every control must justify its cost, and every architecture must tolerate failure.</p>
        <p>I don&apos;t chase perfect security. I build systems that continue to operate under pressure.</p>
      </div>

      <div class="about-panel space-y-4">
        <h4 class="about-section-heading text-sm font-semibold uppercase tracking-[0.12em] text-cyan-300">Approach</h4>
        <ul class="about-list space-y-4 text-sm leading-8 text-slate-300">
          <li>Security is iterative. If a strategy doesn&apos;t hold, it gets reworked, not defended.</li>
          <li>I use AI as a force multiplier, not a decision-maker. Engineering judgment stays in control.</li>
          <li>I prioritize visibility, auditability, and failure tolerance over checkbox compliance.</li>
        </ul>
      </div>

      <div class="about-panel space-y-4">
        <h4 class="about-section-heading text-sm font-semibold uppercase tracking-[0.12em] text-cyan-300">Selected Work</h4>
        <div class="space-y-6 text-sm leading-8 text-slate-300">
          <div class="about-link-block">
            <p class="font-medium text-slate-100">Report samples:</p>
            <a class="text-cyan-300 hover:text-cyan-200 underline underline-offset-4 break-all" href="/reports/">/reports/</a>
          </div>
          <div class="about-link-block">
            <p class="font-medium text-slate-100">Mobile application delivery (3 months from idea to production):</p>
            <p>Kotlin / Jetpack / Snyk / SonarCloud</p>
            <a class="text-cyan-300 hover:text-cyan-200 underline underline-offset-4 break-all" href="https://www.rustore.ru/catalog/app/ru.datadef.tenarhiva" target="_blank" rel="noopener noreferrer">https://www.rustore.ru/catalog/app/ru.datadef.tenarhiva</a>
            <p class="text-slate-400">Google Play release in progress.</p>
          </div>
        </div>
      </div>

      <div class="about-panel space-y-4">
        <h4 class="about-section-heading text-sm font-semibold uppercase tracking-[0.12em] text-cyan-300">Core Areas</h4>
        <ul class="about-list space-y-4 text-sm leading-8 text-slate-300">
          <li>Information Security Architecture</li>
          <li>Risk Assessment and Audit</li>
          <li>Secure Development Practices</li>
          <li>Digital Forensics and Cryptography (ongoing focus)</li>
        </ul>
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
        audience: 'For visitors who need context for this section.',
        focus: 'Focus: what this page contains and why it exists.'
      },
      me: {
        title: '',
        audience: 'For teams and stakeholders reviewing my profile.',
        focus: 'Focus: expertise, specialization, and security background.'
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

