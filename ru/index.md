---
layout: default
title: Аудит безопасности
permalink: /ru/
lang: ru
translation_key: home
---

<section class="h-screen flex items-center justify-center relative overflow-hidden">

  <div class="absolute inset-0 bg-[radial-gradient(#0ff1_1px,transparent_1px)] [background-size:40px_40px] opacity-10"></div>

  <div class="absolute w-[600px] h-[600px] bg-cyan-500/20 blur-3xl rounded-full"></div>

  <div class="text-center z-10" data-aos="fade-up">

    <h1 class="text-5xl md:text-7xl font-bold text-white mb-6">
      SECURITY<br>
      <span class="text-cyan-400">AUDIT</span>
    </h1>

    <p class="text-gray-400 max-w-xl mx-auto mb-8">
      Отчеты по пентесту, анализ уязвимостей и моделирование реальных атак.
    </p>

    <div class="flex justify-center gap-4">
      <a href="{{ '/ru/reports/' | relative_url }}" class="px-6 py-3 bg-cyan-500 text-black font-bold hover:bg-cyan-400 transition">
        Смотреть отчеты
      </a>

      <a href="{{ '/ru/lab/' | relative_url }}" class="px-6 py-3 border border-red-500 text-red-400 hover:bg-red-500 hover:text-black transition">
        Открыть лабораторию
      </a>
    </div>

  </div>
</section>
