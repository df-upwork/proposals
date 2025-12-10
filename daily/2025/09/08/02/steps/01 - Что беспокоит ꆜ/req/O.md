# 0.
Сегодня 2025-09-08.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021965005218985973513

## 2.2. Title
Expert Alteryx Developer Needed for Data Analytics Project

## 2.3. Description
`PD` ≔ 
```text
We are seeking an expert Alteryx developer to assist with our data analytics project.

There is a very specific initial problem to solve with Alteryx that can't make use of any pushdown to databases i.e. all data is coming via excel and all processing has to be done natively within Alteryx.

We have a ragged hierarchy expressed in a set of tables and the complexity is that each hierarchy can be composed of sub-hierarchies that can be expressed at different levels.  This is solved easily in SQL with a conditional outer join, but this is proving tricky to replicate in Alteryx natively.

If we can nail this first requirement, there are ~40 other tables and flows that need to have logic translated from SQL into native alteryx.
```

## 2.4. Tags
SQL
Alteryx Analytic Process Automation Platform
Microsoft Excel

# 3. Информация о `ꆜ`
## 3.1. Местоположение
United Kingdom
London

## 3.2. Характеристики компании
### 3.2.1. Сектор экономики
неизвестно

### 3.2.2. Количество сотрудников
неизвестно

## 3.3. Характеристики учётной записи на `UW`
### 3.3.1. Member since
Apr 7, 2020
### 3.3.2. Hire rate (%)
43
### 3.3.3. Количество опубликованных проектов (jobs posted)
7
### 3.3.4. Total spent (USD)
$14K
### 3.3.5. Количество оплаченных часов в почасовых проектах
276

# 4. Другие проекты `ꆜ` на `UW`
## 4.1. `P1⁎`

## 4.1.1. URL
https://www.upwork.com/jobs/~012114ef5bdeebd265

## 4.1.3. Title
React web app for B2B lead generation service

## 4.1.4. Description
`P1D` ≔ 
```text
We have an existing web app built in React but the developer who started the front end has reached the extent of their capability and is not able to continue with the project.  We need a solid developer who understands React and how to get the most out of the framework to deliver a slick user experience.

We're almost at Beta launch with 5 customers lined up to work with the platform for 1-3 months before we do our official launch.  The platform is a new take on lead generation for very specific markets.  We're starting with one market and one product to start with and then intend to expand into many others after the Beta launch.

The stack we have is:
UI - desktop web using React.  It's responsive for desktop and not really intended for mobile at this stage.  It will come but it's not a priority for our customers at present

API - this is using pgAPI which is a Node package that sits on top of postgresql and serves data from database functions.  This is not particularly user friendly at the moment and we are in the process of redesigning with a view to moving to something more flexible.  At the moment though   the first priority is to work with this existing API.  We would like the new developer to help us help drive the design of the new API. The API is only for our use - it's not for public consumption

Payments - this is with Stripe and is integrated but not particularly well.  Communication has been an issue which has led to some relatively poor implementation choices.  We need help to review this and assess how we make sure this is supportable on day 1 beta and then redesigned for us to confidently scale.

Business logic - This is pretty much all currently implemented in postgresql functions that are served up by pgapi as endpoints.  There are definitely areas for improvement as we design the new API to move some responsibilities from the database to the API.

We need someone who can hit the ground running and would like to start the process by requesting a code review of our existing estate - we're happy to pay for that and then make decisions about whether we develop an ongoing relationship.
```

## 4.2. `P2⁎`

## 4.2.1. URL
https://www.upwork.com/jobs/~01e19c97d5396b58d8

## 4.2.2. Title
GitHub actions to deploy Node and React web app on DigitalOcean

## 4.2.3. Description
`P2D` ≔ 
```text
We have a React app backed by Node using Nginx, and we're committing to a Github repo.  It's in beta at the moment and we're prepping for production launch.

Our infra is on Digital Ocean and we have a fairly simple setup with a front end droplet that has a load balancer sitting in front.  We will move to containers but not right now.

The previous dev was deploying changes to our beta completely manually so we need to fix that.

Our first priority is a very simple automation that allows us to manually trigger a deployment of a branch to the DO server, and make it publicly available.  We're open to suggestions on what that is but we do want something super simple to start with.

Our aim with this first task is to establish a relationship with someone that can deliver what we need and then see how we can start developing a more modern and integrated CICD pipeline to support multiple developers
```

# 5.
## 5.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`}

## 5.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 5.3.
`Pi` : `Ps`

# 6.
N/A

# 7.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
There is a very specific initial problem to solve with Alteryx that can't make use of any pushdown to databases i.e. all data is coming via excel and all processing has to be done natively within Alteryx.
~~~
```


 