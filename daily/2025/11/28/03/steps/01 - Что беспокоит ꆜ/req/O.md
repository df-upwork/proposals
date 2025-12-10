# 0.
Сегодня 2025-11-28.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021993559314159411838

## 2.2. Title
Zoom API/Developer Needed to Solve Notetaker + Registration Conflict

## 2.3. Description
`PD` ≔ 
```text
# About Us
We run a business coaching and education company that helps trades business owners (plumbing, electrical, HVAC, construction) grow profit, regain time, and systemize their operations. 
We have hundreds of active members in coaching programs and want to better understand how they feel about our experience, what’s working, what’s valuable and where we can improve.

# The Project
##
We currently use Zoom Meetings with registration enabled because we need to capture attendee emails for tracking member engagement. 

##
However, when registration is turned on:
- Our AI notetaker tool (Fathom) is blocked from joining the meeting, even when added as an alternative host or invited attendee.
- Disabling registration allows Fathom to join but then we lose email collection, which we must have for reporting.

##
Zoom live chat support confirmed this is considered a developer/API issue and pointed us toward the Zoom Meeting API as a possible workaround.

##
We need a developer who can come up with a solutions that:
- Ensures our notetaker (Fathom) can join meetings AND
- Keep registration on or capture attendee emails another way

# Requirements:
- Proven experience with Zoom Developer Platform & Zoom API
- Experience with OAuth, webhook events and automated meeting workflows
- Ability to advise on feasibility before implementation
- Clear communication and documentation on any setup needed
- (Bonus) Familiarity with AI notetakers like Fathom.

# Please include in your proposal:
- A short explanation of similar Zoom API works you’ve done
- Your recommended initial approach
- Estimated timeline
- Any questions you need answered before starting

# Deliverables
- Implement the chosen solution OR document a recommended alternative
- Provide step-by-step instructions for our internal team to maintain the setup
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
New Zealand
Hamilton

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Oct 16, 2017
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
24
### 5.3.4. Total spent (USD)
44K
### 5.3.5. Количество оплаченных часов в почасовых проектах
1145
### 5.3.6. Средняя почасовая ставка (USD)
18.32 

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021938456368146305758

### 6.1.2. Title
Wix Velo Developer Needed to Show Dynamic Booking Link by Logged-In User

### 6.1.3. Description
`P1D` ≔ 
```text
We’re looking for an experienced Wix Velo developer to implement a filtered booking system on our members-only site.

Project Overview:
Each of our members is assigned a coach. Each coach has their own booking calendar. We want to ensure that when a member logs in and visits the “Office Hours” page, they see only their own coach’s booking link or embedded calendar—no dropdowns, no access to other coaches.

What We Need:

Detect the logged-in user

Retrieve their assigned coach from the Members collection (already stored)

Look up that coach’s booking link from a separate Coaches collection

Display the correct booking link or embed for that coach only


Deliverables:

Fully functional Velo code to perform the lookup and conditional display

Clean, user-friendly interface showing only relevant booking link and sessions

Basic error handling if data is missing or misconfigured

Ideal Candidate:

Strong experience with Wix Velo and Wix CMS

Confident working with reference fields and dynamic user-based content

Able to deliver a reliable, maintainable solution within a few days
```

### 6.1.4. Publication Date
2 quarters ago

## 6.2. `P2⁎`

### 6.2.1. URL
https://www.upwork.com/jobs/~021837369588669795041

### 6.2.3. Title
Admin Needed for Data Entry & File Management

### 6.2.3. Description
`P2D` ≔ 
```text
We are seeking a detail-oriented Data Entry Specialist to transfer workbook data from our old membership site to our new Wix platform, ensuring each workbook is correctly linked to its corresponding video and identifying any content gaps.

Key Responsibilities:
Input workbook data from the old membership site into the corresponding video sections on Wix.
Ensure each workbook is accurately linked to its respective video.
Organize workbooks and videos into designated categories on Wix.
Identify any missing workbooks and create a list of these gaps.
Maintain high accuracy in data labeling and storage for easy accessibility and management.

Looking for someone who can start asap
```

### 6.2.4. Publication Date
last year

## 6.3. `P3⁎`

### 6.3.1. URL
https://www.upwork.com/jobs/~021895182206338936619

### 6.3.2. Title
Call Review System Development with Fathom and GPT Integration

### 6.3.3. Description
`P3D` ≔ 
```text
We are looking for a skilled developer to create a call review system that integrates with Fathom to pull transcripts and uses GPT to evaluate calls based on a specific rubric. The ideal candidate will have experience with API integrations and AI models to ensure smooth operation and accurate evaluations. Responsibilities include setting up the Zapier automation and designing prompts for the GPT model to generate meaningful insights from the transcripts. Strong attention to detail and problem-solving skills are essential.
```

### 6.3.4. Publication Date
3 quarters ago

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 8.
## 8.1.
`С⁎` ≔ 
```
Компания `ꆜ`:
~~~
a business coaching and education company that helps trades business owners (plumbing, electrical, HVAC, construction) grow profit, regain time, and systemize their operations
~~~
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
- Our AI notetaker tool (Fathom) is blocked from joining the meeting, even when added as an alternative host or invited attendee.
- Disabling registration allows Fathom to join but then we lose email collection, which we must have for reporting.
~~~
```

 