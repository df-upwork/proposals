# 1. `B.md`
~~~~~~markdown
# 1. `᛭MDi`
## 1.1.
Каждый отдельный (произвольный, неопределённый) документ в формате Markdown, прикреплённый мной к этому запросу, буду обозначать `᛭Di`.
## 1.2.
Имя файла `᛭Di` всегда имеет расширение `.md`.
## 1.3.
Множество всех `᛭Di` буду обозначать `᛭Ds`.

# 2. `L.md`
### 2.1.
`L.md` ∈ `᛭Ds`.
## 2.2.
`L.md` описывает полуформальный язык: `᛭L`.
## 2.3.
Большинство `᛭Di` написаны на `᛭L`.
## 2.4.
Множество всех `᛭Di`, написанных на `᛭L`, буду обозначать `᛭DLs`.
Таким образом, `᛭DLs` ⊆ `᛭Ds`. 

# 3. `O.md`
## 3.1.
`O.md` ∈ `᛭DLs`
## 3.2.
`O.md` описывает некую **онтологию** (`᛭O`)  — модель предметной области, в которой тебе предстоит решать задачу.
«An **ontology** encompasses a representation, formal naming, and definitions of the categories, properties, and relations between the concepts, data, or entities»: https://en.wikipedia.org/wiki/Ontology_(information_science)

# 4. `T.md`
## 4.1.
`T.md` ∈ `᛭DLs`
## 4.2.
`T.md` описывает задачу (`᛭T`), которую ты должен решить.

# 5. Порядок твоих действий
Действуй пошагово:
## 5.1.
Сначала внимательно и полностью прочитай `L.md`.
В точности запомни его содержание.

## 5.2.
Затем внимательно и полностью прочитай `O.md`. 
В точности запомни его содержание.

## 5.3.
Затем внимательно и полностью прочитай `T.md`. 
Выполни `᛭T`.

# 6. Требования к заголовкам в твоём ответе
## 6.1.
У твоего ответа не должно быть одного общего заголовка, потому что твой ответ будет вставлен внутрь секции 1-го уровня (`#`) другого документа Markdown.
## 6.2.
Исходя из §6.1, в качестве заголовков верхего уровня ты должен использовать заголовки 2-го уровня (`##`).
Таких заголовков должно быть несколько: тем самым ты разбиваешь свой ответ на разделы.
Если твой ответ краток, то не разбивай его на разделы вообще.
## 6.3.
Разумеется, ты также можешь использовать заголовки более нижних уровней внутри заголовков 2-го уровня: для дополнительной структуризации текста.
## 6.4.
Никогда не используй выделение жирным (`**`) в заголовках.
## 6.5.
Всегда форматируй заголовки только символами решётки (`#`), не другими способами. 

~~~~~~

# 2. `L.md`
~~~~~~markdown
# 1. `≔`
## 1.1.
- `≔` — это бинарный оператор.
## 1.2.
`A ≔ B` means that `A` **denotes** `B`.
## 1.3.
Я использую `≔` для сокращения записи.
В выражении `A ≔ B` `B` обычно — это длинный текст, а `A` — это более короткое обозначение.  
## 1.4.
~~~code
A ≔
```
B
```
~~~
равнозначно `A ≔ B` и используется, когда `B` — многострочный текст.

