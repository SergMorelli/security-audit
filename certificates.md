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
        <div class="flex items-center gap-2">
          <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg" alt="IBM" class="rounded-sm bg-white/95" style="width:46px;height:23px;max-width:46px;max-height:23px;object-fit:contain;display:block;" title="IBM (International Business Machines)">
          <img src="https://www.google.com/s2/favicons?sz=32&domain=credly.com" alt="Credly" class="w-7 h-7 rounded-sm" title="Credly">
        </div>
      </div>

      <!-- Course title -->
      <h2 class="text-lg md:text-xl font-bold text-white mb-3 leading-snug">
        IT Fundamentals for Cybersecurity
      </h2>

      <ul class="text-sm text-gray-400 leading-relaxed mb-5 list-disc list-inside space-y-1">
        <li>Introduction to Cybersecurity Tools &amp; Cyberattacks</li>
        <li>Operating Systems: Overview, Administration, and Security</li>
        <li>Cybersecurity Compliance Framework, Standards &amp; Regulations</li>
        <li>Computer Networks and Network Security</li>
      </ul>

      <div class="border-t border-slate-700/60 mb-3"></div>

      <!-- Action buttons -->
      <div class="cert-actions">

        <a
          href="https://www.credly.com/badges/1b730c34-a8b6-4d97-8232-af097c3cb48e/public_url"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn primary"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 4v5c0 5-3.5 8-7 9-3.5-1-7-4-7-9V7l7-4z"/></svg>
          Badge Credly
        </a>

        <!-- Link to official verification page -->
        <a
          href="https://coursera.org/share/a316fe91058dde6567813a3f3a316753"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
          Verify on Coursera
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
          src="{{ '/sertificate/Coursera 5N2LNGY9T8KH.pdf' | relative_url }}"
          class="w-full"
          style="height: 520px;"
          title="Certificate PDF preview"
          loading="lazy"
        ></iframe>
      </div>

    </div>
    <!-- ── END CERTIFICATE CARD ─────────────────────────────────── -->

    <div class="cert-card rounded-xl p-6" data-aos="fade-up">
      <div class="flex items-center justify-between flex-wrap gap-3 mb-5">
        <span class="cert-badge">
          <img src="https://www.google.com/s2/favicons?sz=32&domain=coursera.org" alt="Coursera" class="w-4 h-4 rounded-sm">
          Coursera
        </span>
        <img src="https://logo.clearbit.com/eccouncil.org" alt="EC-Council" class="rounded-sm bg-white px-1 py-0.5" style="width:80px;height:40px;max-width:80px;max-height:40px;object-fit:contain;display:block;" title="EC-Council" onerror="this.onerror=null;this.src='https://www.google.com/s2/favicons?sz=128&domain=eccouncil.org';this.className='rounded-sm bg-white';this.style='width:40px;height:40px;max-width:40px;max-height:40px;object-fit:contain;display:block;';">
      </div>

      <h2 class="text-lg md:text-xl font-bold text-white mb-3 leading-snug">
        Cybersecurity Attack and Defense Fundamentals
      </h2>

      <ul class="text-sm text-gray-400 leading-relaxed mb-5 list-disc list-inside space-y-1">
        <li>Ethical Hacking Essentials (EHE)</li>
        <li>Network Defense Essentials (NDE)</li>
        <li>Digital Forensics Essentials (DFE)</li>
      </ul>

      <div class="border-t border-slate-700/60 mb-3"></div>

      <div class="cert-actions">
        <a
          href="https://coursera.org/share/cde0e4bf442d944f2ae3e98f72d0574d"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn primary"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
          Verify on Coursera
        </a>

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

      <div class="cert-pdf-preview">
        <iframe
          src="{{ '/sertificate/Coursera 80C2FPT2K0QG.pdf' | relative_url }}"
          class="w-full"
          style="height: 520px;"
          title="Certificate PDF preview"
          loading="lazy"
        ></iframe>
      </div>
    </div>

    <div class="cert-card rounded-xl p-6" data-aos="fade-up">
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

      <h2 class="text-lg md:text-xl font-bold text-white mb-3 leading-snug">
        Google Cybersecurity
      </h2>

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
        <a
          href="https://www.credly.com/badges/4899c982-6381-473b-915e-4479222f0cc4/public_url"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn primary"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 4v5c0 5-3.5 8-7 9-3.5-1-7-4-7-9V7l7-4z"/></svg>
          Badge Credly
        </a>

        <a
          href="https://coursera.org/share/687ca5118a74e9887b0189e0e757b135"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
          Verify on Coursera
        </a>

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

      <div class="cert-pdf-preview">
        <iframe
          src="{{ '/sertificate/Coursera A7MUSAOT3OJ0.pdf' | relative_url }}"
          class="w-full"
          style="height: 520px;"
          title="Certificate PDF preview"
          loading="lazy"
        ></iframe>
      </div>
    </div>

    <div class="cert-card rounded-xl p-6" data-aos="fade-up">
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

      <h2 class="text-lg md:text-xl font-bold text-white mb-3 leading-snug">
        Microsoft Cybersecurity Analyst
      </h2>

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
        <a
          href="https://www.credly.com/badges/b4529e87-f355-44e2-9b55-2f6f9d5e9a2a"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn primary"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 4v5c0 5-3.5 8-7 9-3.5-1-7-4-7-9V7l7-4z"/></svg>
          Badge Credly
        </a>

        <a
          href="https://coursera.org/share/c628b3add4065861f249ac0ce62e02d6"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
          Verify on Coursera
        </a>

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

      <div class="cert-pdf-preview">
        <iframe
          src="{{ '/sertificate/Coursera KLBK3U18FQHA.pdf' | relative_url }}"
          class="w-full"
          style="height: 520px;"
          title="Certificate PDF preview"
          loading="lazy"
        ></iframe>
      </div>
    </div>

    <div class="cert-card rounded-xl p-6" data-aos="fade-up">
      <div class="flex items-center justify-between flex-wrap gap-3 mb-5">
        <span class="cert-badge">
          <img src="https://www.google.com/s2/favicons?sz=32&domain=coursera.org" alt="Coursera" class="w-4 h-4 rounded-sm">
          Coursera
        </span>
        <img src="https://logo.clearbit.com/learnkarts.com" alt="Learnkarts" class="rounded-sm bg-white px-1 py-0.5" style="width:68px;height:34px;max-width:68px;max-height:34px;object-fit:contain;display:block;" title="Learnkarts" onerror="this.onerror=null;this.src='https://www.google.com/s2/favicons?sz=128&domain=learnkarts.com';this.className='rounded-sm bg-white';this.style='width:40px;height:40px;max-width:40px;max-height:40px;object-fit:contain;display:block;';">
      </div>

      <h2 class="text-lg md:text-xl font-bold text-white mb-3 leading-snug">
        Ethical Hacking
      </h2>

      <ul class="text-sm text-gray-400 leading-relaxed mb-5 list-disc list-inside space-y-1">
        <li>Ethical Hacking Fundamentals</li>
        <li>System &amp; Network Security Essentials</li>
        <li>Advanced Ethical Hacking &amp; Cybersecurity</li>
        <li>Ethical Hacking Practice Project &amp; Questions</li>
      </ul>

      <div class="border-t border-slate-700/60 mb-3"></div>

      <div class="cert-actions">
        <a
          href="https://coursera.org/share/0d934c9e95db8ea390fa9085e7a7fcfc"
          target="_blank"
          rel="noopener noreferrer"
          class="cert-action-btn primary"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
          Verify on Coursera
        </a>

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

      <div class="cert-pdf-preview">
        <iframe
          src="{{ '/sertificate/Coursera PSYSKZY1K3EC.pdf' | relative_url }}"
          class="w-full"
          style="height: 520px;"
          title="Certificate PDF preview"
          loading="lazy"
        ></iframe>
      </div>
    </div>

  </div>
</section>
