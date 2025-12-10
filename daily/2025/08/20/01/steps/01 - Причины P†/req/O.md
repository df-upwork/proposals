# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`C` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `C` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021957814134474185065

## 2.2. Title
Senior Backend Engineer | API Performance Optimization (AWS + MongoDB)

## 2.3. Description
`PD` ≔ 
```text
We’re looking for a Senior Backend Engineer to troubleshoot and fix slow API response times (~5s) in our pre-production environment. You’ll profile our AWS + MongoDB stack, identify bottlenecks (code, database, or infrastructure), and implement optimizations to get latency down to production-ready levels. This is a short-term, urgent engagement for someone experienced in API performance tuning and scalability.

Must-Have Skills:
• Strong experience with backend APIs (Node.js/Python/Java)
• Deep knowledge of MongoDB query optimization and indexing
• Familiarity with AWS services (EC2, ECS, Lambda, API Gateway, CloudWatch)
• Experience implementing caching strategies (Redis, in-memory, etc.)
• Proven track record in diagnosing and reducing API latency

Deliverable:
• Diagnose API latency issues
• Recommend and implement fixes (code, database, infra)
• Reduce API response time from ~5s to  1s (P95 target)
```

## 2.4. Tags
- MongoDB
- Amazon Web Services
- API Development

# 3. Информация о `C`
## 3.1. Местоположение
USA
Kirkland

## 3.2. Характеристики компании
### 3.2.1. Сектор экономики
неизвестно

### 3.2.2. Количество сотрудников
неизвестно

## 3.3. Характеристики учётной записи на `UW`
### 3.3.1. Member since
Jul 6, 2025
### 3.3.2. Hire rate (%)
100
### 3.3.3. Количество опубликованных проектов (jobs posted)
3
### 3.3.4. Total spent (USD)
$17K
### 3.3.5. Количество оплаченных часов в почасовых проектах
210

# 4. Другие проекты `C` на `UW`
## 4.1. `P1⁎`

## 4.1.1. Title
MongoDB Load Testing & Performance Analysis (No Code Changes)

## 4.1.2. Description
`P1D` ≔ 
```text
We’re looking for an experienced backend performance engineer to help us identify and resolve performance bottlenecks in our MongoDB Atlas-backed fantasy sports app.

During our real-time draft feature, we’ve noticed lag as user traffic scales up. The app runs smoothly with a few users (4–5), but slows significantly when more users join (target is 100+). We’re already on an M30 cluster, but MongoDB Atlas shows spikes in:

Query execution time

Documents scanned per returned

Opcounters

We suspect the issue may be related to inefficient queries or missing indexes, but we’re not entirely sure. We do not want code changes — just a detailed, data-driven performance analysis and load simulation.

Scope of Work:
Run load tests (simulate 100+ concurrent users hitting relevant endpoints)

Tools: Artillery, k6, Locust, or similar

Monitor MongoDB Atlas metrics during test runs

Identify key performance bottlenecks

Suggest optimizations (e.g., indexing strategy, query tuning)

Deliver a short findings report with clear action items

Requirements:
Proven experience with MongoDB Atlas performance tuning

Deep knowledge of query profiling, indexing, and load testing tools

Ability to interpret Atlas dashboards (Query Targeting, Execution Time, etc.)

Familiarity with real-time apps or socket-based backends is a plus

Must be comfortable analyzing backend behavior without modifying any code
```

## 4.2. `P2⁎`

## 4.2.1. Title
Full Stack – Stealth Fantasy Football App Launch

## 4.2.2. Description
`P2D` ≔ 
```text
We’re a stealth startup reimagining fantasy football. Instead of managing a team solo, users collaborate with friends to make key decisions together. We’re preparing for a Fall launch on iOS and Android and need a sharp, proactive teammate to help bring the product across the finish line. (Note: Our Upwork account may still show our original name, Huddle.)

Project Scope:
We're hiring a QA/UX Support Specialist to work 5–15 hours/week (flexible based on your availability) to test, polish, and improve our mobile experience before launch.

Responsibilities:

Review and test signup and onboarding flows for usability and functionality

Identify bugs, broken flows, and confusing UI/UX elements

Collaborate with our CTO and backend team to log and resolve issues

Recommend helper screens, tooltips, or first-time user walkthroughs to improve clarity

Ensure the app is intuitive and accessible—even for users new to fantasy sports

What We’re Looking For:

You don’t need to be a fantasy football expert—in fact, we welcome a fresh perspective

Detail-oriented, solution-minded, and self-directed

Strong communicator who can give clear, actionable feedback

Experience in mobile QA, usability testing, or product design is a plus

Timeline:
This role starts immediately and could expand into a broader support role through August, helping ensure we’re ready for App Store and Play Store submission.
```

# 5.
## 5.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`}

## 5.2.
`Ps` ≔⠿ {`P⁎`, `P1⁎`, `P2⁎`}

## 5.3.
`Pi` : `Ps`

# 6.
## 6.1.
`S⁎` ≔ 
```
Startup, о котором `C` пишет о нём в `P2D`:
~~~
We’re a stealth startup reimagining fantasy football
~~~
```

## 6.2.
⊤ (Все `Pi` касаются `S⁎`)

# 5.
`P†` ≔†
```
Проблема, о которой `C` пишет в `PD`:
~~~
slow API response times (~5s) in our pre-production environment
~~~
```


 