# 2. `→`
~~~code
A → B
~~~
denotes a material conditional (https://en.wikipedia.org/wiki/Material_conditional)

# 3. `⊢`
~~~code
A ⊢ B
~~~
denotes a logical consequence (https://en.wikipedia.org/wiki/Logical_consequence)

# 4. `⊤`
## 4.1.
~~~code
⊤ B
~~~
means that `B` is true (is a fact).

## 4.2.
~~~code
⊤⟦Rs⟧ B
~~~
means:
```
(⊤ `B`) AND (`Rs` are the reasons why `B` is true)
```

## 4.3.
~~~code
A ≔⊤
```
B
```
~~~
means:
```code
(`A` ≔ `B`) AND (⊤ `B`).
```

## 4.4.
~~~code
A ≔⊤⟦Rs⟧
```
B
```
~~~
means:
```code
(`A` ≔ `B`) AND (⊤⟦Rs⟧ B).
```

# 5. `≔!`
## 5.1.
~~~code
A ≔! B
~~~
means:
```code
(`A` ≔⊤ `B`) AND (`B` is surprising).
```

## 5.2.
~~~code
A ≔!⟦Rs⟧ B
~~~
means:
```code
(`A` ≔⊤⟦Rs⟧ `B`) AND (`B` is surprising).
```

# 6. `?`
## 6.1.
~~~code
? B
~~~
means that `B` is a hypothesis.

## 6.2.
~~~code
?⟦Rs⟧ B
~~~
means:
```code
(? `B`) AND (`Rs` are the reasons for the hypothesis)
```

## 6.3.
~~~code
A ≔? B
~~~
means:
```code
(? `B`) AND (`A` ≔ `B`)
```

## 6.4.
~~~code
A ≔?⟦Rs⟧ B
~~~
means:
```code
(?⟦Rs⟧ `B`) AND (`A` ≔ `B`)
```

# 7.
## 7.1.
~~~code
A : S ≔ B
~~~
means:
```code
(`A` ≔ `B`) AND (`A` ∈ `S`).
```

## 7.2.
~~~code
A : S
~~~
means:
```code
`A` : `S` ≔ (an arbitrary element of `S`)
```

# 8. `⠿{…}`
## 8.1. `⠿{I₁, I₂, …, Iₙ}`
`⠿{I₁, I₂, …, Iₙ}` обозначает множество, заданное точным перечислением всех его элементов: {`I₁`, `I₂`, …, `Iₙ`}.

## 8.2. `⠿{I₁-Iₙ}` 
`⠿{I₁-Iₙ}` обозначает множество, заданное интервалом (диапазоном) его значений.
Это множество, в числе прочего, включает границы указанного интервала: `I₁` и `Iₙ`.

# 9. `⠿~`
## 9.1. `⠿~ (D)`
`⠿~ (D)` обозначает множество, заданное неформальным (словесным) описанием его элементов (`D`).

## 9.2.
~~~code
⠿~
```
D
```	
~~~
равнозначно `⠿~ (D)` и используется, когда `D` — многострочный текст.

## 9.3.
~~~code
S ≔ ⠿~ (D)
```yaml
- I₁
- I₂
- …
- Iₙ
```	
~~~
означает: (`S ≔ ⠿~ (D)`) AND (⠿{`I₁`, `I₂`, …, `Iₙ`} ⊆ `S`) .

# 10.
## 10.1.
`᛭DLi` : `᛭DLs`
## 10.2.
### 10.2.1.
`᛭Dc` — это обозначение `᛭DLi` самого себя.
Другими словами, если текст `᛭DLi` содержит упоминание `᛭Dс` — это значит, что `᛭Di` упоминает сам себя. 
### 10.2.2.
Например: если имя файла `᛭Di` — `sample.md`, и текст `sample.md` использует обозначение `᛭Dc`, это значит, что `᛭Dc` в данном случае обозначает документ `sample.md`.  

# 11. `§`
## 11.1.
~~~code
§P
~~~
означает ссылку на пункт `P` `᛭Dc`.
Например, §8.2.2 означает ссылку на пункт 8.2.2 `᛭Dc`.
## 11.2.
~~~code
`᛭DLi`::§P
~~~
означает ссылку на пункт `P` `᛭DLi`.
  
# 12. Local Definitions
## 12.1.
~~~code
A[§P] ≔ B
~~~
Означает:
- Для понятия `B` я **временно**, **только в рамках** §`P`, использую обозначение `A`.
- Вне §`P` это правило не применяется: в частности, если до §`P` обозначение `A` имело другой смысл, то после §`P` обозначение `A` снова будет иметь этот смысл.
- По сути, `A[§P] ≔ B` объявляет **локальную переменную** `A` с **областью действия** §`P`.
- В отличие от `A[§P] ≔ B`, `A ≔ B` объявляет **глобальную переменную** `A`.

## 12.2.
~~~code
A[§P₁, §P₂, …, §Pₙ] ≔ B
~~~
Означает, что обозначение `A` имеет значение `B` в контексте ⠿{§`P₁`, §`P₂`, …, §`Pₙ`}.
По сути, это правило аналогично §12.1, но область действия локальной переменной `A` ограничивается не одним пунктом, а множеством пунктов.

## 12.3.
~~~code
A[§P₁-§Pₙ] ≔ B
~~~
Означает, что обозначение `A` имеет значение `B` в контексте ⠿{§P₁-§Pₙ}.
По сути, это правило аналогично §12.1 и §12.2.

# 13. `≔†`
~~~code
A ≔† B
~~~
means:
```code
(`A` ≔ `B`) AND (`B` is a **problem** to me).
```

# 14. `▶`
```code
▶ A
```
означает, что в описываемой мной ситуации я использую `A`.

# 15. `ⰳ`
```code
Aⰳ(a, b, …) ≔ B
```
means:
- `A` — это функция с параметрами ⠿{`a`, `b`, …}.
- `B` — семантика `A`

# 16. `߷`
## 16.1.
```
߷⠿ ≔ ⠿~ (приложенные к этому запросу файлы)
```

## 16.2.
```code
߷ⰳ(ID, Name) ≔ Desc
```
means:
```code
- `ID` : `߷⠿` ≔ `Desc`
- `Name` — имя файла
```


~~~~~~

# 3. `O.md`
~~~~~~markdown
# 0.
Сегодня 2025-11-21.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021991626840386871934

## 2.2. Title
Fix Polymarket API Authentication (Python Bot) – 401 Unauthorized Error

## 2.3. Description
`PD` ≔ 
~~~text
# Project Type
One-time fix (with potential ongoing work)

# Languages
Python

# Experience Required
Polymarket API, crypto wallets (MetaMask), API auth flows, WebSockets, EIP-712 signing

# Budget
Open (quick fix for an expert)

# Job Description
##
I need an experienced developer who understands Polymarket’s private API authentication to fix a specific issue in my Python bot.
##
My bot is fully functional in paper mode, connects to all WebSocket feeds, and runs strategies correctly.
##
However, when switching to live order execution, I get:

```
REAL_EXEC- Failed to submit BUY order: PolyApiException[status_code=401, error_message='error': 'Unauthorized/Invalid api key'
```

## What I Know So Far
###
The bot is connected — this isn’t a WebSocket issue.
###
The issue happens at the REST order-submit endpoint only.
###
Python 3.14
Custom market-maker logic
EIP-712 signing for CLOB orders
Polymarket Wallet connected through MetaMask
###
I already have my API Key, API Secret, API Passphrase, and private key.

# Your Job
- Identify why the bot’s authenticated POST requests are failing with 401.
- Patch the code to correctly use my API credentials.
- Ensure the bot signs and submits orders successfully in live mode.
- Verify nothing is being overwritten by the credential derivation logic.
- Help me test one successful live order (small size).

# Ideal Candidate
- Has fixed Polymarket API auth before — not someone learning for the first time.
- Understands private-key vs API-key flows.
- Familiar with order-books, maker bots, latency considerations.
- Can read and fix Python quickly.

# What I Will Provide
- Full zipped repository
- `Config.py` with redacted credentials
- Live logs from the bot
- Clear reproduction steps
- Optional: access to a test VPS environment
~~~

## 2.4. Tags
Python
API
API Integration

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Tigard

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Apr 7, 2022
### 5.3.2. Hire rate (%)
44
### 5.3.3. Количество опубликованных проектов (jobs posted)
23
### 5.3.4. Total spent (USD)
13K
### 5.3.5. Количество оплаченных часов в почасовых проектах
39
### 5.3.6. Средняя почасовая ставка (USD)
97.79

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021989025164479965499

### 6.1.2. Title
Need Developer to Integrate Polymarket Live Data Feed (15m & 1h Crypto Up/Down Markets)

### 6.1.3. Description
`P1D` ≔ 
```text
I need an expert developer who understands Polymarket’s live data feeds (RTDS + CLOB WebSocket streams) to help me pull real-time prices, order books, and trades for the 15-minute and 1-hour crypto Up/Down markets (BTC, ETH, SOL, XRP).

This is not a trading bot job.

This is not execution logic.

I only need:

1. How to properly connect to Polymarket’s live feeds

2. Working Python code that successfully streams live data
— from the correct WebSocket endpoints
— for ONLY the 15m & 1h crypto Up/Down markets
— real-time “Up” and “Down” prices
— order book updates
— trades / ticks

The deliverable is simply functional Python WebSocket code that prints real-time updates every time new data arrives.

Requirements

Looking for someone who has experience with at least one of the following:

Polymarket RTDS feeds
Polymarket CLOB websocket feeds
Real-time market data systems (crypto, prediction markets, options)
Python async / websockets libraries
Building live-data bots or dashboards
If you already have working code for Polymarket feeds — even better.
Deliverables
A working Python script that:
Connects to the correct Polymarket WebSocket endpoint
Subscribes to the live crypto markets (15m & 1h)
Streams the following in real-time:
Best bid/ask for Yes/No (Up/Down)
Last traded price
Order book depth
Any other feed data provided by RTDS
Clear instructions on:
How to run it on a VPS
What headers / authentication Polymarket currently requires
How to bypass 403/404 errors people commonly hit
Confirmation the code works on my end.
Additional Info
We’re running paper mode only, not placing orders.
We just need the live data so we can monitor markets programmatically.
I already have:
A Python environment
A VPS
Test scripts
Polymarket API keys (if needed)
Budget
Open to reasonable quotes — fast delivery is a bonus.
This job is extremely simple for someone who’s already familiar with Polymarket’s RTDS.
```

### 6.1.4. Publication Date
last week

### 6.1.5. Payment Terms (USD) 
#### 6.1.5.1. Expected by `ꆜ`  
Hourly
#### 6.1.5.2. Actual
5 hrs @ $60.00/hr

### 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.1.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month


### 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

### 6.2.1. URL
https://www.upwork.com/jobs/~021928532725946340381

### 6.2.3. Title
Options Flow Indicator Development

### 6.2.3. Description
`P2D` ≔ 
```text
Options Flow Indicator Development
Project goal
Develop a Pine Script indicator to track options flow including puts and calls, potentially linked to a flow provider.
Scope of work
- Design a Pine Script indicator that visualizes options flow with settings for filtering by premium and expiration.
- Explore integration options with a flow provider to automatically populate chart data.
- Consider alternative implementation using Python if Pine Script is unfeasible.
Read more
Additional information
- Open to ideas for implementation.
Programming language
Pine Script
```

### 6.2.4. Publication Date
2 quarters ago

### 6.2.5. Payment Terms  (USD) 
#### 6.2.5.1. Expected by `ꆜ`
50-200 Hourly
#### 6.2.5.2. Actual 
3 hrs @ $180.00/hr
Billed: $382.99

### 6.2.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.2.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

### 6.2.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.3. `P3⁎`

### 6.3.1. URL
https://www.upwork.com/jobs/~021953850147847536926

### 6.3.2. Title
Investor Operating Agreement

### 6.3.3. Description
`P3D` ≔ 
```text
I have a business that is receiving a cash investment. In return the investor is receiving a 30% stake in the company. I already have an operating agreement in place with my investor. However, their counsel is wanting some things added/changed in the agreement.
```

### 6.3.4. Publication Date

last quarter

### 6.3.5. Payment Terms (USD) 
#### 6.3.5.1. Expected by `ꆜ`  
Hourly
#### 6.3.5.2. Actual
5 hrs @ $120.00/hr
Billed: $634.99

### 6.3.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.3.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

### 6.3.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.4. `P4⁎`

### 6.4.1. URL
https://www.upwork.com/jobs/~021965437878325647113

### 6.4.2. Title
Arbitrage Sports Betting Bot

### 6.4.3. Description
`P4D` ≔ 
```text
Looking to build an arbitrage sports betting bot to run in sync with Odds Jam, or a similar site.

Arbs don’t last long: 2–15 seconds max.
OddsJam = too slow/manual: by the time you click, the line moved.
Need automation: instant execution across multiple sportsbooks.


Auto-Execution Module
* Browser extension (Chrome/Firefox) or API integration.
* When arb detected → instantly fires both bets.
* Fills bet slips and submits automatically (like OddsJam’s “Bet” button, but for all books).
```

### 6.4.4. Publication Date
2 months ago

### 6.4.5. Payment Terms (USD) 
#### 6.4.5.1. Expected by `ꆜ`  
Hourly
#### 6.4.5.2. Actual
Fixed-price $200.00

### 6.4.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.4.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

### 6.4.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.5. `P5⁎`

### 6.5.1. URL
https://www.upwork.com/jobs/~021965216594002089737

### 6.5.2. Title
Chrome Extension Dev Needed – One-Click Bet Slip Autofill (Sportsbook Automation)

### 6.5.3. Description
`P5D` ≔ 
```text
Project: One-Click Bet Extension (OddsJam Companion)

Build a Chrome/Edge extension that, from the OddsJam arbitrage table, opens target sportsbooks in new tabs and prefills the bet slip (selection + stake) so the user only needs to click “Place Bet.” No auto-betting.

Scope (MVP → Phase 1)
Target books (initial): Pinnacle, Bookmaker, BetUS, BetOnline, Bovada
User flow: Click “Bet+” on an OddsJam row → two sportsbook tabs open (hedge flow optional) → correct market/outcome is selected → bet slip opens with stake prefilled → user confirms.

Technical Requirements
1) Extension Architecture
MV3 extension with:
Background service worker (tabs, scripting, storage).
Content script on oddsjam.com (“listener/overlay”).
Content scripts per sportsbook domain (adapters).
Host permissions: whitelist only the listed sportsbook domains + oddsjam.com.
Hot-config: selectors & URL patterns fetched from a remote JSON so fixes don’t require store resubmission.

2) OddsJam Integration (Non-invasive first)
Listen to clicks on arb rows or inject a small “Bet+” button beside each book.
Extract payload from the row (or a lightweight overlay input):

4) Safety & Compliance
No auto-placing bets. Stop at prefilled slip.
User-initiated only (click/shortcut).
Prominent odds moved / market closed guardrail.
Don’t store credentials, bypass geo/KYC, or use hidden iframes.

5) QA & Tooling
Playwright tests (headful) per adapter:
Navigate → select outcome → slip opens → stake present → odds check UI appears when forced drift.
Feature flag to disable/enable individual adapters from hot-config.
Basic logging panel (extension popup) for debugging last action.

You will see on my screenshot attachment, "1 click bet" some say "site" "bet" and "game" we want all of the sports books I choose to be able to say "bet" which directly opens a new tab with the bet slip loaded.
```

### 6.5.4. Publication Date
2 months ago

### 6.5.5. Payment Terms (USD) 
#### 6.5.5.1. Expected by `ꆜ`  
Hourly
#### 6.5.5.2. Actual
Fixed-price $5,800.00

### 6.5.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.5.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

### 6.5.8. Contractor Location (expected by `ꆜ`)
Not specified

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 8.
## 8.1.
`С⁎` ≔ 
```
Компания `ꆜ`
```

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
when switching to live order execution, I get:

«REAL_EXEC- Failed to submit BUY order: PolyApiException[status_code=401, error_message='error': 'Unauthorized/Invalid api key'»
~~~
```

# 10.
## 10.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Identify why the bot’s authenticated POST requests are failing with 401
~~~
```

# 11. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Research)
https://gemini.google.com/share/5531f1fa94ae


## **1. Введение: Архитектурная парадигма гибридной децентрализации**

В современной экосистеме децентрализованных финансов (DeFi) платформа Polymarket занимает уникальное положение, реализуя гибридную модель биржи, которая объединяет эффективность централизованного мэтчинга ордеров с безопасностью децентрализованных расчетов. Эта архитектура, известная как CLOB (Central Limit Order Book), создает специфический ландшафт для разработчиков и алгоритмических трейдеров. В отличие от традиционных Web2 API, где ошибка 401 Unauthorized обычно указывает на простую неверную пару логин/пароль, в контексте Polymarket этот код ответа служит "зонтичным" индикатором для широкого спектра криптографических, структурных и инфраструктурных аномалий.

Для сущности, обозначенной в запросе как ꆜ, попытка интеграции с Polymarket API превратилась в столкновение с жесткими требованиями криптографической верификации. Проблема не является тривиальной ошибкой доступа; это симптом фундаментального непонимания того, как взаимодействуют Layer 1 (подписи приватным ключом) и Layer 2 (сессионные API ключи) в среде, где каждое действие должно быть математически доказано. В данном отчете мы проведем глубокую деконструкцию всех векторов отказа, приводящих к ошибке 401, опираясь на анализ документации, исходного кода и технических дискуссий разработчиков.

### **1.1 Операционная модель и роль оператора**

Polymarket функционирует на базе гибридно-децентрализованной модели.1 Это означает, что критически важный процесс сопоставления ордеров (matching) происходит вне блокчейна (off-chain). Это решение продиктовано необходимостью обеспечить высокую пропускную способность и отсутствие платы за газ (gas fees) при размещении и отмене ордеров, что невозможно в полностью ончейн-среде. Оператор биржи отвечает за ведение книги ордеров, но не имеет доступа к средствам пользователей.

Фактическое исполнение сделок (settlement) происходит ончейн через специализированный смарт-контракт Exchange Contract.1 Этот контракт обеспечивает атомарные свопы между бинарными токенами исходов (Outcome Tokens, стандарт ERC1155) и залоговыми активами (обычно USDC, стандарт ERC20). Именно здесь кроется корень многих проблем аутентификации: API не просто принимает команду "купить", он принимает *подписанное сообщение*, которое оператор затем передает в смарт-контракт для исполнения. Если подпись, сгенерированная клиентом, не соответствует строгим стандартам, ожидаемым контрактом, API отвергает запрос с кодом 401, защищая целостность системы.1

---

## **2. Криптографическая природа аутентификации и дихотомия уровней (L1 vs L2)**

Одной из наиболее распространенных причин возникновения ошибок авторизации у интеграторов уровня ꆜ является фундаментальная путаница между двумя слоями аутентификации, используемыми в системе Polymarket. Система требует четкого разграничения между доказательством владения аккаунтом (Layer 1) и авторизацией текущей сессии (Layer 2).

### **2.1 Layer 1: Доказательство владения и подписи EIP-712**

Первый уровень аутентификации (L1) — это высшая форма доказательства личности в системе. Она опирается непосредственно на приватный ключ Polygon-аккаунта пользователя.4 В отличие от традиционных систем, где сервер хранит хэш пароля, здесь сервер не знает ничего о приватном ключе пользователя. Аутентификация происходит исключительно через верификацию цифровой подписи.

Этот уровень строго обязателен для действий, требующих наивысших привилегий или изменения состояния безопасности аккаунта. Согласно документации, L1 аутентификация необходима для двух критических операций:

1. **Создание или отзыв API ключей (onboarding):** Сервер должен быть уверен, что запрос на создание сессионного ключа исходит от истинного владельца кошелька.4  
2. **Размещение ордера (подписание тела ордера):** Хотя сам HTTP-запрос на отправку ордера может быть защищен L2-заголовками, *тело* ордера (payload) должно содержать криптографическую подпись параметров сделки.1

Механизм подписи здесь базируется на стандарте **EIP-712** ("Typed Structured Data Hashing and Signing"). Этот стандарт был разработан для того, чтобы пользователи видели, что именно они подписывают, вместо непонятной строки шестнадцатеричных символов.5 Ошибка 401 на этом уровне часто возникает из-за того, что клиент формирует структуру данных, которая байт-в-байт не совпадает с тем, что ожидает сервер. Даже малейшее расхождение в типах данных (например, передача числа как строки) приведет к изменению хэша и невалидности подписи.

### **2.2 Layer 2: Сессионные ключи и HMAC**

Второй уровень (L2) предназначен для высокочастотных операций, таких как чтение приватных данных пользователя, получение истории ордеров или управление открытыми позициями. Для этого используются API ключи, которые криптографически выводятся из подписи L1.4

Комплект учетных данных L2 состоит из трех элементов:

* **API Key (UUID):** Публичный идентификатор ключа.  
* **Secret:** Секретная строка, используемая для генерации HMAC-подписей запросов. Она никогда не передается по сети.  
* **Passphrase:** Парольная фраза, используемая для шифрования/дешифрования секрета.

Ошибка 401 при использовании L2 заголовков чаще всего вызвана неправильной генерацией заголовка POLY_SIGNATURE. В отличие от L1, где используется эллиптическая криптография (ECDSA), в L2 используется **HMAC-SHA256**.4 Клиент должен взять метод запроса, путь, тело запроса и временную метку, и подписать их секретом. Любая ошибка в конкатенации этих строк на стороне клиента приведет к тому, что сервер вычислит другой хэш и отвергнет запрос.

### **Таблица 1: Матрица требований к заголовкам аутентификации**

| Заголовок | Уровень L1 (Приватный ключ) | Уровень L2 (API Ключ) | Описание и критические точки отказа |
| :---- | :---- | :---- | :---- |
| POLY_ADDRESS | Обязательно | Обязательно | Публичный адрес кошелька Polygon. Ошибка здесь — неверный идентификатор пользователя. 4 |
| POLY_SIGNATURE | **ECDSA (EIP-712)** | **HMAC-SHA256** | Главный источник ошибок 401. Тип подписи должен строго соответствовать типу операции. 4 |
| POLY_TIMESTAMP | Обязательно | Обязательно | Текущее время UNIX. Рассинхронизация часов клиента и сервера вызывает отказ. 4 |
| POLY_NONCE | Обязательно (Def: 0) | Не применимо | Используется для защиты от атак повторного воспроизведения (replay attacks) на уровне создания ключей. 4 |
| POLY_API_KEY | Не применимо | Обязательно | UUID ключа. Должен существовать в базе данных для указанного POLY_ADDRESS. 4 |
| POLY_PASSPHRASE | Не применимо | Обязательно | Фраза-пароль. Передается в открытом виде (внутри TLS). 4 |

---

## **3. Проблема сериализации JSON: "Невидимый" враг в Python**

Одним из самых коварных и технически сложных источников ошибок 401 для разработчиков, использующих Python (и в частности библиотеку py-clob-client), является проблема сериализации JSON. Это классический пример того, как высокоуровневые абстракции языков программирования конфликтуют с жесткими требованиями бинарной детерминированности криптографии.

### **3.1 Природа аномалии пробелов**

При формировании L2-подписи (HMAC) клиент должен хэшировать тело запроса. Сервер Polymarket ожидает, что JSON-структура тела запроса будет "плотной" (compact), то есть без пробелов между ключами и значениями (например, {"key":"value"}). Однако стандартная библиотека json в Python по умолчанию при вызове метода json.dumps() добавляет пробелы после разделителей для лучшей читаемости (например, ", ").7

Это создает критическое расхождение.

1. Клиент формирует объект данных (словарь).  
2. Библиотека подписывания (внутри клиента) может сериализовать этот объект в строку *без пробелов* и сгенерировать подпись Sig_Compact.  
3. Библиотека HTTP-запросов (например, requests), получая этот же объект в параметре json=, использует стандартный сериализатор Python, который создает строку *с пробелами* (Body_Spaced).  
4. По сети уходит Body_Spaced и заголовок Sig_Compact.  
5. Сервер получает Body_Spaced, вычисляет его хэш и видит, что он не совпадает с Sig_Compact.  
6. Результат: **401 Unauthorized / Invalid API Key**.9

### **3.2 Техническое подтверждение и анализ кода**

Анализ проблем (issues) в репозитории py-clob-client подтверждает массовый характер этой проблемы. Разработчики отмечают, что "некоторые эндпоинты не принимают (валидный) JSON и возвращают ошибку авторизации".10 В частности, обсуждение в Issue #164 прямо указывает на необходимость патчинга метода request в библиотеке.9

Решение требует принудительного удаления пробелов при сериализации перед отправкой запроса:

Python

## Пример коррекции сериализации для соответствия ожиданиям сервера  
import json

## Неверно (стандартное поведение):  
```
data_str = json.dumps(data) -> '{"price": 0.5, "side": "BUY"}' (с пробелами)
```

## Верно (для Polymarket CLOB):  
```
data_str = json.dumps(data, separators=(',', ':'))   -> '{"price":0.5,"side":"BUY"}'
```

Для ꆜ это означает, что использование стандартных средств отладки может не выявить проблему, так как логи будут показывать "правильный" JSON. Проблема кроется исключительно в байтовом представлении пробельных символов, которые невидимы при стандартном просмотре объектов, но меняют криптографический хэш.

### **3.3 Влияние версии Python**

Дополнительную сложность вносит эволюция самого языка Python. В версии 3.4 и выше поведение json.dumps по умолчанию изменилось, закрепив использование (', ', ': ') в качестве разделителей, если indent не равен None.8 Более того, в последних версиях (включая альфа-версии 3.14) продолжаются оптимизации производительности json.dumps, что может косвенно влиять на порядок ключей в словарях, если он не зафиксирован явно.11 Для детерминированной подписи порядок ключей критичен: {"a":1,"b":2} и {"b":2,"a":1} дадут совершенно разные хэши. Сервер Polymarket, вероятно, нормализует JSON, но полагаться на это рискованно. Лучшая практика — сортировка ключей (sort_keys=True) при подписании и отправке.

---

## **4. Кризис идентичности: EOA против Proxy Wallets**

Следующий класс проблем, приводящих к отказу в обслуживании (401/403), связан с абстракцией учетных записей. Polymarket активно использует концепцию **Proxy Wallets** (часто на базе Gnosis Safe), чтобы обеспечить пользователям возможность торговли без газа (meta-transactions) и атомарного управления позициями.12

### **4.1 Фундаментальное различие типов подписи**

При отправке ордера API требует явного указания параметра signatureType.14 Это поле сообщает смарт-контракту (и оператору), как именно верифицировать предоставленную подпись EIP-712.

* **Type 0 (EOA):** Прямая подпись от внешнего кошелька (например, MetaMask). Средства должны находиться непосредственно на балансе этого адреса, и этот адрес должен дать разрешение (allowance) контракту биржи.  
* **Type 1 (POLY_PROXY):** Подпись от EOA, который *владеет* прокси-кошельком Polymarket. Средства находятся на прокси-контракте. Оператор проверяет, является ли подписант владельцем прокси.  
* **Type 2 (POLY_GNOSIS_SAFE):** Подпись от владельца Gnosis Safe (мультисиг).

Наиболее частая ошибка ꆜ заключается в смешивании контекстов. Пользователь может инициализировать клиент с приватным ключом EOA, но указать signatureType=1 (Proxy), не имея развернутого прокси-кошелька. Или наоборот, пользователь перевел средства на прокси (пополнил баланс в UI), но пытается торговать с signatureType=0, используя пустой EOA-адрес в качестве "funder" (источника средств).15 В этом случае проверка баланса или прав доступа провалится, что система интерпретирует как неавторизованное действие.

### **4.2 Барьер "Enable Trading"**

Термин "Enable Trading" в интерфейсе Polymarket технически означает деплоймент прокси-контракта в блокчейн.17 До тех пор, пока эта транзакция не будет подтверждена сетью Polygon, прокси-адрес де-факто не существует (или не инициализирован).  
Если скрипт ꆜ пытается отправить ордер немедленно после вычисления адреса прокси (counterfactual address), но до фактического майнинга транзакции создания прокси, API вернет ошибку. Это связано с тем, что оператор не может верифицировать права владения несуществующим контрактом. Процесс "Enable Trading" также включает установку бесконечных approve (разрешений) для контракта биржи тратить USDC с прокси-аккаунта.13 Отсутствие этого шага приведет к сбою на этапе проверки обеспечения ордера.

---

## **5. Экологический дрейф: Миграция с Mumbai на Amoy**

Среда разработки на блокчейне Polygon претерпела значительные изменения, которые сделали множество старых туториалов и конфигураций устаревшими. Это создает критический риск конфигурационных ошибок, которые маскируются под ошибки аутентификации.

### **5.1 Депрекация Mumbai и восход Amoy**

Ранее основной тестовой сетью (testnet) для Polygon была Mumbai (Chain ID 80001). Однако, в связи с отключением сети Ethereum Goerli (которая служила L1-слоем для Mumbai), Polygon перевел свою экосистему на новую тестовую сеть — **Amoy** (Chain ID 80002), базирующуюся на Ethereum Sepolia.19

Для ꆜ, использующего устаревшие фрагменты кода или документацию, это создает фатальную проблему. EIP-712 подписи включают параметр chainId в структуру domain для защиты от атак повторного воспроизведения (replay attacks) между сетями.20  
Если разработчик настраивает клиент на использование URL тестовой среды, но оставляет chainId=80001 (Mumbai) или chainId=137 (Mainnet), сервер Amoy при получении запроса попытается восстановить адрес подписанта, используя свой chainId (80002). Из-за несовпадения параметров домена восстановленный адрес будет представлять собой случайный набор байт, который не совпадет с адресом пользователя. Результат — ошибка 401 Unauthorized или "Invalid Signature".21

### **5.2 Конфигурационная матрица**

Чтобы избежать этих ошибок, необходимо строго соблюдать соответствие всех параметров среды. Смешивание параметров (например, использование RPC Amoy с адресами контрактов Mumbai) недопустимо.

### **Таблица 2: Параметры сетевых окружений**

| Параметр | Polygon Mainnet (Prod) | Polygon Amoy (Testnet) | Статус / Примечание |
| :---- | :---- | :---- | :---- |
| **Chain ID** | 137 | 80002 | Критично для EIP-712 Domain Separator. 15 |
| **CLOB Endpoint** | https://clob.polymarket.com/ | *(Требует уточнения в Docs)* | Использование Mainnet URL с тестовыми ключами вызовет 401. 23 |
| **Exchange Contract** | 0x4bFb...82E | 0xdFE0...9E40 | Адреса контрактов различны для каждой сети. 15 |
| **Collateral (USDC)** | 0x2791...174 | 0x41e9...e0C | Токены USDC также имеют разные адреса. 15 |

---

## **6. Глубокий анализ структуры EIP-712 и ошибок формирования ордера**

Помимо проблем с заголовками и сетью, источником ошибки 401 часто является некорректное формирование самой структуры данных Order, которую подписывает пользователь. Смарт-контракт Exchange Contract ожидает строго определенную схему данных.

### **6.1 Структура Order и хеширование типов**

Согласно стандарту EIP-712, данные хешируются с использованием схемы типов (typeHash). Для Polymarket структура ордера включает следующие поля: salt, maker, signer, taker, tokenId, makerAmount, takerAmount, expiration, nonce, feeRateBps, side, signatureType.15

Если ꆜ использует библиотеку, которая неправильно обрабатывает большие числа (например, uint256), хэш будет неверным. В JavaScript и Python числа больше $2^{53}-1$ требуют использования специальных библиотек (BigInt, decimal), иначе происходит потеря точности. Если tokenId (который является огромным числом, кодирующим ID условия и исхода) будет передан как обычное число с плавающей точкой, подпись станет невалидной.

### **6.2 Salt и Nonce: Уникальность и защита от коллизий**

* **Salt (Соль):** Случайное число, обеспечивающее уникальность хэша ордера. Ошибка 401 может возникнуть, если пользователь повторно отправляет ордер с тем же salt, который уже был обработан или отменен, хотя чаще это вызывает логическую ошибку, система может интерпретировать это как попытку replay-атаки.14  
* **Nonce:** В контексте CLOB это не просто счетчик транзакций. Это параметр, используемый для отмены ордеров. Пользователь может отменить все ордера с nonce < X. Если текущий nonce ордера меньше, чем значение, установленное при последней массовой отмене, ордер будет отвергнут.14

### **6.3 Особенности Conditional Tokens Framework (CTF)**

Polymarket использует стандарт CTF (ERC1155). TokenID актива — это не просто порядковый номер. Это хэш, вычисляемый на основе conditionId (ID вопроса) и indexSet (битовой маски исхода, например, YES или NO).  
Если ꆜ пытается вычислить tokenId вручную и ошибается в алгоритме хеширования (например, использует неверную версию keccak или неправильный порядок байт), он подпишет ордер для несуществующего актива. Оператор, проверяя подпись, увидит, что пользователь подписал намерение купить "Актив Х", в то время как в параметрах запроса указан "Актив Y" (или наоборот). Это несоответствие также приведет к ошибке валидации подписи.

---

## **7. Стратегии отладки и рекомендации по устранению**

На основе проведенного анализа, для ꆜ предлагается следующий алгоритм действий по устранению ошибок 401 и стабилизации интеграции.

### **7.1 Аудит кода сериализации**

Необходимо внедрить жесткий контроль над преобразованием JSON. Рекомендуется создать обертку над методом отправки запросов, которая гарантирует отсутствие пробелов.

* **Для Python:** Использовать json.dumps(payload, separators=(',', ':')).  
* **Для JavaScript/TypeScript:** JSON.stringify() обычно работает корректно (без пробелов), но стоит убедиться, что не используются "красивые" принтеры (pretty printers) на этапе формирования подписи.

### **7.2 Верификация параметров сети**

Следует жестко зафиксировать конфигурацию для среды.

* Если цель — **Production**: Chain ID = 137, Endpoint = https://clob.polymarket.com/.  
* Если цель — **Testing**: Chain ID = 80002 (Amoy), Endpoint и контракты должны быть взяты из актуальной документации разработчика для Amoy. Использование старых конфигов Mumbai недопустимо.

### **7.3 Синхронизация времени**

Убедиться, что системное время на сервере, запускающем бота, синхронизировано через NTP. Допустимое окно отклонения POLY_TIMESTAMP обычно составляет не более нескольких секунд. Если часы отстают или спешат, даже идеально подписанный запрос будет отвергнут.4

### **7.4 Проверка статуса Proxy Wallet**

Перед началом торговли необходимо программно проверить статус прокси-кошелька.

1. Вычислить адрес прокси для данного EOA.  
2. Проверить код контракта по этому адресу в блокчейне (getCode). Если код пуст (0x), значит прокси еще не развернут.  
3. В этом случае необходимо выполнить процедуру "Enable Trading" и *дождаться подтверждения транзакции*. Только после этого можно использовать signatureType=1.

### **7.5 Использование официальных SDK с осторожностью**

Хотя Polymarket предоставляет клиенты на Python и TypeScript, анализ показал, что они могут содержать баги (как в случае с пробелами в JSON). Рекомендуется фиксировать версии библиотек (pinning dependencies) и внимательно следить за Issues в репозиториях GitHub.9 Если возможно, стоит рассмотреть вариант реализации собственной логики подписания на базе надежных криптографических примитивов (web3.py, ethers.js), чтобы иметь полный контроль над процессом формирования байт-кода подписи.

## **8. Заключение**

Проблема 401 Unauthorized в API Polymarket CLOB является сложным феноменом, выходящим за рамки простых ошибок доступа. Это индикатор нарушения целостности данных в распределенной криптографической системе. Для ꆜ решение лежит не в переборе API-ключей, а в обеспечении байтовой точности на всех этапах: от сериализации JSON и выбора Chain ID до понимания архитектуры прокси-контрактов. Успешная интеграция требует перехода от мышления веб-разработчика к мышлению криптографического инженера, где каждый бит имеет значение, а доверие строится на математических доказательствах, а не на сессионных куки.

---

**Примечание:** Все утверждения в данном отчете подкреплены ссылками на техническую документацию, исходный код и дискуссии сообщества разработчиков Polymarket, представленные в исследовательских фрагментах. Идентификаторы источников интегрированы в текст для обеспечения проверяемости выводов.

#### **Works cited**

1. CLOB Introduction - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/CLOB/introduction](https://docs.polymarket.com/developers/CLOB/introduction)  
2. How Polymarket Works | The Tech Behind Prediction Markets, accessed November 21, 2025, [https://rocknblock.io/blog/how-polymarket-works-the-tech-behind-prediction-markets](https://rocknblock.io/blog/how-polymarket-works-the-tech-behind-prediction-markets)  
3. iPaulPro/PolymarketAttestActionModule: An Open Action for embeding Polymarket trading within Lens Protocol Publications - GitHub, accessed November 21, 2025, [https://github.com/iPaulPro/PolymarketAttestActionModule](https://github.com/iPaulPro/PolymarketAttestActionModule)  
4. Authentication - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/CLOB/authentication](https://docs.polymarket.com/developers/CLOB/authentication)  
5. Build Smarter, Safer Wallet Interactions with EIP-712 (Code Inside!) - Medium, accessed November 21, 2025, [https://medium.com/@ancilartech/build-smarter-safer-wallet-interactions-with-eip-712-code-inside-c963686a46cf](https://medium.com/@ancilartech/build-smarter-safer-wallet-interactions-with-eip-712-code-inside-c963686a46cf)  
6. @dicedhq/polymarket - JSR, accessed November 21, 2025, [https://jsr.io/@dicedhq/polymarket](https://jsr.io/@dicedhq/polymarket)  
7. How to Read and Write JSON Files in Python - Vertabelo Academy, accessed November 21, 2025, [https://academy.vertabelo.com/course/python-json/writing-json-files/writing-to-json-file/jsondumps-options-2](https://academy.vertabelo.com/course/python-json/writing-json-files/writing-to-json-file/jsondumps-options-2)  
8. json — JSON encoder and decoder — Python 3.14.0 documentation, accessed November 21, 2025, [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)  
9. Some endpoints don't accept (valid) JSON that doesn't have extra spaces, and will instead return {"error":"Unauthorized/Invalid api key"} · Issue #164 · Polymarket/py-clob-client - GitHub, accessed November 21, 2025, [https://github.com/Polymarket/py-clob-client/issues/164](https://github.com/Polymarket/py-clob-client/issues/164)  
10. Issues · Polymarket/py-clob-client - GitHub, accessed November 21, 2025, [https://github.com/Polymarket/py-clob-client/issues](https://github.com/Polymarket/py-clob-client/issues)  
11. Changelog — Python 3.14.0 documentation, accessed November 21, 2025, [https://docs.python.org/3/whatsnew/changelog.html](https://docs.python.org/3/whatsnew/changelog.html)  
12. Proxy wallet - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/proxy-wallet](https://docs.polymarket.com/developers/proxy-wallet)  
13. Connecting to Polymarket, accessed November 21, 2025, [https://legacy-docs.polymarket.com/faq/connecting-to-polymarket](https://legacy-docs.polymarket.com/faq/connecting-to-polymarket)  
14. Orders Overview - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/CLOB/orders/orders](https://docs.polymarket.com/developers/CLOB/orders/orders)  
15. Polymarket order signing in Clojure - GitHub Gist, accessed November 21, 2025, [https://gist.github.com/shaunlebron/7463f0003aa906ffe6f31dc18c408f73](https://gist.github.com/shaunlebron/7463f0003aa906ffe6f31dc18c408f73)  
16. quantpylib.wrappers.polymarket, accessed November 21, 2025, [https://quantpylib.hangukquant.com/wrappers/polymarket/](https://quantpylib.hangukquant.com/wrappers/polymarket/)  
17. MetaMask | Polymarket, accessed November 21, 2025, [https://legacy-docs.polymarket.com/getting-started/connecting/metamask](https://legacy-docs.polymarket.com/getting-started/connecting/metamask)  
18. Relayer Client - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/builders/relayer-client](https://docs.polymarket.com/developers/builders/relayer-client)  
19. Introducing the Amoy Testnet for Polygon PoS, accessed November 21, 2025, [https://polygon.technology/blog/introducing-the-amoy-testnet-for-polygon-pos](https://polygon.technology/blog/introducing-the-amoy-testnet-for-polygon-pos)  
20. Polymarket/poly-py-eip712-structs: EIP712 data structure management for python - GitHub, accessed November 21, 2025, [https://github.com/Polymarket/poly-py-eip712-structs](https://github.com/Polymarket/poly-py-eip712-structs)  
21. Web3.py Error: Failed to Sign Typed Data, Invalid Domain Key ClobAuth for EIP-712 in Polymarket - Stack Overflow, accessed November 21, 2025, [https://stackoverflow.com/questions/79072329/web3-py-error-failed-to-sign-typed-data-invalid-domain-key-clobauth-for-eip-71](https://stackoverflow.com/questions/79072329/web3-py-error-failed-to-sign-typed-data-invalid-domain-key-clobauth-for-eip-71)  
22. Invalid signature when creating orders in negative risk market · Issue #79 · Polymarket/py-clob-client - GitHub, accessed November 21, 2025, [https://github.com/Polymarket/py-clob-client/issues/79](https://github.com/Polymarket/py-clob-client/issues/79)  
23. Endpoints - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/CLOB/endpoints](https://docs.polymarket.com/developers/CLOB/endpoints) 

# 12. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Think)
https://gemini.google.com/share/f86af4fbbcef
https://gemini.google.com/share/f86af4fbbcef

## 1. Выявленные проблемы, беспокоящие `ꆜ`

Основная проблема клиента (`P†`) определена в `O.md` (§9) и детально описана в `PD` (`O.md` §2.3).

### 1.1. Основная техническая проблема (`P†`): Ошибка аутентификации (401) при отправке боевых ордеров

Клиент разработал Python-бота для маркет-мейкинга на Polymarket. Бот успешно функционирует в тестовом режиме (paper mode), но при переключении на исполнение реальных ордеров (live order execution) возникает критическая ошибка.

**Симптом:** При попытке отправить ордер через REST API бот получает ответ:

```
REAL_EXEC- Failed to submit BUY order: PolyApiException[status_code=401, error_message='error': 'Unauthorized/Invalid api key'
```

**Контекст:**

  * Ошибка возникает только на эндпоинте отправки ордера (REST order-submit endpoint).
  * WebSocket-соединения и получение данных работают корректно.
  * Клиент обладает всеми необходимыми учётными данными (API Key, API Secret, API Passphrase, private key).
  * Бот использует подписание EIP-712 для ордеров CLOB (Central Limit Order Book) и подключён через MetaMask.

### 1.2. Сопутствующие опасения и неопределённости

Исходя из `PD`, клиент также обеспокоен следующими аспектами:

1.  **Корректность использования учётных данных:** Неопределённость в том, правильно ли бот применяет имеющиеся ключи для аутентификации POST-запросов.
2.  **Логика деривации ключей:** Опасение, что логика получения (деривации) учётных данных может некорректно перезаписывать или использовать ключи («Verify nothing is being overwritten by the credential derivation logic»).
3.  **Различия в потоках аутентификации:** Необходимость чёткого понимания разницы между аутентификацией на основе приватного ключа и API-ключей в контексте Polymarket.

## 2. Анализ обоснованности проблем

Проблема `P†` является полностью обоснованной и критичной для функционирования бота. Код состояния HTTP 401 (Unauthorized) указывает на то, что запрос не был принят из-за недействительных учётных данных аутентификации.

Анализ сложности аутентификации Polymarket API подтверждает, что существует множество потенциальных точек отказа при переходе из тестового режима в боевой.

### 2.1. Двухуровневая аутентификация Polymarket CLOB

Для понимания проблемы критически важно разобрать модель аутентификации Polymarket CLOB, которая состоит из двух уровней (L1 и L2).

#### 2.1.1. L1: Аутентификация приватным ключом (EIP-712)

Этот уровень использует приватный ключ кошелька Polygon для подписания структурированных данных ордера в соответствии со стандартом EIP-712. Это криптографически подтверждает намерение владельца средств совершить сделку. L1 также используется для генерации ключей L2.

#### 2.1.2. L2: Аутентификация API-ключом (HMAC)

Этот уровень использует API Key, Secret и Passphrase для аутентификации самого HTTP-запроса к серверу CLOB. Он подтверждает право пользователя отправлять команды API. Реализуется через генерацию HMAC-подписи запроса.

#### 2.1.3. Интерпретация ошибки

Сообщение `'Unauthorized/Invalid api key'` и код 401 указывают на сбой именно на уровне **L2**. Сервер отклоняет запрос до того, как приступает к валидации ордера (L1), потому что не может верифицировать подпись самого запроса (L2).

### 2.2. Вероятные причины возникновения ошибки 401 (`T1⁎`)

Анализ документации и публичных репозиториев выявил несколько высоковероятных причин сбоя L2-аутентификации в Python-боте.

#### 2.2.1. Критическая проблема: Форматирование (сериализация) JSON

Наиболее вероятной причиной является специфическое требование бэкенда Polymarket к формату JSON при расчёте HMAC-подписи (L2). HMAC-подпись генерируется на основе точного строкового представления тела запроса. Если строка, подписанная клиентом, отличается от строки, которую ожидает сервер (даже на один пробел), подписи не совпадут.

В официальном репозитории Python-клиента (`Polymarket/py-clob-client`) зафиксирована проблема (Issue #164), точно соответствующая симптомам клиента:

> "Some endpoints don't accept (valid) JSON that doesn't have extra spaces, and will instead return `{"error":"Unauthorized/Invalid api key"}`"

Стандартные библиотеки Python могут сериализовать JSON с пробелами для читаемости (например, `{"key": "value"}`). Если сервер Polymarket ожидает компактный формат (например, `{"key":"value"}`) и рассчитывает HMAC на его основе, а клиент отправляет форматированный JSON, возникнет ошибка 401.

**Обоснованность:** Высокая. Это подтверждённая проблема, специфичная для Python-реализации и API Polymarket.

#### 2.2.2. Некорректная генерация HMAC-подписи (L2)

Если бот реализует логику подписания вручную или использует устаревшую версию библиотеки, ошибка может быть в самом алгоритме генерации HMAC. Это включает:

  * Неправильный порядок конкатенации элементов для подписи (Timestamp, Method, Request Path, Body).
  * Использование неверного API Secret.

**Обоснованность:** Средняя. Стандартные библиотеки обычно реализуют это корректно, но ошибки в интеграции возможны.

#### 2.2.3. Ошибки в логике деривации или использования ключей

Клиент явно указал на необходимость проверки логики деривации. Если бот использует ключи от тестовой среды в боевой, или если логика деривации L2-ключей из L1-подписи содержит ошибки (например, используется неверный nonce или приватный ключ), это приведёт к использованию недействительных L2-ключей.

**Обоснованность:** Средняя. Это обоснованное опасение, учитывая явное упоминание этой логики клиентом.

#### 2.2.4. Рассинхронизация времени

Аутентификация L2 включает временную метку (`POLY_TIMESTAMP`). Если часы на сервере бота значительно отличаются от времени сервера Polymarket, запрос будет отклонён как просроченный. Это распространённая проблема в API криптобирж.

**Обоснованность:** Низкая, но возможная. Требует проверки синхронизации времени на VPS клиента.

## Заключение

Проблемы клиента (`ꆜ`) обоснованы и связаны со сложностями и неочевидными требованиями аутентификации Polymarket API при переходе в режим реальной торговли. Ошибка 401 указывает на сбой L2-аутентификации.

Наиболее вероятной причиной является специфическая проблема с форматированием JSON-тел запросов (Issue #164 в `py-clob-client`), что приводит к неверному расчёту HMAC-подписи. Другие возможные причины включают ошибки в логике генерации HMAC или некорректное управление/деривацию API-ключей.

# 13.
## 13.1.
`Cᛘ⠿` ≔ ⠿~ (Возможные причины `P†`)

## 13.2.
`Cᛘᵢ` : `Cᛘ⠿`

## 13.3.
? `Cᛘᵢ`

## 13.4.
`Pⰳ(Cᛘᵢ)` ≔ (Правдоподобность гипотезы `Cᛘᵢ`)

# 14. Анализ `Cᛘ⠿` (выполнен Gemini Deep Think) 
https://gemini.google.com/share/187c5a087597


## Cᛘ₁: Некорректная сериализация JSON (Аномалия пробелов)

### Суть
Сервер Polymarket требует, чтобы тело JSON-запроса было сериализовано в компактном формате (без пробелов между ключами и значениями) для верификации HMAC-подписи (L2).
Стандартная библиотека `json` в Python по умолчанию добавляет пробелы при сериализации (например, `{"key": "value"}` вместо `{"key":"value"}`).
Если байтовое представление тела запроса, отправленного по сети, отличается от того, которое было использовано для генерации подписи, сервер отвергает запрос с кодом 401.

### Оценка
95

### Доводы за
Клиент использует Python (`O.md` §2.3), язык, в котором стандартное поведение `json.dumps()` приводит к этой аномалии (`O.md` §11.3.1).
Эта проблема официально задокументирована в репозитории `Polymarket/py-clob-client` (Issue #164) как причина ошибки `{"error":"Unauthorized/Invalid api key"}` (`O.md` §11.3.2, §12.2.1).
Симптомы `P†` точно соответствуют этой известной проблеме взаимодействия Python и Polymarket API.
Анализ в `O.md` §11.3 определяет это как «коварный» и «технически сложный» источник ошибок 401.

### Доводы против
Возможно, клиент уже использует пропатченную версию библиотеки или корректно обрабатывает сериализацию вручную, используя `json.dumps(data, separators=(',', ':'))`.

## Cᛘ₂: Ошибки в управлении или деривации учетных данных

### Суть
Бот некорректно использует или получает (деривирует) ключи L2 (API Key, Secret, Passphrase) при работе в боевой среде.
Это может включать использование ключей от тестовой среды (Testnet/paper mode) в боевой (Mainnet), ошибки в логике получения L2-ключей из L1-подписи, или использование неверного API Secret.
Использование неверных учетных данных приводит к генерации невалидной HMAC-подписи или попытке доступа с недействительным API Key.

### Оценка
75

### Доводы за
Проблема `P†` возникла именно при переключении с paper mode на live execution (`O.md` §2.3), что часто связано со сменой учетных данных.
Клиент явно выразил обеспокоенность по поводу корректности этой части кода: «Verify nothing is being overwritten by the credential derivation logic» (`O.md` §2.3, §12.1.2).
Если используется неверный API Secret для генерации HMAC, ошибка 401 «Invalid api key» является ожидаемым результатом.

### Доводы против
Клиент утверждает, что у него уже есть все необходимые ключи (`O.md` §2.3), предполагая, что он уверен в их корректности.

## Cᛘ₃: Некорректная реализация генерации HMAC-подписи (Исключая Cᛘ₁)

### Суть
Алгоритм генерации заголовка `POLY_SIGNATURE` (HMAC-SHA256) в коде бота реализован с ошибками, не связанными с сериализацией JSON.
Это включает неправильный порядок конкатенации элементов, используемых для подписи: временной метки (Timestamp), метода запроса (Method), пути запроса (Request Path) и тела запроса (Body).
Также это может включать некорректное кодирование данных или API Secret перед хэшированием.

### Оценка
50

### Доводы за
Генерация HMAC требует точного следования спецификации API (`O.md` §11.2.2).
Любая ошибка в порядке параметров или кодировке приведет к невалидной подписи (`O.md` §12.2.2).
Если `ꆜ` реализует логику подписания вручную, а не использует стандартный SDK, вероятность такой ошибки возрастает.

### Доводы против
Если используется официальный SDK (`py-clob-client`), базовая логика HMAC, как правило, реализована корректно (за исключением специфического бага Cᛘ₁).

## Cᛘ₄: Рассинхронизация системного времени (Clock Skew)

### Суть
Системное время на сервере (VPS), где запущен бот, значительно отличается (отстает или спешит) от времени сервера Polymarket.
Заголовок `POLY_TIMESTAMP` используется в L2-аутентификации для защиты от атак повторного воспроизведения.
Если временная метка выходит за допустимое окно (обычно несколько секунд), сервер отклоняет запрос как просроченный (`O.md` §11.7.3).

### Оценка
30

### Доводы за
Это распространенная проблема при интеграции с финансовыми и криптовалютными API (`O.md` §12.2.4).
Конфигурация синхронизации времени (NTP) на сервере клиента может быть некорректной.

### Доводы против
Современные серверные среды обычно имеют адекватную синхронизацию времени по умолчанию.
Часто API возвращают более специфическое сообщение об ошибке (например, «Timestamp Expired»), а не общее «Invalid api key».

## Cᛘ₅: Несоответствие конфигурации среды (Endpoint/Chain ID Mismatch)

### Суть
Бот использует несовместимые параметры конфигурации для боевой среды.
Это может включать отправку запросов на неверный URL (например, использование Testnet эндпоинта вместо Mainnet) или использование неверного идентификатора сети (Chain ID) при подписании.
Использование URL одной среды с ключами или параметрами другой среды приведет к сбоям аутентификации (`O.md` §11.5.2).

### Оценка
25

### Доводы за
Ошибки конфигурации часто возникают при переходе между тестовой и боевой средами.
Недавняя миграция тестовой сети Polygon с Mumbai на Amoy увеличивает вероятность использования устаревших параметров (`O.md` §11.5.1).
Использование неверного эндпоинта (URL) приведет к ошибке 401, если ключи не существуют в этой среде.

### Доводы против
Бот успешно подключается к WebSocket-каналам (`O.md` §2.3), что предполагает, что базовый URL, вероятно, верен.
Неверный Chain ID влияет на L1 (EIP-712), и хотя он может вызвать отказ в авторизации, он реже проявляется как ошибка «Invalid api key» (L2).

## Cᛘ₆: Ошибки в подписании ордера EIP-712 (L1)

### Суть
Бот некорректно формирует или подписывает структурированные данные ордера в соответствии со стандартом EIP-712 (L1-аутентификация).
Это может включать ошибки в типах данных, неправильную обработку больших чисел (uint256) в Python, неверное вычисление `tokenId`, или использование некорректных `salt` или `nonce` (`O.md` §11.6).

### Оценка
10

### Доводы за
Стандарт EIP-712 сложен в реализации и требует байтовой точности (`O.md` §11.2.1).
В Python могут возникать проблемы с точностью при работе с большими числами, используемыми в криптографии (`O.md` §11.6.1).
`O.md` §11.1 указывает, что код 401 может служить "зонтичным" индикатором для широкого спектра криптографических аномалий.

### Доводы против
Сообщение об ошибке `Unauthorized/Invalid api key` строго указывает на сбой L2-аутентификации (доступ к API), а не L1 (валидация ордера) (`O.md` §12.2.1.3).
Сбой L1 обычно происходит после успешной аутентификации L2 и возвращает ошибки типа "Invalid Signature".

## Cᛘ₇: Проблемы со статусом кошелька (EOA vs Proxy Wallet)

### Суть
Клиент неправильно настроил взаимодействие с кошельком для боевой торговли.
Это может включать неверное указание параметра `signatureType` (Type 0 EOA vs Type 1 Proxy) (`O.md` §11.4.1).
Также возможно, что Proxy Wallet не был активирован в блокчейне (не выполнен "Enable Trading"), что делает невозможным торговлю через него (`O.md` §11.4.2).

### Оценка
5

### Доводы за
Архитектура Proxy Wallets на Polymarket нетривиальна и часто вызывает путаницу (`O.md` §11.4).
Это обязательный шаг при переходе к реальной торговле, который может быть пропущен.

### Доводы против
Эти ошибки относятся к логике исполнения ордера и валидации L1/баланса.
Они маловероятно проявятся как ошибка L2 «Invalid api key», которая возникает до проверки статуса кошелька.

## Вердикт

Анализ показывает, что проблема `P†` (ошибка 401 Unauthorized) почти наверняка вызвана сбоем на уровне L2-аутентификации (HMAC-подпись HTTP-запроса).
Сообщение «Invalid api key» указывает на то, что сервер не смог верифицировать запрос, используя предоставленные API-ключи и подпись.

Наиболее вероятной причиной является **Cᛘ₁: Некорректная сериализация JSON (P=95)**.
Существует подтвержденная проблема в экосистеме Python/Polymarket, когда стандартная сериализация JSON с пробелами приводит к несовпадению HMAC-подписей.
Это точно соответствует описанным симптомам и используемому стеку технологий.

Второй по вероятности причиной является **Cᛘ₂: Ошибки в управлении или деривации учетных данных (P=75)**.
Поскольку проблема возникает при переходе в боевой режим, существует высокая вероятность, что бот использует неверный набор ключей (например, неправильный API Secret) или некорректно их обрабатывает.

Гипотезы, связанные с L1-аутентификацией (Cᛘ₆, Cᛘ₇), крайне маловероятны, так как ошибка возникает до этапа валидации ордера.

# 15. Анализ `Cᛘ⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/09e2179ffc85


## **1. Введение**

В современной архитектуре децентрализованных финансов (DeFi) гибридные модели бирж, такие как Polymarket, представляют собой уникальный синтез централизованных книг ордеров (Central Limit Order Books — CLOB) и децентрализованных расчетов (on-chain settlement). Эта двойственная природа создает беспрецедентные вызовы для интеграции автоматизированных торговых систем. В то время как традиционные финансовые API опираются на устоявшиеся стандарты REST и статические ключи API, гибридные системы требуют от разработчика навигации в сложном пространстве криптографических примитивов, стандартов EIP (Ethereum Improvement Proposals) и специфических требований к сериализации данных.

Настоящий отчет посвящен детальному анализу критического сбоя аутентификации, обозначенного как инцидент P†, при котором автоматизированная торговая система, разработанная на языке Python, теряет способность размещать ордера при переходе из тестового режима (Paper Mode) в режим реального исполнения (Live Execution). Симптоматика инцидента — получение HTTP-ответа 401 Unauthorized с сообщением Invalid api key при отправке POST-запросов — является классическим, но многогранным индикатором разрыва между транспортным уровнем (L2) и уровнем подписи данных (L1).

Цель данного документа — предоставить исчерпывающую техническую деконструкцию механизмов безопасности Polymarket, выявить корневую причину отказа и предложить верифицированную стратегию устранения. Анализ выходит за рамки поверхностной отладки, затрагивая фундаментальные вопросы детерминированной сериализации JSON в Python, управления криптографическими контекстами (Chain ID) и жизненного цикла прокси-контрактов в сети Polygon. Мы исследуем, как микроскопические отклонения в байтовом представлении данных могут привести к каскадному отказу систем безопасности, предназначенных для защиты активов пользователей.

## **2. Архитектурная парадигма Polymarket: L1 и L2 Аутентификация**

Для понимания природы ошибки 401 необходимо сначала разобрать многослойную модель безопасности, которую использует Polymarket. В отличие от большинства Web2 сервисов, где сессия определяется одним токеном, Polymarket реализует разделение ответственности между доказательством владения средствами и правом на передачу команд.

### **2.1. Дихотомия слоев безопасности**

Система функционирует на базе двух независимых, но взаимосвязанных слоев аутентификации. Понимание различий между ними критично для диагностики, так как разные слои генерируют разные классы ошибок при сбоях.

| Характеристика | Layer 1 (L1): Владение | Layer 2 (L2): Транспорт |
| :---- | :---- | :---- |
| **Цель** | Криптографическое доказательство намерения владельца кошелька совершить сделку. | Авторизация конкретного HTTP-запроса к шлюзу API. Защита от DDoS и спама. |
| **Механизм** | Цифровая подпись ECDSA (secp256k1) согласно стандарту EIP-712. | Вычисление HMAC-SHA256 от параметров запроса (метод, путь, тело, время). |
| **Ключи** | Приватный ключ Ethereum-кошелька (EOA) или подпись EIP-1271 (Smart Contract Wallet). | Сессионная пара API Key (UUID) и API Secret, деривируемая из L1 подписи. |
| **Место в запросе** | Внутри JSON-тела ордера (поле signature). | В HTTP-заголовках (POLY_SIGNATURE, POLY_API_KEY). |
| **Тип ошибки при сбое** | 400 Bad Request, Invalid Order Signature. Сервер принял запрос, но отверг данные. | 401 Unauthorized, Invalid api key. Сервер отверг запрос на шлюзе. |

Критический вывод из этой архитектуры заключается в следующем: наблюдаемая ошибка 401 однозначно указывает на сбой в **Layer 2**. Это означает, что сервер Polymarket (или его шлюз безопасности, вероятно Cloudflare или внутренний Nginx) отклоняет входящий пакет *до* того, как он попадает в матчинговый движок. Следовательно, содержимое самого ордера (цена, тикер, L1-подпись) еще даже не проверялось. Проблема лежит исключительно в том, как бот формирует «обертку» запроса — HTTP-заголовки и, что наиболее важно, как он подписывает тело этого запроса для транспорта.

### **2.2. Механика деривации ключей (API Key Derivation)**

Процесс получения ключей L2 в Polymarket также нетривиален и является потенциальным вектором ошибки. Ключи не создаются в веб-интерфейсе. Они генерируются программно. Клиент подписывает специальное сообщение («This message attests that I control...») своим приватным ключом (L1). Эта подпись отправляется на сервер, который использует ее как семя (seed) для генерации пары API Key и API Secret. 1

Если клиент и сервер используют разные параметры при этой процедуре (например, разные Nonce или Timestamp), они придут к разным результатам. Однако, поскольку разработчик ꆜ утверждает, что WebSocket работает исправно, мы можем с высокой долей уверенности утверждать, что сама пара ключей валидна. WebSocket использует те же ключи для аутентификации при подписке на приватные каналы. Если бы ключи были «битыми» глобально, бот не смог бы получать данные о балансе. Это наблюдение позволяет нам исключить гипотезу о полной невалидности ключей и сосредоточиться на специфике использования этих ключей в REST POST-запросах.

## **3. Феноменология ошибки: POST против GET и WebSocket**

Различие в поведении между методами HTTP и протоколами передачи данных служит «розеттским камнем» для расшифровки инцидента.

1. **WebSocket:** Работает. Аутентификация происходит один раз при установке соединения (handshake) или подписке на канал. Сообщение подписки обычно короткое и имеет жесткую структуру.  
2. **GET-запросы:** Вероятно, работают (бот «fully functional in paper mode»). В GET-запросах нет тела сообщения (body). Подпись HMAC рассчитывается только от timestamp + method + path. В этой формуле практически нет места для вариативности.  
3. **POST-запросы (Send Order):** Не работают (401). Здесь в формулу расчета HMAC добавляется body — JSON-строка с параметрами ордера.

Именно здесь кроется фундаментальная уязвимость. Функция HMAC чувствительна к любому изменению входных данных. Строка {"side":"BUY"} и строка {"side": "BUY"} (с пробелом) — это две совершенно разные строки с точки зрения криптографии, дающие абсолютно разные хэши. Если клиент подписывает компактную версию, а отправляет версию с пробелами (или наоборот), сервер, получив запрос, пересчитает хэш от *полученной* версии и обнаружит несовпадение.

## **4. Глубинный анализ гипотез причинности (Cᛘ⠿)**

В ходе исследования («Deep Research») мы выделили и проанализировали четыре основные гипотезы, объясняющие поведение системы. Каждая гипотеза была оценена на основе документации, анализа кода библиотек и прецедентов в сообществе разработчиков.

### **4.1. Гипотеза Cᛘ1: Нарушение канонической сериализации JSON (Whitespace Anomaly)**

Это наиболее вероятная и технически обоснованная причина сбоя. Она коренится в реализации стандарта JSON в экосистеме Python.

#### **4.1.1. Техническая суть проблемы**

Стандартная библиотека json в Python при вызове метода json.dumps() по умолчанию использует так называемую «pretty-like» сериализацию, добавляя пробелы после разделителей для улучшения читаемости человеком. Дефолтные разделители в Python: separators=(', ', ': '). Это означает, что объект {'a': 1} превращается в строку '{"a": 1}' (с пробелом после двоеточия).

Однако, высокопроизводительные API, такие как Polymarket CLOB, часто требуют (или подразумевают) «каноническую» или «компактную» форму JSON для расчета подписей, чтобы минимизировать трафик и исключить неоднозначность. Компактная форма не содержит пробелов: '{"a":1}'.

Библиотека requests, которую использует подавляющее большинство Python-ботов, при передаче словаря в параметр json= неявно вызывает json.dumps() с настройками по умолчанию. Таким образом, по сети улетает «разреженный» JSON.

Если логика подписания внутри бота (или используемой им библиотеки py-clob-client) принудительно удаляет пробелы перед хэшированием (что является стандартом для крипто-подписей), возникает фатальная рассинхронизация:

* **Client Sign:** Hmac(Secret, Timestamp + POST + /order + {"price":10})  
* **Network Payload:** {"price": 10}  
* **Server Verify:** Hmac(Secret, Timestamp + POST + /order + {"price": 10})

Хэши не сойдутся. Сервер вернет 401 Unauthorized, так как подпись не соответствует переданному телу.

#### **4.1.2. Доказательная база**

Анализ репозитория py-clob-client выявил Issue #164 2, где разработчики прямо описывают эту проблему: «Some endpoints don't accept (valid) JSON that doesn't have extra spaces, and will instead return {"error":"Unauthorized/Invalid api key"}». Это прямое подтверждение того, что бэкенд Polymarket чувствителен к пробелам.

Более того, это объясняет, почему ошибка возникает только на POST-запросах (где есть тело) и не затрагивает GET/WebSocket.

#### **4.1.3. Оценка вероятности**

**98/100**. Совокупность фактов (Python, POST-only fail, 401 error, подтвержденный issue) делает эту гипотезу практически достоверной.

---

### **4.2. Гипотеза Cᛘ2: Конфликт сетевых идентификаторов (Chain ID Mismatch)**

Вторая по значимости гипотеза связана с конфигурацией среды исполнения, особенно в свете недавних изменений в экосистеме Polygon.

#### **4.2.1. Техническая суть проблемы**

Polymarket работает на блокчейне Polygon. Взаимодействие с биржей требует указания Chain ID — уникального идентификатора сети.

* **Polygon Mainnet (Live):** 137  
* **Polygon Mumbai (Testnet - Deprecated):** 80001  
* **Polygon Amoy (Testnet - Active):** 80002

При переходе из режима разработки (где мог использоваться локальный форк или тестнет) в боевой режим, разработчик мог забыть сменить Chain ID в конфигурации.

Если Chain ID используется при деривации L2-ключей (как «соль» или часть подписанного сообщения), то ключи, сгенерированные для Chain ID 80002, будут математически отличаться от ключей для Chain ID 137. Если бот стучится в боевой API (clob.polymarket.com) с ключами, выведенными для тестнета, сервер просто не найдет этот Key UUID в своей базе данных (или подпись не сойдется), что приведет к ошибке 401.

#### **4.2.2. Доказательная база**

Документация 1 подчеркивает важность правильного Chain ID для формирования домена EIP-712. Однако, ꆜ утверждает, что WebSocket работает. Обычно L2-ключи едины для среды. Если бы Chain ID был неверен глобально, аутентификация WebSocket тоже упала бы.

Тем не менее, возможен сценарий «смешанной конфигурации», где для WS используется один конфиг, а для REST-клиента — другой (захардкоженный).

#### **4.2.3. Оценка вероятности**

**20/100**. Гипотеза сильная, но противоречит факту работающего WebSocket, если предположить, что конфигурация едина.

---

### **4.3. Гипотеза Cᛘ3: Отсутствие активации Proxy Wallet («Enable Trading»)**

#### **4.3.1. Техническая суть проблемы**

Polymarket использует концепцию Proxy Wallet (обычно на базе Gnosis Safe или релейного контракта) для атомарного исполнения сделок. Перед началом торговли пользователь должен выполнить транзакцию «Enable Trading» (Proxy Deployment) в блокчейне.

Если пользователь пытается отправить ордер с signatureType=1 (Proxy), но прокси-контракт еще не развернут (адрес пуст), валидация ордера (L1) провалится.

#### **4.3.2. Доказательная база**

В «Paper Mode» эта проверка часто отсутствует или эмулируется. В «Live Mode» требуется реальное состояние блокчейна..4  
Однако, ошибка отсутствия прокси обычно выявляется после аутентификации запроса, на этапе проверки обеспечения или прав доступа к контракту. Это вызвало бы ошибку бизнес-логики (например, 400, Execution Reverted), а не ошибку шлюза 401. Шлюзу все равно, есть у вас прокси или нет, ему важно, чтобы HTTP-запрос был подписан корректно.

#### **4.3.3. Оценка вероятности**

**10/100**. Маловероятно, что это причина именно кода 401, хотя это может стать следующей ошибкой после исправления аутентификации.

---

### **4.4. Гипотеза Cᛘ4: Дрейф времени (Timestamp Drift)**

#### **4.4.1. Техническая суть проблемы**

Защита от атак повторного воспроизведения (Replay Attacks) требует, чтобы заголовок POLY_TIMESTAMP был в пределах узкого временного окна (обычно ±30-60 секунд от времени сервера). Если часы на VPS отстают, запрос будет отклонен.

#### **4.4.2. Оценка вероятности**

**5/100**. Обычно вызывает ошибку с явным указанием на timestamp (Timestamp out of range), а не общий Invalid api key. Кроме того, это сломало бы и другие запросы.

## **5. Детализация решения и стратегия исправления**

На основе анализа гипотезы Cᛘ1 как доминирующей, мы предлагаем следующее техническое решение. Проблема не в том, какие ключи используются, а в том, как байты передаются по проводам.

### **5.1. Патчинг сериализации в Python**

Разработчику необходимо вмешаться в процесс отправки запроса. Вместо того чтобы полагаться на автоматическую сериализацию requests, нужно подготовить строку JSON вручную.

**Некорректный код (вероятная причина):**

Python

### Стандартный подход, вызывающий ошибку  
payload = {  
    "order": {... },  
    "owner": "0x...",  
    #... другие поля  
}  
### requests вызывает json.dumps(payload) -> добавляет пробелы!  
response = requests.post(url, json=payload, headers=auth_headers) 

**Корректный код (Решение):**

Python

import json  
import requests

### 1. Принудительная компактная сериализация  
### separators=(',', ':') убирает пробелы после разделителей  
compact_json_str = json.dumps(payload, separators=(',', ':'))

### 2. Подпись должна вычисляться именно от этой строки compact_json_str  
timestamp = str(int(time.time()))  
sig_payload = timestamp + "POST" + "/order" + compact_json_str  
signature = generate_hmac(secret, sig_payload)

headers = {  
    "POLY-API-KEY": api_key,  
    "POLY-TIMESTAMP": timestamp,  
    "POLY-SIGNATURE": signature,  
    "Content-Type": "application/json" # Обязательно явно указать тип  
}

### 3. Отправка строки как 'data', а не объекта как 'json'  
response = requests.post(url, data=compact_json_str, headers=headers)

### **5.2. Проверка версии библиотеки py-clob-client**

Если ꆜ использует официальную библиотеку py-clob-client, необходимо проверить файл requirements.txt. Старые версии этой библиотеки могли содержать баг сериализации. Рекомендуется обновиться до последней стабильной версии или, если обновление невозможно, применить «monkey patch» к методу _request класса клиента, внедрив логику, описанную выше.

### **5.3. Верификация Chain ID**

В качестве меры предосторожности необходимо явно проверить Config.py.

* Для **Live Mode**: CHAIN_ID = 137 (Polygon PoS). URL API: https://clob.polymarket.com/.  
* Для **Test Mode**: CHAIN_ID = 80002 (Polygon Amoy). URL API должен соответствовать тестовому стенду (часто меняется, требует уточнения в актуальной документации, ранее был на базе Mumbai).

## **6. Широкий контекст: Проблема детерминизма в распределенных системах**

Инцидент P† является частным случаем фундаментальной проблемы распределенных систем — проблемы детерминированного представления данных. В мире Web2 JSON воспринимается как объектная модель: {a:1} и { a : 1 } семантически равны. В мире Web3 и криптографии JSON — это последовательность байтов. Любое изменение байтов (пробел, перенос строки, порядок ключей) разрушает целостность подписи.

### **6.1. Порядок ключей (Key Ordering)**

Помимо пробелов, потенциальной угрозой является порядок ключей в словаре. В Python 3.7+ словари сохраняют порядок вставки, но JSON стандарт не гарантирует сохранения порядка. Если сервер Polymarket нормализует JSON (сортирует ключи по алфавиту) перед проверкой, а клиент отправляет их в произвольном порядке, подпись также упадет.  
Хотя в данном случае проблема пробелов более вероятна, хорошей практикой является использование sort_keys=True при сериализации для подписи и отправки:

Python

json.dumps(payload, separators=(',', ':'), sort_keys=True)

Это обеспечивает строгий детерминизм на всех платформах и языках.

### **6.2. Рекомендации для будущей разработки**

1. **Логирование «сырых» данных:** При отладке 401 ошибок всегда логируйте не объект dict, а именно строку string, которая уходит в сеть, и строку, которая подписывается. Сравнение этих двух строк часто мгновенно выявляет проблему.  
2. **Изоляция сред:** Использовать разные .env файлы для Mainnet и Testnet, чтобы исключить случайное смешивание CHAIN_ID и ключей.  
3. **Мониторинг дрейфа часов:** Внедрить в бот проверку ntplib при старте, чтобы убедиться, что системное время синхронизировано.

## **7. Заключение**

Анализ инцидента с высокой степенью достоверности указывает на то, что блокировка торговых операций вызвана **некорректной сериализацией тела JSON-запроса** на стороне Python-клиента. Стандартные средства языка добавляют избыточные пробельные символы, которые нарушают криптографическую целостность HMAC-подписи, ожидаемой сервером Polymarket.

Данная проблема не является показателем компрометации ключей или ошибок в смарт-контрактах. Это классический интеграционный конфликт, решаемый путем ужесточения контроля над форматом передаваемых данных. Применение предложенного патча (использование separators=(',', ':') и отправка через data=) должно немедленно восстановить работоспособность системы в режиме Live Trading.

---

## **Дополнительный раздел: Глубокий анализ экосистемы данных Polymarket и альтернативные векторы диагностики**

Примечание: В данном разделе интегрированы дополнительные инсайты, полученные в ходе расширенного анализа исследовательских материалов (6 - 7), для обеспечения максимальной полноты отчета.

## **8. Роль и специфика Data-API и WebSocket в диагностике**

В ходе расследования мы опирались на факт работоспособности WebSocket как на индикатор валидности ключей. Однако, детальный анализ документации 8 выявляет важный нюанс: архитектура потоков данных (WebSocket) и архитектура исполнения ордеров (REST CLOB) в Polymarket могут обслуживаться разными микросервисами с разными требованиями к толерантности.

### **8.1. RTDS (Real-Time Data Socket) как ложноположительный индикатор**

Сервис RTDS (wss://ws-live-data.polymarket.com) используется для получения рыночных данных и событий. Он требует аутентификации только для приватных каналов. Важно отметить, что механизм хендшейка в WebSocket часто реализуется через подпись сообщения GET /ws/connect..., где нет тела запроса.  
Успешное подключение к WS доказывает только то, что:

1. API Key и Secret математически корректны.  
2. Timestamp находится в допустимых пределах.  
3. Клиент умеет правильно подписывать *строки без тела*.

Это подтверждает нашу основную гипотезу: сбой происходит именно в тот момент, когда в уравнении появляется переменная body (тело ордера). Если бы проблема была в ключах, WS не подключился бы. Если бы проблема была во времени, WS отключался бы по таймауту или не проходил хендшейк.

### **8.2. Ограничения Rate Limiting и их влияние на 401**

Анализ материалов по лимитам запросов 10 показывает, что Polymarket использует агрессивное троттлинг-регулирование (например, 50 запросов/10с для определенных эндпоинтов). Важно: в некоторых реализациях API-шлюзов (например, Kong или Nginx) превышение лимита может возвращать не только 429 Too Many Requests, но и иногда маскироваться под ошибки доступа, если шлюз блокирует пользователя по IP.  
Однако, в случае ꆜ, ошибка возникает мгновенно при первом же запросе ордера, что исключает Rate Limiting как причину. Кроме того, сообщение Invalid api key слишком специфично.

## **9. Сравнительный анализ с другими клиентами (TypeScript vs Python)**

Исследование 6 показывает фундаментальное различие в подходах к реализации клиентов.

* **TypeScript (JS):** Метод JSON.stringify() в JavaScript по умолчанию производит *компактный* JSON (без пробелов). Разработчики на Node.js редко сталкиваются с проблемой Cᛘ1, так как их нативный инструмент «из коробки» соответствует ожиданиям сервера.  
* **Python:** Метод json.dumps() по умолчанию производит *разреженный* JSON.

Это объясняет, почему в чатах разработчиков и на StackOverflow 12 проблема непропорционально часто встречается именно у Python-разработчиков. Бэкенд Polymarket, вероятно написанный с использованием Go или Node.js, ожидает поведения, стандартного для этих языков, но нетипичного для дефолтного Python.

## **10. Юридические и комплаенс аспекты («Enable Trading»)**

Хотя мы оценили гипотезу отсутствия прокси как маловероятную причину кода 401, материалы 5 поднимают важный аспект: Geo-Blocking и KYC.  
Polymarket официально ограничивает доступ для пользователей из США (US Persons). Если ꆜ находится в США (в профиле указано "United States, Tigard"), и его IP-адрес не замаскирован через VPN/Proxy, или если его кошелек был помечен как связанный с US, API может блокировать запросы на уровне Cloudflare.  
Обычно это вызывает код 403 Forbidden (Geo-blocked), но в некоторых конфигурациях WAF это может проявляться как отказ в авторизации.  
Рекомендация: Разработчику следует убедиться, что он не нарушает Terms of Service (ToS) платформы, так как технические средства обхода блокировок могут привести к перманентному бану аккаунта и заморозке средств на смарт-контракте. В контексте задачи T мы рассматриваем техническое решение, но игнорировать юридический контекст местоположения пользователя (O.md §5.1) было бы упущением.

## **11. Итоговая сводная таблица диагностических признаков**

Для удобства навигации по проблеме мы составили матрицу симптомов, которая помогла отсеять ложные гипотезы.

| Симптом | Гипотеза сериализации (Cᛘ1) | Гипотеза ключей/сети (Cᛘ2, Cᛘ5) | Гипотеза времени (Cᛘ4) | Соответствие ситуации ꆜ |
| :---- | :---- | :---- | :---- | :---- |
| **Ошибка 401 на POST** | **Да** (из-за тела) | Да (неверный ключ) | Да | **Полное** |
| **Ошибка 401 на GET** | Нет (нет тела) | **Да** (ключ неверен везде) | **Да** | Только POST падает |
| **Ошибка при WS Connect** | Нет | **Да** | **Да** | WS работает |
| **Текст ошибки** | Invalid api key (из-за неверной подписи) | Invalid api key (не найден) | Timestamp error | Invalid api key |
| **Зависимость от языка** | **Высокая (Python)** | Низкая | Низкая | Клиент на Python |

Эта матрица наглядно демонстрирует, почему гипотеза сериализации является единственной, которая объясняет все наблюдаемые факты без противоречий.

## **12. Финальный вердикт**

На основании всестороннего анализа архитектуры, документации, кода и контекста пользователя, мы подтверждаем вывод: **инцидент вызван несоответствием форматов сериализации JSON между клиентом (Python/Requests) и сервером (Polymarket CLOB).**

Решение лежит в плоскости приведения формата данных к каноническому виду перед подписанием и отправкой. Это техническая задача низкого уровня, решение которой полностью восстановит функциональность торгового бота.

#### **Works cited**

1. Authentication - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/CLOB/authentication](https://docs.polymarket.com/developers/CLOB/authentication)  
2. Some endpoints don't accept (valid) JSON that doesn't have extra ..., accessed November 21, 2025, [https://github.com/Polymarket/py-clob-client/issues/164](https://github.com/Polymarket/py-clob-client/issues/164)  
3. RPC endpoints - Polygon Knowledge Layer, accessed November 21, 2025, [https://docs.polygon.technology/pos/reference/rpc-endpoints/](https://docs.polygon.technology/pos/reference/rpc-endpoints/)  
4. Proxy wallet - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/proxy-wallet](https://docs.polymarket.com/developers/proxy-wallet)  
5. Why does PolyMarket create an unverified smart contract wallet for users even when they have their own custodial wallet? - Reddit, accessed November 21, 2025, [https://www.reddit.com/r/ethdev/comments/1eic9z0/why_does_polymarket_create_an_unverified_smart/](https://www.reddit.com/r/ethdev/comments/1eic9z0/why_does_polymarket_create_an_unverified_smart/)  
6. Your First Order - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/quickstart/orders/first-order](https://docs.polymarket.com/quickstart/orders/first-order)  
7. polymarketdataclient package - github.com/Matthew17-21/go-polymarket-real-time-data-client - Go Packages, accessed November 21, 2025, [https://pkg.go.dev/github.com/Matthew17-21/go-polymarket-real-time-data-client](https://pkg.go.dev/github.com/Matthew17-21/go-polymarket-real-time-data-client)  
8. Endpoints - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/CLOB/endpoints](https://docs.polymarket.com/developers/CLOB/endpoints)  
9. Real Time Data Socket - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/RTDS/RTDS-overview](https://docs.polymarket.com/developers/RTDS/RTDS-overview)  
10. API Rate Limits - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/quickstart/introduction/rate-limits](https://docs.polymarket.com/quickstart/introduction/rate-limits)  
11. Clients - Polymarket Documentation, accessed November 21, 2025, [https://docs.polymarket.com/developers/CLOB/clients](https://docs.polymarket.com/developers/CLOB/clients)  
12. How to deal with 401 (unauthorised) in python requests - Stack Overflow, accessed November 21, 2025, [https://stackoverflow.com/questions/26298860/how-to-deal-with-401-unauthorised-in-python-requests](https://stackoverflow.com/questions/26298860/how-to-deal-with-401-unauthorised-in-python-requests)  
13. Issues · Polymarket/clob-client - GitHub, accessed November 21, 2025, [https://github.com/Polymarket/clob-client/issues](https://github.com/Polymarket/clob-client/issues)  
14. Complete Guide to DeFi Development Services for Startups - Rock'n'Block, accessed November 21, 2025, [https://rocknblock.io/blog/guide-to-defi-development-services-for-startups](https://rocknblock.io/blog/guide-to-defi-development-services-for-startups)
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1. 
`L_SOURCE` ≔ (Русский язык)

## 1.2. 
`L_TARGET` ≔ (English)

# 2.
## 2.1.
`D` ≔ (мой ответ `ꆜ`)

## 2.2.
Содержание `D`:
~~~markdown
1) Ваша проблема наверняка вызвана нарушением канонической сериализации JSON (Whitespace Anomaly): https://github.com/Polymarket/py-clob-client/issues/164
2) Краткое объяснение:
Сервер Polymarket требует, чтобы тело JSON-запроса было сериализовано в компактном формате (без пробелов между ключами и значениями) для верификации HMAC-подписи (L2).
Стандартная библиотека `json` в Python по умолчанию добавляет пробелы при сериализации (например, `{"key": "value"}` вместо `{"key":"value"}`).
Если байтовое представление тела запроса, отправленного по сети, отличается от того, которое было использовано для генерации подписи, сервер отвергает запрос с кодом 401.
3) Подробное объяснение:
3.1) Стандартная библиотека `json` в Python при вызове метода `json.dumps()` по умолчанию использует так называемую «pretty-like» сериализацию, добавляя пробелы после разделителей для улучшения читаемости человеком. 
3.2) Дефолтные разделители в Python: `separators=(', ', ': ')`. 
Это означает, что объект `{'a': 1}` превращается в строку `'{"a": 1}'` (с пробелом после двоеточия).
3.3) Однако, высокопроизводительные API, такие как Polymarket CLOB, часто требуют (или подразумевают) «каноническую» или «компактную» форму JSON для расчета подписей, чтобы минимизировать трафик и исключить неоднозначность. 
Компактная форма не содержит пробелов: `'{"a":1}'`.
3.4) Библиотека `requests`, которую использует подавляющее большинство Python-ботов, при передаче словаря в параметр `json=` неявно вызывает `json.dumps()` с настройками по умолчанию. 
Таким образом, по сети улетает «разреженный» JSON.
3.5) Если логика подписания внутри бота (или используемой им библиотеки `py-clob-client`) принудительно удаляет пробелы перед хэшированием (что является стандартом для крипто-подписей), возникает фатальная рассинхронизация:
Client Sign: `Hmac(Secret, Timestamp + POST + /order + {"price":10})`
Network Payload: `{"price": 10}`
Server Verify: `Hmac(Secret, Timestamp + POST + /order + {"price": 10})`
3.6) В итоге, хэши не сойдутся. 
Сервер вернет `401 Unauthorized`, так как подпись не соответствует переданному телу.
~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
3.5) Если логика подписания внутри бота (или используемой им библиотеки `py-clob-client`) принудительно удаляет пробелы перед хэшированием (что является стандартом для крипто-подписей), возникает фатальная рассинхронизация:
Client Sign: `Hmac(Secret, Timestamp + POST + /order + {"price":10})`
Network Payload: `{"price": 10}`
Server Verify: `Hmac(Secret, Timestamp + POST + /order + {"price": 10})`
3.6) В итоге, хэши не сойдутся. 
Сервер вернет `401 Unauthorized`, так как подпись не соответствует переданному телу.
~~~

# 5. `᛭T`
Переведи `F` на `L_TARGET`, с учётом:
- контекста `D`
- `D2`: уже переведённой части `D`
- `᛭O`

# 6. Правила перевода / Общие
## 6.1.
Переводи именно в той стилистике, как написано на `L_SOURCE`.
Не делай перевод более вежливым, чем оригинал.

## 6.2.
Те предложения, которые сейчас полностью на `L_TARGET` — оставь без изменения.

## 6.3.
### 6.3.1.
Не используй Markdown: только plain text.
### 6.3.2.
При этом можно и нужно использовать то форматирование, которое уже есть в оригинале: его не убирай.

## 6.4.
Форматируй перевод в точности как оригинал. 
В частности:
*) каждый абзац должен содержать ровно одно предложение
*) между абзацами не должно оставаться пустых строк.
*) кавычки используй те же, что и в оригинале: «» и ``.

## 6.5.
Не используй жаргон.
Вместо этого используй официальные термины.
### 6.5.1.
В частности, фразы в кавычках используй только в том случае, когда они являются точными цитатами.
Не используй фразы в кавычках для применения жаргонных фраз.
Например, следующий фрагмент текста недопустим, потому что там используется жаргонная фраза «пролетел»: 
```
Например, код, который пушит данные о покупке, подключён асинхронно и загружается с небольшой задержкой, а триггер уже «пролетел».
```

## 6.6.
При обсуждении программного обеспечения используй точные официальные термины на английском языке: именно в том виде, как они указаны в официальной англоязычной документации к этому программному обеспечению.

## 6.7.
### 6.7.1.
Не используй самовольно «you need» и другие подобные обращённые к `ꆜ` фразы, перекладывающие действия на него, если в исходном тексте явно не сказано подобное (типа «вы должны»).
Помни: я пишу `ꆜ`.
Делать в любом случае буду я, а не `ꆜ`.
Именно за то, что описываемую работу делать буду я, `ꆜ` мне будет платить.
Моя задача — показать мою компетенцию и предложить `ꆜ` решение его проблемы, а не переложить решение проблемы на `ꆜ`.

### 6.7.2. Пример
### 6.7.2.1. Пример `F`
```text
Установить и использовать готовый модуль для импорта структурированных данных в Magento.
```
### 6.7.2.2. Примеры допустимого перевода `F`
### 6.7.2.2.1.
```text
Install a ready-made module for importing structured data into Magento.
```
### 6.7.2.2.2.
```text
Installing a ready-made module for importing structured data into Magento.
```
### 6.7.2.3. Пример недопустимого перевода `F`
```text
You need to install a ready-made module for importing structured data into Magento.
```
### 6.7.2.
Не переводи фразы подобные §6.7.2.1, начиная их словом «To».
Пример недопустимого перевода §6.7.2.1:
```text
To install a ready-made module for importing structured data into Magento.
```

### 6.7.3. «It is necessary»
#### 6.7.3.1.
Иногда в контексте §6.7.1 уместно при переводе использовать конструкцию «it is necessary»: она нейтральна и не перекладывает работу на `ꆜ`.
#### 6.7.3.2. Пример `F`
```text
Лучшую из них я намеренно описываю последней (пункт 7): чтобы понять, что она — лучшая, надо сначала увидеть недостатки других.
```
### 6.7.2.3. Примеры допустимого перевода §6.7.3.2
```text
The best of them I intentionally describe last (point 7): to understand why it is the best, it is necessary to first see the disadvantages of the others.
```

## 6.8.
### 6.8.1.
Порой в исходном тексте термины на языке исходного текста дублируются (обычно, в круглых скобках) переводом этих терминов на язык перевода.
### 6.8.2.
Пример:
```text
Реализовать механизм сбора явной обратной связи (Explicit Feedback) в Chatbot Widget.
```
В примере для понятия «явной обратной связи» уже дан правильный перевод этого термина на английский язык: «Explicit Feedback».
### 6.8.3.
Когда ты видишь такие случаи как в §6.8.2, то не надо при переводе дублировать термин.
### 6.8.4.
Например, так переводить текст примера §6.8.2 неправильно:
```text
Implement the mechanism for collecting explicit feedback (Explicit Feedback) in the Chatbot Widget. 
```
В этом неправильном переводе термин «explicit feedback» дублируется.
### 6.8.5.
Правильный перевод в случаях типа §6.8.2 подразумевает убирание дубликата, например:
```text
Implement the mechanism for collecting explicit feedback in the Chatbot Widget. 
```
## 6.9. Правила перевода URL
### 6.9.1.
Если в `F` URL не оформлен посредством синтаксиса Markdown (`[текст URL](URL)`), то тебе запрещено добавлять этот синтаксис.
Вместо этого ты обязан включить URL в перевод в его исходном виде, без добавления `[]()`.
### 6.9.2. Пример
### 6.9.2.1. Пример `F`
```text
В Великобритании она введена в действие посредством «The National Insurance and Industrial Injuries (Turkey) Order, 1961» (S.I. 1961/584): https://www.legislation.gov.uk/uksi/1961/584  
``` 
### 6.9.2.2. Пример правильного перевода `F`
```text
In the United Kingdom, it was given effect by «The National Insurance and Industrial Injuries (Turkey) Order, 1961» (S.I. 1961/584): https://www.legislation.gov.uk/uksi/1961/584
``` 
### 6.9.2.3. Пример неправильного перевода `F`
```text
In the United Kingdom, it was given effect by «The National Insurance and Industrial Injuries (Turkey) Order, 1961» (S.I. 1961/584): [https://www.legislation.gov.uk/uksi/1961/584](https://www.legislation.gov.uk/uksi/1961/584)
``` 
Как видишь, в неправильном переводе URL захерачен в Markdown посредством `[]()`, хотя `F` так не сделано.

## 6.10.
При переводе важное значение имеет `D2`: уже переведённая часть `D`.
Используй её, в частности, чтобы единообразно переводить термины.
Чтобы не получилось так, что в `D2` используется один вариант перевода термина, а в твоём переводе `F` — другой вариант перевода того же самого термина.

## 6.11.
Все числительные должны писаться цифрами (а не прописью).

## 6.12.
До и после перевода `F` ничего не пиши.
В частности, не добавляй от себя заголовки, которых нет в исходном тексте.

## 6.13.
Не переводи текст за пределами `F`.

# 7. Правила перевода / На английский язык
## 7.1.
Не используй сокращения типа «don't». Все подобные фразы пиши полностью: «do not».

## 7.2.
Никогда не переводи понятие «сайт» / «веб-сайт» как «site». 
Вместо этого используй форму «website»: это является более профессиональным.

## 7.3.
### 7.3.1.
Никогда не переводи понятие «пункт нумерованного списка» как «item».
### 7.3.2.
Для пунктов нормативных актов вместо «item» используй тот термин, который принято использовать в данном юридическом контексте: «paragraph», «section» и т.п.
### 7.3.3.
Для всех остальных текстов переводи «item» как «point».

## 7.4.
Вместо «for example» в тексте на английском языке используй «e.g.».
При этом не забывай, что в начале предложения эта фраза должна начинатся с заглавной буквы: «E.g.»
~~~~~~