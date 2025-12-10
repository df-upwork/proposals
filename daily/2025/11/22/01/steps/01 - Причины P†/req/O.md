# 0.
Сегодня 2025-11-22.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021991792005809079894

## 2.2. Title
Fix Danish Card Declines After Switching Shopify/Stripe Payments to US Entity


## 2.3. Description
`PD` ≔ 
~~~text
#
We recently sold our business and switched our Shopify Payments account from a Danish entity to the buyer’s US entity. 

#
Since the switch, almost all Danish card payments (Visa/Mastercard) are being declined.

# Decline codes include:
- `do_not_honor`
- `network_decline_code`: 59 (Suspected Fraud)
- `declined_by_network`

# Key facts:
- Payments work when we revert to the Danish entity
- Failures are mostly from Danish-issued cards
- We use Shopify Payments (Stripe backend)
- No custom fraud settings or checkout scripts
- Nets is likely the acquiring bank
- Whitelisting was applied by Nets but did not resolve the issue

# We’re looking for someone with strong experience in:
- Shopify Payments / Stripe integration
- Acquiring banks, merchant ID (MID) logic
- Diagnosing card declines or fraud filters
- Cross-border e-commerce payment behavior (EU to US)

# Here is an example failed payment:
```ini
Card issuer: Danske Bank (Visa debit)
Decline code: do_not_honor
Network decline code: 59 (Suspected Fraud)
Amount: DKK 399
Card country: DK
Created: Nov 20, 2025
3DS: Supported, not triggered
Payment method ID: pm_1SVafLQuDGuorNtgOHW5k4NQ
```

# Deliverables
Help us identify and resolve the cause of these card declines so we can continue processing Danish payments under the US entity.
~~~

## 2.4. Tags
Stripe
Payment Gateway
Payment Processing
Fraud & Risk Management
Shopify Payments
Acquiring Banks & MID Logic
Cross-Border Payments
Visa/Mastercard Network Rules
PSD2 / 3D Secure
eCommerce Checkout Optimization
Stripe Dashboard
Shopify Admin
Shopify Markets
Stripe Radar
Payment Gateway Logs

# 5. Информация о `ꆜ`
## 5.1. Местоположение

Denmark
Copenhagen

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
2-9

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Aug 2, 2023
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
12
### 5.3.4. Total spent (USD)
11K
### 5.3.5. Количество оплаченных часов в почасовых проектах
18
### 5.3.6. Средняя почасовая ставка (USD)
39.9

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021981623365633715570

### 6.1.2. Title
Shopify Payments & Subscription Billing Migration (EU → US entity issue)

### 6.1.3. Description
`P1D` ≔ 
```text
#
We run a Shopify store with active subscriptions using Appstle Subscriptions. 
#
The store was originally under a Danish company and used Shopify Payments (EU). 
#
The business is now operated under a US company, and when updating Shopify Payments to the US entity, payouts and recurring subscription billing stopped working due to region/entity restrictions.
#
We need someone with hands-on experience fixing Shopify subscription billing when switching payment providers or regions. 
#
The goal is to get recurring charges working again, ensure new subscribers can check out normally, and make sure payouts go to the US company’s bank account. 
#
We're using Appstle for subscriptions.

# Deliverables
- Identify which payment provider setup will work for a US entity serving EU customers
- Configure Shopify + Appstle to use the new payment gateway
- Ensure existing subscriptions continue billing smoothly (or provide the best possible workaround)
- Ensure payouts go to the US business bank account
- Provide basic documentation of the final setup
```

### 6.1.4. Publication Date
4 weeks ago

### 6.1.5. Payment Terms (USD) 
#### 6.1.5.1. Expected by `ꆜ`  
Hourly
#### 6.1.5.2. Actual
неизвестно

### 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.1.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

### 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

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
Компания `ꆜ`
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
Since the switch, almost all Danish card payments (Visa/Mastercard) are being declined
~~~
```
