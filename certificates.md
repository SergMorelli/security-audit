---
layout: default
title: Certificates
permalink: /certificates/
lang: en
translation_key: certificates
---

<section class="pt-14 pb-10 md:pt-32 md:pb-20 text-center">
  <h1 class="text-4xl text-cyan-400 mb-6">Certificates</h1>
  <p class="text-gray-400 max-w-xl mx-auto">Professional training certificates from leading cybersecurity and technology platforms.</p>
</section>

<style>
  .cert-card {
    border: 1px solid rgba(71, 85, 105, 0.65);
    background: linear-gradient(165deg, rgba(8, 14, 28, 0.96), rgba(2, 8, 23, 0.86));
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }

  @media (hover: hover) {
    .cert-card:hover {
      transform: translateY(-4px);
      border-color: rgba(34, 211, 238, 0.75);
      box-shadow: 0 0 0 1px rgba(34, 211, 238, 0.25), 0 0 28px rgba(34, 211, 238, 0.25);
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
    gap: 0.4rem;
    padding: 0.45rem 1rem;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    border-radius: 0.4rem;
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

<section class="max-w-5xl mx-auto px-4 pb-20">
  <div class="grid grid-cols-1 gap-6">

    <!-- ── SAMPLE CERTIFICATE CARD ─────────────────────────────── -->
    <!-- Replace the placeholder values below with your actual data -->
    <div class="cert-card rounded-xl p-6" data-aos="fade-up">

      <!-- Top row: corporation badge + date -->
      <div class="flex items-center justify-between flex-wrap gap-3 mb-5">
        <span class="cert-badge">
          <img src="https://www.google.com/s2/favicons?sz=32&domain=coursera.org" alt="Coursera" class="w-4 h-4 rounded-sm">
          Coursera
        </span>
        <span class="text-xs text-gray-500 font-mono">2024</span>
      </div>

      <!-- Course title -->
      <h2 class="text-lg md:text-xl font-bold text-white mb-3 leading-snug">
        <!-- TODO: replace with actual course name -->
        Introduction to Cybersecurity Tools &amp; Cyber Attacks
      </h2>

      <!-- Description -->
      <p class="text-sm text-gray-400 leading-relaxed mb-6">
        <!-- TODO: replace with actual description -->
        Covers the history of cybersecurity and an overview of common attack types, including social engineering, phishing,
        malware, and network-based exploits. Introduces key security tools used in threat detection and incident response.
      </p>

      <div class="border-t border-slate-700/60 mb-5"></div>

      <!-- Action buttons -->
      <div class="flex flex-wrap gap-3 items-center">

        <!-- Link to official verification page -->
        <a
          href="https://coursera.org/verify/5N2LNGY9T8KH"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn primary"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
          Verify on Coursera
        </a>

        <!-- PDF download -->
        <a
          href="/sertificate/Coursera 5N2LNGY9T8KH.pdf"
          download
          class="cert-action-btn"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
          Download PDF
        </a>

        <!-- Toggle PDF preview -->
        <button
          type="button"
          class="cert-action-btn"
          onclick="
            var preview = this.closest('.cert-card').querySelector('.cert-pdf-preview');
            var isOpen = preview.classList.toggle('open');
            this.textContent = isOpen ? '▲ Hide Preview' : '▼ Preview PDF';
          "
        >
          ▼ Preview PDF
        </button>

      </div>

      <!-- PDF preview panel (hidden by default) -->
      <div class="cert-pdf-preview">
        <iframe
          src="/sertificate/Coursera 5N2LNGY9T8KH.pdf"
          class="w-full"
          style="height: 520px;"
          title="Certificate PDF preview"
          loading="lazy"
        ></iframe>
      </div>

    </div>
    <!-- ── END CERTIFICATE CARD ─────────────────────────────────── -->

  </div>
</section>
