# 0.
Сегодня 2025-12-05.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021996860063292693905

## 2.2. Title
Tax Expert (Austria/Cyprus) for Cross-Border Structure & POEM Risk Assessment

## 2.3. Description
`PD` ≔ 
```text
# Project Overview
We are an Austrian business team looking for a highly experienced Tax Advisor or Tax Lawyer to review a specific cross-border structure between Austria (AT) and Cyprus (CY).

# The Situation
- We have executed a sale-to-self transaction: An asset/company previously held in Austria was sold to a newly founded Cyprus Limited.
- Structure: The Cyprus entity acts as a holding/operating company.
- Ownership: The Ultimate Beneficial Owners (UBOs) are identical in both the original Austrian entity and the new Cyprus structure.
- Substance: We have established local substance in Cyprus (Local Director, Registered Office, Secretary, etc.).

# The Challenge
We need to ensure our setup creates a robust defense against Austrian fiscal authorities claiming Place of Effective Management (POEM/Ort der Geschäftsleitung) remains in Austria. 
We are fully aware of the risks regarding CFC rules (Hinzurechnungsbesteuerung) and general anti-avoidance rules (GAAR).
```

## 2.5. Questions
### 2.5.1.
Regarding POEM (Place of Effective Management) in a Cyprus-Austria setup: Aside from a local director, what are the top 3 specific operational factors Austrian authorities check to prove management is actually happening in Austria?

### 2.5.2.
Since this is a "related party transaction" (sale to self): How do you typically advise clients to document the valuation to prevent issues with "Verdeckte Gewinnausschüttung" (hidden profit distribution) or Transfer Pricing audits in Austria?

### 2.5.3.
lease briefly describe your experience with international taxation. 
Have you handled tax audits (Betriebsprüfung) in this context?

# 5. Информация о `ꆜ`
## 5.1. Местоположение
Cyprus
Larnaca

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Nov 24, 2025
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
2
### 5.3.4. Total spent (USD)
2K
### 5.3.5. Количество оплаченных часов в почасовых проектах
83
### 5.3.6. Средняя почасовая ставка (USD)
46.46

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021996173974471583763

### 6.1.2. Title
Senior AI Engineer (Python/Async): Build High-Performance Multi-Model LLM Orchestrator

### 6.1.3. Description
`P1D` ≔ 
```text
We are building a cutting-edge LLM Orchestration Layer designed to outperform single models (like GPT-4) by intelligently routing, combining, and ranking outputs from multiple top-tier providers (OpenAI, Anthropic, Gemini, Llama 3 via Groq) in real-time.

The Goal: Create a system that queries multiple models in parallel, handles race conditions, and delivers the single best answer (or a synthesized fusion) to the user with minimal latency.

The Scope (4-Week Sprint):

- Parallel Execution Engine: Build a Python-based engine (asyncio) to query 3-5 LLMs simultaneously.

- Smart Routing & Fallback: Implement logic to route queries based on complexity and handle API failures/timeouts instantly.

- Response Fusion: Develop a logic layer to rank or merge responses (e.g., "Take code from Claude, explanation from GPT-4").

- Streaming Architecture: Ensure the frontend receives the first token as fast as possible (Time-to-First-Token optimization) via SSE/WebSockets.


⚠️ Who we are NOT looking for:

- Developers who rely 100% on heavy frameworks (like LangChain) for simple logic. We need clean, performant custom code.

- "Prompt Engineers" without solid backend engineering skills.


The Hiring Process:

- Short screening of your profile/portfolio.

- Paid Assessment (2-3 hours): We will pay you to build a mini-prototype of the parallel query logic.

- Kick-off for the full 4-week project.

To Apply: Please answer the screening questions below. Proposals with generic AI-generated cover letters will be ignored.

- In a FastAPI async endpoint, how do you handle heavy CPU-bound tasks (e.g., parsing) without blocking the main event loop? Which specific Python method or executor do you use to offload these tasks to keep the server responsive?
- We stream via SSE. How do you implement a Python generator that queries 2 LLMs in parallel and yields chunks from whichever model responds first? Mention the specific asyncio function or queue pattern you would use to merge streams.
- OpenAI API fails often. Beyond try/except, how do you implement 'Exponential Backoff' or a 'Circuit Breaker' to prevent the system from hanging? Name the specific Python library (e.g. tenacity) or custom logic you use for retries.
```

### 6.1.4. Publication Date
Nov 24, 2025

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 8.
## 8.1.
`С⁎` ≔ 
```
Компания `ꆜ`:
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
ensure our setup creates a robust defense against Austrian fiscal authorities claiming Place of Effective Management (POEM/Ort der Geschäftsleitung) remains in Austria
~~~
```

# 11.
## 11.1.
`Q1⁎` ≔ (Вопрос `ꆜ` §2.5.1)

## 11.2.
`Q2⁎` ≔ (Вопрос `ꆜ` §2.5.2)

## 11.3.
`Q3⁎` ≔ (Вопрос `ꆜ` §2.5.3)
