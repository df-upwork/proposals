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

 