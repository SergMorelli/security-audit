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
      <button type="button" class="about-filter-button px-4 py-2 text-xs sm:text-sm uppercase tracking-[0.08em] rounded-md text-slate-300 hover:text-cyan-200 hover:bg-white/5" data-filter="links">🔗 Links / Socials</button>
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
          <li>I look for unconventional points of vulnerability in both systems and business operations to surface risks before they turn into incidents and losses.</li>
          <li>I rely on probabilistic risk theory and assess threats through likelihood, impact, and the system&apos;s ability to absorb failure.</li>
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

    <article class="about-filter-item about-card rounded-xl flex flex-col about-body" data-about-category="links">
      <div class="about-panel space-y-4">
        <h4 class="about-section-heading text-sm font-semibold uppercase tracking-[0.12em] text-cyan-300">Links / Socials</h4>
        <p class="text-sm leading-8 text-slate-300">Public links and channels for contact, project access, and selected work references.</p>
      </div>

      <div class="about-panel space-y-6 text-sm leading-8 text-slate-300">
        <div class="about-link-block">
          <div class="about-social-row">
            <div class="about-social-meta">
              <span class="about-social-badge about-social-badge--mail" aria-hidden="true">@</span>
              <span>Email</span>
            </div>
            <a class="about-social-link" href="mailto:blackIce6573@DataDef.ae">blackIce6573@DataDef.ae</a>
          </div>
        </div>
        <div class="about-link-block">
          <div class="about-social-row">
            <div class="about-social-meta">
              <span class="about-social-badge about-social-badge--gh" aria-hidden="true">GH</span>
              <span>GitHub</span>
            </div>
            <a class="about-social-link" href="https://github.com/SergMorelli" target="_blank" rel="noopener noreferrer">github.com/SergMorelli</a>
          </div>
        </div>
        <div class="about-link-block">
          <div class="about-social-row">
            <div class="about-social-meta">
              <span class="about-social-badge about-social-badge--blog" aria-hidden="true">BL</span>
              <span>Blog</span>
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
        audience: 'For visitors who need context for this section.',
        focus: 'Focus: what this page contains and why it exists.'
      },
      me: {
        title: '',
        audience: 'For teams and stakeholders reviewing my profile.',
        focus: 'Focus: expertise, specialization, and security background.'
      },
      links: {
        title: '',
        audience: 'For visitors who want direct access to public channels and project links.',
        focus: 'Focus: contact details, GitHub, and external project references.'
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

