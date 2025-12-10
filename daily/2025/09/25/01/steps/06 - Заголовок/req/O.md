# 0.
Сегодня 2025-09-25.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021970870593655419818

## 2.2. Title
DevOps, LB in OC spitting 502 when refreshing in a sveltekit SSR project

## 2.3. Description
`PD` ≔ 
```text
Running into a super annoying issue with Oracle Cloud’s load balancer and hoping someone here has seen it before.

Setup:

Frontend is SvelteKit, sitting behind Nginx.

Traffic goes through an Oracle Cloud public load balancer (HTTPS).

Health checks are green, normal client-side navigation works fine.

The problem:
If I refresh a page (so the app does a full server-side render instead of just SPA navigation), the load balancer often spits out a 502 Bad Gateway. If I hit the backend directly (bypass LB), everything works. It only happens through the LB, and only on refresh/deep links.

What I’ve tried:

Bumped up LB timeouts (idle + response) to 60–120s.

Made sure SSR fetches don’t loop back through the public LB domain.

----------------------------------------

this a quick project, we need a quick solution from someone with experience working in similar issue there will be no interview. quick screening through the questioner and we might ask some questions in the chat if we felt that we need it
```

## 2.4. Tags
DevOps
Oracle Cloud
Svelte
Load Balancing

# 5. Информация о `ꆜ`
## 5.1. Местоположение
Saudi Arabia

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Sep 1, 2024
 
### 5.3.2. Hire rate (%)
0
### 5.3.3. Количество опубликованных проектов (jobs posted)
2
### 5.3.4. Total spent (USD)
0
### 5.3.5. Количество оплаченных часов в почасовых проектах
0
### 5.3.6. Средняя почасовая ставка (USD)
0

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
If I refresh a page (so the app does a full server-side render instead of just SPA navigation), the load balancer often spits out a 502 Bad Gateway. If I hit the backend directly (bypass LB), everything works. It only happens through the LB, and only on refresh/deep links.
~~~
```