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

# Пример коррекции сериализации для соответствия ожиданиям сервера  
import json

# Неверно (стандартное поведение):  
# data_str = json.dumps(data) -> '{"price": 0.5, "side": "BUY"}' (с пробелами)

# Верно (для Polymarket CLOB):  
data_str = json.dumps(data, separators=(',', ':'))   
# -> '{"price":0.5,"side":"BUY"}'

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

# 1. Выявленные проблемы, беспокоящие `ꆜ`

Основная проблема клиента (`P†`) определена в `O.md` (§9) и детально описана в `PD` (`O.md` §2.3).

## 1.1. Основная техническая проблема (`P†`): Ошибка аутентификации (401) при отправке боевых ордеров

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

## 1.2. Сопутствующие опасения и неопределённости

Исходя из `PD`, клиент также обеспокоен следующими аспектами:

1.  **Корректность использования учётных данных:** Неопределённость в том, правильно ли бот применяет имеющиеся ключи для аутентификации POST-запросов.
2.  **Логика деривации ключей:** Опасение, что логика получения (деривации) учётных данных может некорректно перезаписывать или использовать ключи («Verify nothing is being overwritten by the credential derivation logic»).
3.  **Различия в потоках аутентификации:** Необходимость чёткого понимания разницы между аутентификацией на основе приватного ключа и API-ключей в контексте Polymarket.

# 2. Анализ обоснованности проблем

Проблема `P†` является полностью обоснованной и критичной для функционирования бота. Код состояния HTTP 401 (Unauthorized) указывает на то, что запрос не был принят из-за недействительных учётных данных аутентификации.

Анализ сложности аутентификации Polymarket API подтверждает, что существует множество потенциальных точек отказа при переходе из тестового режима в боевой.

## 2.1. Двухуровневая аутентификация Polymarket CLOB

Для понимания проблемы критически важно разобрать модель аутентификации Polymarket CLOB, которая состоит из двух уровней (L1 и L2).

### 2.1.1. L1: Аутентификация приватным ключом (EIP-712)

Этот уровень использует приватный ключ кошелька Polygon для подписания структурированных данных ордера в соответствии со стандартом EIP-712. Это криптографически подтверждает намерение владельца средств совершить сделку. L1 также используется для генерации ключей L2.

### 2.1.2. L2: Аутентификация API-ключом (HMAC)

Этот уровень использует API Key, Secret и Passphrase для аутентификации самого HTTP-запроса к серверу CLOB. Он подтверждает право пользователя отправлять команды API. Реализуется через генерацию HMAC-подписи запроса.

### 2.1.3. Интерпретация ошибки

Сообщение `'Unauthorized/Invalid api key'` и код 401 указывают на сбой именно на уровне **L2**. Сервер отклоняет запрос до того, как приступает к валидации ордера (L1), потому что не может верифицировать подпись самого запроса (L2).

## 2.2. Вероятные причины возникновения ошибки 401 (`T1⁎`)

Анализ документации и публичных репозиториев выявил несколько высоковероятных причин сбоя L2-аутентификации в Python-боте.

### 2.2.1. Критическая проблема: Форматирование (сериализация) JSON

Наиболее вероятной причиной является специфическое требование бэкенда Polymarket к формату JSON при расчёте HMAC-подписи (L2). HMAC-подпись генерируется на основе точного строкового представления тела запроса. Если строка, подписанная клиентом, отличается от строки, которую ожидает сервер (даже на один пробел), подписи не совпадут.

В официальном репозитории Python-клиента (`Polymarket/py-clob-client`) зафиксирована проблема (Issue #164), точно соответствующая симптомам клиента:

> "Some endpoints don't accept (valid) JSON that doesn't have extra spaces, and will instead return `{"error":"Unauthorized/Invalid api key"}`"

Стандартные библиотеки Python могут сериализовать JSON с пробелами для читаемости (например, `{"key": "value"}`). Если сервер Polymarket ожидает компактный формат (например, `{"key":"value"}`) и рассчитывает HMAC на его основе, а клиент отправляет форматированный JSON, возникнет ошибка 401.

**Обоснованность:** Высокая. Это подтверждённая проблема, специфичная для Python-реализации и API Polymarket.

### 2.2.2. Некорректная генерация HMAC-подписи (L2)

Если бот реализует логику подписания вручную или использует устаревшую версию библиотеки, ошибка может быть в самом алгоритме генерации HMAC. Это включает:

  * Неправильный порядок конкатенации элементов для подписи (Timestamp, Method, Request Path, Body).
  * Использование неверного API Secret.

**Обоснованность:** Средняя. Стандартные библиотеки обычно реализуют это корректно, но ошибки в интеграции возможны.

### 2.2.3. Ошибки в логике деривации или использования ключей

Клиент явно указал на необходимость проверки логики деривации. Если бот использует ключи от тестовой среды в боевой, или если логика деривации L2-ключей из L1-подписи содержит ошибки (например, используется неверный nonce или приватный ключ), это приведёт к использованию недействительных L2-ключей.

**Обоснованность:** Средняя. Это обоснованное опасение, учитывая явное упоминание этой логики клиентом.

### 2.2.4. Рассинхронизация времени

Аутентификация L2 включает временную метку (`POLY_TIMESTAMP`). Если часы на сервере бота значительно отличаются от времени сервера Polymarket, запрос будет отклонён как просроченный. Это распространённая проблема в API криптобирж.

**Обоснованность:** Низкая, но возможная. Требует проверки синхронизации времени на VPS клиента.

## Заключение

Проблемы клиента (`ꆜ`) обоснованы и связаны со сложностями и неочевидными требованиями аутентификации Polymarket API при переходе в режим реальной торговли. Ошибка 401 указывает на сбой L2-аутентификации.

Наиболее вероятной причиной является специфическая проблема с форматированием JSON-тел запросов (Issue #164 в `py-clob-client`), что приводит к неверному расчёту HMAC-подписи. Другие возможные причины включают ошибки в логике генерации HMAC или некорректное управление/деривацию API-ключей.

