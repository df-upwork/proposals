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
Сегодня 2025-11-20.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021990942446178894203

## 2.2. Title
Building a Locally Installed Application That Can Push SQL Data

## 2.3. Description
`PD` ≔ 
```text
One of our products is a CRM designed for the title industry (titlesphere.io).

Integration with Title Production Systems (e.g. SoftPro, Resware) is really important because the entire history of their business - all clients/transactions - exist in those system.

The problem is most of the TPS products feel like they were built in the Window 3.1 era and have never been significantly upgraded.  Most of them either don't have a cloud hosting option, or when they do it's just a virtual desktop environment.  

So at the moment most of that data has to be exported regularly via CSV and then imported into TitleSphere.  Which is obviously not ideal, especially when it can be important that data is updated regularly (daily or even 3-4 times a day is ideal)

What we'd like to do is build an application that can be installed on the locally hosted server (usually in the title company's office) , that can regularly query the TPS system's SQL database and then push that data to TitleSphere via our API.

It's a very small amount of data - probably less than 10MB daily even for large teams.  But its important that it be seamless and automated.

Let me know if you have any questions.

Thank you!

Hayden
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Portland

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Tech & IT

### 5.2.2. Количество сотрудников
10-99

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Oct 19, 2009
### 5.3.2. Hire rate (%)
93
### 5.3.3. Количество опубликованных проектов (jobs posted)
183
### 5.3.4. Total spent (USD)
325K
### 5.3.5. Количество оплаченных часов в почасовых проектах
6147
### 5.3.6. Средняя почасовая ставка (USD)
25.95

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021960800958149804397

### 6.1.2. Title
Sales and/or Marketing for a CRM

### 6.1.3. Description
`P1D` ≔ 
```text
We are looking for someone to help us grow sales for Sphere (https://usesphere.com) and TitleSphere (https://titlesphere.io).  (As well as possibly a new vertical in the near future outside of real estate - exploring which vertical makes most sense right now).   

Someone who can really move the needle top of the funnel - revenue/sales growth (as opposed to brand awareness, Likes, Follows, Thumbs Ups, Bros, etc :).

Our conversion and attrition rates are excellent. Once a user tries it, we’re set. We just need help getting the word out.

We have tried more than a dozen marketing and sales folks over the last 5 years. Most of whom were highly recommended. All of whom have great track records. All of whom were very confident. And none of who were able to have any impact.

This is likely not going to be solved by an off the shelf marketing solution - e.g. SEO, AdWords, Facebook Ads, Facebook groups, Instagram ads, etc have all been tried by multiple experts in the space, who've gotten great results with other businesses on those platforms.  None were close to ROI positive for us (even with a very high LTV).

But possibly there is a creative solution in one of those spaces that can work.  

There is also tons of stuff we haven't tried - e.g. cold calling with targeted list, strategic business development, partnerships, email lists (but not willing to do anything spammy), etc.

This is definitely a challenge. But also huge potential upside.   And we are willing to share that.  Along with an hourly rate we'll add a very meaningful bonuses structure if you can put something together that is ROI positive.  

There is also a budget for testing different strategies/platforms.  

But just to be 100% clear, we have absolutely no interest in building anything intangible right now on the marketing and sales front.  If it doesn't directly lead to an increase in sales in a fairly short timeframe (weeks or months, not years) it's not something we can afford to spend time or money on right now.  

Let me know if you have any questions.

Thanks!

Hayden
```

### 6.1.4. Publication Date
3 months ago

### 6.1.5. Payment Terms (USD) 
#### 6.1.5.1. Expected by `ꆜ`  
Hourly
#### 6.1.5.2. Actual
76 hrs @ $25.00/hr
Billed: $1,658.74

### 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.1.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
3-6 months

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


## 8.3.
Сайты `С⁎`:
- https://www.titlesphere.io
- https://www.usesphere.com

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
The problem is most of the TPS products feel like they were built in the Window 3.1 era and have never been significantly upgraded.  
Most of them either don't have a cloud hosting option, or when they do it's just a virtual desktop environment.  

So at the moment most of that data has to be exported regularly via CSV and then imported into TitleSphere.  Which is obviously not ideal, especially when it can be important that data is updated regularly (daily or even 3-4 times a day is ideal)
~~~
```

# 10.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
What we'd like to do is build an application that can be installed on the locally hosted server (usually in the title company's office) , that can regularly query the TPS system's SQL database and then push that data to TitleSphere via our API.
~~~
```

# 11.
`Sᨀ` ≔ (Система Sphere, которую разрабатывает `С⁎`) 

# 12.
`D⸙` ≔
```
Официальная документация к `Sᨀ`:
https://www.usesphere.com/docs/Sphere.Manual.2024.docx?v=10.1.2.1
```

# 13.
Содержание `D⸙`:
~~~markdown
**GETTING STARTED - IMPORTING & SYNCING**

Getting all your contacts into Sphere, syncing your calendar and email, downloading the Sphere App, and setting a goal for the year are the most important first steps.

**Importing Contacts**

It's important to be selective about which contacts you bring into Sphere. Bringing in hundreds of potential leads from years ago that you never got any traction with will dilute Sphere's effectiveness.

**CSV Upload**

* Go to [People > Import](https://www.usesphere.com/admin/leads/import) (which is a button on the top right). Then go to the Import from CSV section and select the CSV file of contacts you want to import.  
* Sphere has a field mapping tool that will help you map the fields in your CSV into the correct fields within Sphere.  
* You can also see a [sample CSV](https://www.usesphere.com/admin/leads/download-sample-csv?type=people) in this section.

**Gmail or Microsoft Contact Import**

[People > import](https://www.usesphere.com/admin/leads/import) (button in the top right corner on the top of the People page). There is a section for importing from Microsoft and another from Gmail.

**Check for Duplicates**

After your contacts have been imported, check for duplicates. There is a small, gray link on the top of the People page near the import button "[Find Duplicates](https://www.usesphere.com/admin/leads/merge)". You can then either merge, merge as a connection (spouse/partner), or ignore.

If you are going to use the Merge All button in the top left, make sure you look through all the potential duplicates first. Some may not actually be duplicates, and one of the merged contacts will be erased.

**CALENDAR SYNC**

There are two ways to get to this. Go to [Settings > Calendar,](https://www.usesphere.com/admin/settings/calendars) or just click on Calendar on the main menu. There is an “Add Calendar” button at the top of both pages.

Once you have setup your calendar, go to [Settings > Calendar](https://www.usesphere.com/admin/settings/calendars) and decide on the items you want to sync.

**SPHERE APP**

Go to the Apple App Store or Google Play Store and search for “Sphere Real Estate” and the Sphere app should be the first result. Download it on your phone and log in.

**GOALS**

* Setting a goal for the year may be the most important aspect of getting Sphere set up. We've tried to make this incredibly quick and intuitive.  
* Click on the Set a Goal link near the top right on the dashboard. The first time it works as a wizard and asks you one question at a time.  
* Don't spend a lot of time worrying about getting exactly the right answer. It should only take 3-4 minutes. And you can always come back and tweak as much as you like.  
* Once your contacts are imported and your business plan is filled out, you're ready to go.

**DASHBOARD**

* The dashboard is where you start when you login every day. It shows all your high-level stats, how you are tracking against your goals, and provides a list of referral calls each day on the To Do list.  
* The referral calls are only for people you haven't called (or been in a transaction with) in the last 90 days. And anyone with Rank X will never show up on this list (Rank X is for colleagues, vendors, etc.).  
* You can click on the 3 dots on the To-Do list items to assign team members to the item or add a due date.

**TODAY**

* Every morning, the Today page shows you what's going on today as well as what's coming up that you should be aware of, e.g. birthday, housiversaries in the next couple of weeks.  
* You can send handwritten cards to multiple clients at once directly from the Today page.  
* A Today update is sent to your phone via push notification, email, or text each morning (set this up in [Settings > Notifications](https://www.usesphere.com/admin/settings/notifications)).

**PEOPLE**

This is the core functionality most people associate with a CRM. It's where all your contact profiles are stored.

**Adding People**

* You can always import people in bulk via a CSV, from your phone, or from Gmail and Outlook.  
* To add new contacts one at a time in Sphere, click on the ‘+' button, which is always on the top menu. Or go to the People page and click the “Add People” button on the top right.  
* There are two ways to add people. One is for you to type in all the information you have for them into the People page fields.

**Intake Form**

The second is just to add their first name and email address and then toggle on the “Send Intake Email” switch at the bottom. This allows you to send out an email with an intake form to the new contact.

You can also send an intake form to multiple people or even to everyone in your database at once.

Ross does this every year around the holidays. He sends out an intake note that says, "Hey, I can't believe it's almost 2024. I would love to send you a holiday card and celebrate your birthday this year. Can you just make sure my information is up to date?”

And over the next few weeks, hundreds of clients will update their profiles and include all kinds of great additional information—birthdays, favorite books, favorite movies, social media links, kids' birthdays, pets' names, etc.

**Lead Source**

Make sure you record the "Lead Source" or who referred to them when you add a new contact. This allows you to create reports that can show you where your business comes from.

**Mass Actions**

You can always click on the tick box next to one or many people's names on the People page list view to create a mass action (most of which are marketing-related), e.g., send a mass email, SMS, intake form, or handwritten card.

**Labels**

You can create as many custom labels as you like (under [Settings > Labels](https://www.usesphere.com/admin/settings/labels)) and add them to people or transactions. This allows you to easily find and sort contacts and create lists.

**Advanced Filters**

You can use the advanced filter to get a very tailored list of people to either export or use for a mass action, e.g., send an email or SMS to all of them.

You can filter by all the categories at the top of the page, e.g. Rank, Client Type, Labels.

You can decide for each whether to use AND, OR, or NOT. E.g., Rank A OR “Active Seller” AND “$1M” NOT “Vancouver”.

This would create a list of all your Rank A clients and people who are not Rank A but have an “Active buyer” label attached to their name, and only Rank A and active buyers who also have a “$1M” label and who also do not have a “Vancouver” label.

**Interaction Notes**

We try to automatically track everything related to the contacts in the Interaction Notes section. e.g., if you send them a handwritten card, make a referral call, send them an intake form, an email, or a text blast, those are all recorded with all the details we have in Interaction Notes. The date and message you send will be noted in chronological order in the interaction notes.

**Emails**

If you sync Sphere with Gmail or Outlook, all emails to and from the contact will be listed in chronological order in the Email section of their People profile.

**Rank**

There are lots of different ranking philosophies. Ross uses it to track the two things he cares most about - transactions and referrals. Here is his system:

1. **A- **2 transactions or 2 referrals, or one of each.  
2. **B- **1 transaction or 1 referral.  
3. **C- **Haven't done anything yet but really think they will when the opportunity arises.  
4. **D- **Haven't done anything yet and not sure yet if they ever will. Ross tries to either delete Ds or graduate them to Cs every 90 days.  
5. **X- **people who you do not want to market to such as lenders, other brokers, inspectors, etc.

Rank A-D will show up on your to-do list for a referral/check-in call every 90 days (unless they were a part of a transaction in the last 90 days).

The referral call list is an important part of growing your business. If it fills up with people you don't know or don't think it’s worth calling, it's not nearly as useful. So, it's important to only have people ranked A–D who you think are going to help grow your business.

**Connections**

This is the ability to link to contact profiles, e.g., spouses, partners, etc. This allows you to sync some elements of their profiles, e.g., home address, kids, pets.

To connect to profiles, just click on the “Add Connection” button on the top right of the contact page.

**Find Duplicate**

We need to make this easier to find. It's a small font link on the top of the People page next to the Import button.

Finding duplicates allows you to see if potentially the same contact has been entered into Sphere more than once. You can then merge them one at a time or merge the entire list of potential duplicates at once. Just be careful doing this because sometimes people on the list share contact information—e.g., email address or phone number—but are not actually in the same contact.

Along those lines, you can also use the Find Duplicates page to merge as a connection, e.g., connection spouses' profiles.

**Export**

On the top right of the People page, there is an Export button. If you click it, it will export all the contacts in your database.

If you'd like to export a list of people with certain criteria, e.g., a Rank A, you can use the filters on the people page to create that list and then export it.

You can also just manually go through and check the boxes next to the people you want to export.

**TRANSACTIONS**

The Transaction section was designed to help you and your clients track every aspect of a transaction from the point when someone mentions they might want to buy or sell in the next few months through archiving.

**Create a New Transaction**

Either click the ‘+' button on the top menu or click the Add Transaction button on the top right of the transaction page.

**Edit**

To edit a transaction, click on the address on the Transaction page.

**Transaction Stages**

* **All. **This will show you all transactions for the date range selected (which defaults to YTD but can be changed to any date range by using the date selection in the top right).  
* **Potential. **This is often used as a hot list. If anyone even casually mentions they might be interested in buying or selling, you can create a potential transaction for them. If you put in a rough guess for the price, you'll have some sense of what your funnel looks like at any given time.  
* **Active. **Active buyers and sellers.  
* **Listed. **Sellers whose listing is live.  
* **Pending. **Pending buyer and seller transactions.  
* **Closed. **A transaction archive of all your closed transactions, including all documents if you add them.  
* **Got Away. **Any transactions that didn't close, or for which you clicked the "Sell Fell Through" button on the bottom of the Transaction page (which saves a copy of the failed transaction and creates a new transaction with all still relevant data).

**Changing Stages**

You can change the stage of the transaction, e.g., from Potential to Active - with the pulldown menu on the top of the Transaction page.

**Labels**

Labels make it easy for you to find and sort transactions by any criteria. You can create as many custom labels as you like in [Settings > Labels](https://www.usesphere.com/admin/settings/labels) and add them to transactions (or people).

E.g., Ross creates one for every lockbox number and has the rule that it's not allowed to be removed from the transaction until the box is physically removed (and has not lost a lockbox since).

Some labels are also auto generated for stages of the transaction.

**Assignee**

If you have other members of your team that are working on the transaction, add them here.

**Expenses**

Transaction-level expenses are categorized and added to reports.

**Transaction Checklist**

You can create as many unique transaction checklists as you'd like in [Settings > Transactions](https://www.usesphere.com/admin/settings/transaction), e.g., Buyer HOA. You can also add team members to checklist items by default, e.g., Chris is always assigned to the “Thank You Gift” checklist item.

Click on the three dots on a checklist item to open an edit menu that allows you to assign the checklist item to a team member or have an email sent to one/many parties involved when an item is completed.

You can also set a calendar due date for any item or a relative due date for each checklist item, e.g., 2 days before the "Disclosure Deadline”.

**Custom Fields**

You can add or edit transaction fields in [Settings > Transaction > Contract Details](https://www.usesphere.com/admin/settings/transaction/contract).

**Parties Involved**

This allows you to keep track of everyone involved in the transactions and send them updates automatically through the Transaction Timeline.

**Transaction Timeline**

One of our most popular features. The timeline creates a customized client-facing portal for each of your clients' transactions. It allows them to always feel as if they know exactly what's going on and what's happening next.

It also allows you to differentiate yourself in listing appointments because most other agents don't have anything like this. Clients feel more in control, and you receive significantly fewer calls and texts.

You get to decide both whose contact information is listed on the timeline and who receives a copy of the timeline and updates for each transaction.

You can also add and edit explanations of each stage of the timeline in [Settings > Transaction > Contract Details](https://www.usesphere.com/admin/settings/transaction/contract).

You can create a transaction timeline by clicking on the timeline link just below the address at the very top of the transaction page.

**Demand Draft**

This link, just below the address at the very top of a transaction edit page, automatically creates a demand draft using the information you've entered on the transaction page. You can decide for each Demand Draft which fields you want to include.

**Send to Escrow**

In the same spot as the Timeline and Demand Draft links, you'll find the Send to Escrow link. This allows you to automatically create an email to open escrow, include the email address for the escrow officer, and adds the Demand Draft.

**Skyslope**

If you use Skyslope, this button can be used to create and then update the transaction information in Skyslope.

**Document Archive**

A spot for archiving documents related to the transaction for your records. It also allows you to share one or many with parties involved through the transaction timeline.

**Transaction Timeline Links**

This allows you to add links to any sites you think could be helpful for your client or the parties involved. The links are included in the transaction timeline.

**CALENDAR**

Once you sync your Outlook for Google Calendar with Sphere, you can see your calendar and team members' calendars on the Calendar page.

You can decide which Sphere dates (transaction dates, birthdays, housiversaries, etc.) are synced with your calendars in [Settings > Calendar.](https://www.usesphere.com/admin/settings/calendars)

**REPORTS**

The reports currently available are:

* Referrals  
* Referral Calls  
* PopBys  
* Out of Touch  
* Birthday  
* Anniversary  
* Housiversary  
* Lead Source  
* Expense  
* Monthly Summary Report  
* Full Summary Report  
* Annual Report

You can set date ranges, search your results, and list them in order by referral source, total referrals, gross sales volume, and gross commission.

You can also send handwritten cards from some reports, e.g., Birthday and Housiversary.

**MARKETING**

Our goal with Sphere has been to create marketing functionality that we'd be excited for our friends and family to receive. Things that provide useful information—e.g., Equity or make them smile by sending a handwritten birthday card with a gift card for an ice cream Sunday at Salt & Straw.

**Handwritten cards**

We've partnered with a company to provide handwritten cards to your clients, which can include a gift card.

The message on the card and the address and return address on the envelope are written with a ballpoint pen. There are hundreds of cards to choose from (more than a dozen housiversary alone), and you can choose your handwriting style (Ross and I always choose the messiest :).

We price them at $4, including postage.

Cards can be set to be sent automatically in [Marketing > Cards > Card Template.](https://www.usesphere.com/admin/leads/handwrytten-settings)

Or you can send them to one person at a time from a list of people by ticking the box next to the names of those you want one sent to on the People page, the birthday or housiversary list on the Today page, or in Reports.

**Equity**

This is like a lite version of HomeBot. Equity provides a monthly market value and home equity update for the client's home.

You can add one or multiple clients to Equity by clicking on the Equity button under the Marketing menu or clicking on the tick box next to their name on the People page and clicking on the Equity button on the top mass action menu.

When a client is added, they get an initial email explaining what Equity is and asking if they would like to get a monthly equity report. If they opt in, they'll receive an updated report each month.

You can customize the home estimate before the first email is sent as part of the signup process.

You can customize the email templates they receive in [Marketing > Equity > Equity Email >Template](https://www.usesphere.com/admin/equity/notes).

You can see a list of all the clients who are subscribed and their open rates in [Marketing > Equity > Subscription](https://www.usesphere.com/admin/equity/subscription).

The data we use comes from several sources, including the Fed's FRED database and Zillow, but isn't available for all addresses.

**Popby**

This allows you to upload a CSV list of popby's, which will then be added to the interaction notes of each client’s profile.

**Groups**

This allows you to create marketing groups to send mass emails or SMS. In the future, there will also be a filter option on the People page.

**Templates**

This is the complete template library—all the templates you've created in the past as well as a library of stock templates. You can start a mass email here or in Email Blast.

**Email Blast**

This is still being built out, but basic email marketing functionality is now available.

Start by selecting a previous template or creating a new template from scratch.

Then add and edit the content of the email.

Then click Continue in the top-right corner. Add the recipients, either individually or by selecting a group. Create a campaign name (which only you will see), the subject line of the email your recipients will see, and the name and email address you want to be associated with the email.

If you are not going to send it now, make sure you click the Save button at the top.

**What if my emails sent from Sphere are going to Junk/bouncing?**

Google has significantly changed it's requirements for delivering email blasts to Gmail accounts in the last six months in order to try to curtail spam (and another significant update is scheduled for Feb 1).

One of the things they now require for mass emails going to Gmail accounts is the sender's email domain (in your case has a note on account that says it's ok for the server sending the email to use it's domain.

If the DNS record doesn't have a note referencing the sending server (in our case usesphere.com) they will mark the email as spam or in some cases even refuse to deliver them.

The good news is this is an easy addition to make to the DNS record. It only takes a minute and only needs to be done once. The steps depend on who you are using as your DNS host, but they are usually as simple as:

1. Login to your DNS host site  
2. Click on Manage Domain for the URL  
3. Click on Advanced DNS  
4. Click on Add New Record  
5. Select record type "TXT". Under "Host" type in the character '@' and under Value type include:spf.usesphere.com.

We have included a screenshot below of an example of this being added.

![A screenshot of a computerDescription automatically generated][image1]

**SMS Blast**

The landing page on [Marketing > SMS Blast](https://www.usesphere.com/admin/orders/sms-conversation) is an inbox that organizes any SMS conversation by client.

You can create an SMS blast in three ways. You can click on the compost icon on the top right and then type in recipients or select a group.

You can click on the “Send SMS” link on the top left and then tick the boxes next to the clients you want to send the SMS to.

Or you can do something very similar by starting on the People page, ticking the box next to everyone you send an SMS to, and then clicking on the “Send SMS” mass action button at the top of the People page.

**Drip Campaign**

This functionality is still being built out. But it will allow you to use a group or trigger for a list of actions.

For instance, a welcome drip. Anytime anyone is added, they receive a sequence of things, e.g., a welcome email, then two days later an SMS asking if there is anything you can help them with, and four days after that a handwritten welcome card.

Each drip sequence and content are entirely customizable.

**Buy Supplies**

We love All Things Real Estate ([https://www.allthingsrealestatestore.com](https://www.allthingsrealestatestore.com/)) and have built in a link to the Sphere marketing menu to make it easy for you to stock up on signs, logo booties, etc.

**LoLo**

This service is amazing. They connect with the best local businesses in dozens of US cities and provide gift certificates to different businesses each month. The gifts are amazing (e.g., two coffees and pastries at Portland's best bakery), and the price is unbelievable (about $1.25 per client per month).

We can't fully integrate LoLo into Sphere until their API is live later this year. But you can learn more about the service and sign up at [https://lolo.gifts](https://lolo.gifts/).

**TEAM**

We totally overhauled Sphere's team functionality a few years ago to make it much more customizable and modular.

The setup is now similar to that of a social network. You can invite anyone to be on your team. For each person, you get to decide which data you want to share with them, and they get to decide which data they want to share with you.

Making someone part of your team doesn't make them part of anyone else's team (e.g., if you invite two people to your team, they are not automatically connected to each other as well).

The first screen you see when you click on Team is a Team Dashboard. This gives you high-level metrics for everyone on your team.

**Team Settings**

To add someone to your team or create an account for a team member who doesn't have a Sphere account, click on the Team Setting box in the top right corner of the team page.

On the top, you can type in the email address of someone you want to add who already has a Sphere account. Or you can create an account for a team member who doesn't already have one using the “Create an Account” button.

This is also where you can configure and change access privileges for anyone you are connected to.

If you want to pay for team members Sphere subscriptions, you click on the “Manage Subscription” link on this page on the far right of the team members’ row.

**REFERRAL REWARDS**

We put every dime of revenue back into building out and improving the Sphere. So, referrals are huge for us.

And we've tried to make them huge for you too. For every person you refer who subscribes, we'll give them $50 and you $50. A Win/Win/Win.

There are three ways for you to pass on referral rewards.

* Send them your Sphere referral URL. If they click on that to sign up, you both automatically get $50 when they subscribe.  
* Send them your referral code. We've tried to make these as simple as possible, e.g., your first name. But they must remember to enter the code when they sign up. Which virtually no one ever does.  
* Type in their name and email address on the top right of the referral rewards page, and they will get an email with a signup link that gives you both the $50.

**SETTINGS**

We've tried to make Sphere as customizable as possible. Most of that is done in settings.

**Account**

It is important to notice there is a top submenu on the Account Settings page that includes Account Information, Change Password, Signature, Subscription, Coupons, Payments, and Billing.

The two major things Account controls are your profile settings (e.g., profile picture, email signatures, personized URLs for Equity, Intake, etc.) and your account type, billing, and subscription information.

**Email**

This is where you can add or remove any Outlook or Gmail address you want to sync with your Sphere account.

**Calendar**

You can add or remove an Outlook or Gmail calendar and decide which dates in Sphere sync with your calendar and when they show up, e.g., client birthdays, housiversaries and virtually any transaction date.

**Connect**

Connect is like a lite version of Calendly. Once it's configured, it allows you to send a vanity URL to clients so they can find a free spot on your calendar and make an appointment.

In Connect settings, you can decide which days of the week you want to be available and how long an appointment they have the option to make, e.g., 15 minutes, 30 minutes, etc.

**To Do**

This controls what shows up on your to-do list. The big one is the very first option at the top, which determines whether referral calls automatically show up (with Rank A-D clients that you haven't been in touch with in the last 90 days).

**People**

It is important to note that there is a top submenu on People Settings that includes the items below.

**Custom Fields. **You can add any additional fields you'd like to show up on the People page.

**Intake Form. **You can add any additional fields you'd like to show up on the People page.

**Connections. **Allows you to select which fields are automatically synced between connected spouses/partners profiles.

**People Type. **Add to and edit the “Type” list on the People profile pages.

**Lead Tracking. **Add to and edit the Lead Tracking pulldown.

**Transactions**

It is important to note that there is a top submenu on People Settings that includes the items below.

**Checklists. **Create new transaction checklists (as many as you'd like) and edit your existing ones, e.g., add or remove checklist items from them. Start by selecting the checklist you want to edit using the pull-down menu on the top left of the page.

You can now select team members you'd like to be responsible for a checklist item by default for every transaction the checklist is added to here.

You can also specify default relative due dates for each item here.

**Contract Details. **Decide what fields show up on your Transaction page, add additional fields, and determine the characteristics of each, e.g., date or currency, whether they show up on the timeline, etc.  
This is also where you configure defaults for the transaction timeline, e.g., which timeline fields include an explanation, and which have email updates.

**Lead Tracking. **Add and remove items from the Lead Tracking pulldown menu.

**Reviews. **Edit the email template a client receives at the end of a transaction requesting a review and configure the options for the external review sites, e.g., Yelp, Google, Zillow, etc.

**Timeline. **Setting Transaction Timeline defaults are done in [Settings > Transaction > Contract Details](https://www.usesphere.com/admin/settings/transaction/contract). This section allows you to edit the timeline email templates—the initial timeline email as well as Earnest Money Received, etc.

**Skyslope. **If you want to sync Sphere with your Skyslope account, you need to add Skyslope account details here.

**Labels**

Add, edit, or delete labels (some labels can't be deleted because they are incorporated into automated Sphere processes).

**Notifications**

You can decide which type of notification you receive for different types of events, e.g., an open house request, a response on equity, or an intake update.

**Call & SMS**

You can select a phone number that can be used to make calls and send mass SMS through Sphere. Any message sent or received will be automatically added to each client's interaction notes and show up in the SMS inbox.

**Trash**

Any client profiles or transactions that you delete go to the trash so that nothing can ever be entirely deleted accidentally.

~~~ 

# 14. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Research)
https://gemini.google.com/share/1f93a58f670e


## **1 . Введение: Онтологический базис и контекстуализация проблематики**

В современной индустрии титульного страхования и расчетов (Title & Settlement) наблюдается критический разрыв между маркетинговыми обещаниями технологических вендоров и суровой реальностью операционной эксплуатации. Проект P⁎, инициированный клиентом ꆜ, стал катализатором, вскрывшим глубинные архитектурные противоречия в используемых системах класса TPS (Title Production Software). Данный отчет призван не просто перечислить жалобы клиента, но провести их фундаментальную техническую валидацию, опираясь на онтологию ᛭O и детальный анализ документации, технических требований и рыночных сигналов.

Предметом нашего исследования являются две доминирующие платформы, определяющие ландшафт проекта P⁎: **SoftPro** (в частности, ее флагманская версия Select и облачная инкарнация Hosted) и **Resware** (исторически разработанная Adeptive Software, ныне поглощенная Qualia). Обе системы, несмотря на их широкое распространение и статус отраслевых стандартов, демонстрируют признаки технологического устаревания, которые становятся критическими блокирующими факторами при попытке цифровой трансформации агентства.

В рамках онтологии ᛭O, система TPS рассматривается не просто как инструмент ввода данных, но как центральный нервный узел (hub), агрегирующий потоки данных от андеррайтеров, банков, государственных реестров и конечных потребителей. Любая дисфункция в этом узле — будь то латентность интерфейса, невозможность прямого SQL-запроса или сбой XML-шлюза — приводит к каскадным задержкам, потере транзакционной эффективности и, в конечном счете, к финансовым убыткам.

Клиент ꆜ выражает озабоченность по ряду направлений: от потери суверенитета над собственными данными до невозможности внедрения современных AI-инструментов. Наш анализ показывает, что эти проблемы не являются следствием неправильной настройки на местах, а представляют собой фундаментальные ограничения архитектуры «Walled Garden» (огороженный сад), которую вендоры сознательно выстраивают для монетизации транзакций и удержания клиентской базы. Мы рассмотрим, как эволюция от монолитных On-Premise решений к псевдо-облачным (Hosted) конфигурациям создала «худший из двух миров», где клиент теряет контроль над инфраструктурой, не приобретая взамен гибкости истинных SaaS-платформ.

---

## **2 . Архитектурная дихотомия SoftPro: Select On-Premise против Hosted**

### **2.1. Генезис архитектуры SoftPro Select: Многоуровневая модель и ее узкие места**

Для понимания корня проблем производительности, с которыми столкнулся ꆜ, необходимо детально разобрать архитектуру SoftPro Select. Согласно технической документации 1, Select представляет собой классическое.NET приложение, построенное по многоуровневой (n-tier) архитектуре.

1. **Клиентский уровень (Presentation Tier):** «Толстый» клиент (Smart Client), реализованный на Windows Presentation Foundation (WPF) или Windows Forms. Это приложение требует значительных локальных ресурсов для отрисовки интерфейса и выполнения клиентской логики.  
2. **Сервер приложений (Application Tier / Middleware):** Сервис SoftPro Select Server, который обрабатывает бизнес-логику, аутентификацию и маршрутизацию запросов.  
3. **Уровень данных (Data Tier):** Microsoft SQL Server, где хранятся все транзакционные данные, шаблоны документов и конфигурации.

Критически важным аспектом, часто упускаемым при поверхностном анализе, является механизм взаимодействия между этими уровнями. В документации 1 прямо указано: *«All database communication is handled through a single service account used by the mid-tier server. End users do not communicate directly with the database.»* (Вся коммуникация с базой данных осуществляется через единую сервисную учетную запись, используемую сервером среднего звена. Конечные пользователи не общаются с базой данных напрямую).

Это архитектурное решение имеет далеко идущие последствия. В локальной (On-Premise) инсталляции, где все три уровня находятся в одной высокоскоростной локальной сети (LAN) с минимальной задержкой (latency  < 1ms), эта схема работает приемлемо. Однако при переходе в среду Hosted, эта архитектура подвергается стресс-тесту, который она часто не выдерживает.

### **2.2. Иллюзия облака: SoftPro Hosted как симулякр SaaS**

Клиент ꆜ, вероятно, ожидал от перехода на SoftPro Hosted преимуществ современной облачной архитектуры (доступ через браузер, легкие API, масштабируемость по клику). Однако анализ источников 2 показывает, что SoftPro Hosted — это реализация модели **«Lift and Shift»**. Вендор просто берет традиционное десктопное приложение Select и размещает его на своих серверах, предоставляя доступ пользователям через технологии виртуализации (Citrix XenApp или Microsoft Remote Desktop Services).

#### **2.2.1. Проблема «Application Streaming»**

SoftPro Hosted декларирует функциональный паритет с десктопной версией 2, но способ доставки контента кардинально меняет пользовательский опыт (UX). Вместо передачи структурированных данных (JSON/XML), как это делают современные веб -приложения (например, Qualia Core 3), SoftPro Hosted передает *видеопоток* интерфейса и принимает сигналы клавиатуры и мыши.

Это создает жесткую зависимость от качества интернет-канала. Требования к пропускной способности составляют минимум 8 Мбит/с на пользователя.4 Но более критичным параметром является **латентность (ping)** и **джиттер (jitter)**. Поскольку приложение Select изначально разрабатывалось для локальных сетей, оно может совершать сотни мелких синхронных запросов к серверу («chatty protocol») при открытии одной карточки заказа. В локальной сети это незаметно. В удаленной сессии через интернет каждый такой запрос добавляет задержку. Если пинг до дата-центра SoftPro составляет 50-100 мс, интерфейс начинает «фризить», выпадающие списки открываются с задержкой, а ввод текста становится некомфортным.

#### **2.2.2. Периферийная несовместимость**

Другим следствием использования виртуализации является проблема работы с локальными устройствами. Принтеры и сканеры должны «пробрасываться» (redirection) через терминальную сессию. Это часто приводит к конфликтам драйверов и сбоям печати, что является одной из самых частых жалоб пользователей.5 В отличие от веб -приложений, которые просто генерируют PDF для локальной печати, SoftPro Hosted пытается эмулировать прямое подключение к принтеру через WAN-канал, что технологически ненадежно.

### **2.3. Технические требования как индикатор устаревания**

Анализ системных требований для On-Premise версий 1 раскрывает ресурсоемкость платформы. Для обработки потока заказов более 16,000 в месяц требуется кластерная конфигурация с выделением 1 ядра CPU на каждую 1000 заказов и минимум 24 ГБ оперативной памяти только для сервера приложений.

Особое внимание привлекает требование к дисковой подсистеме: *«Disk I/O (throughput) is critical to overall performance»*.1 Это подтверждает, что Select интенсивно работает с временными файлами и базой данных, создавая высокую нагрузку на IOPS. В среде Hosted, где дисковые ресурсы часто виртуализированы и распределяются между множеством клиентов (Multi-tenancy), эффект «шумного соседа» (noisy neighbor) может приводить к непредсказуемым падениям производительности, когда тяжелый отчет одного клиента замедляет работу остальных.

Кроме того, использование IronPython для внутренней автоматизации и скриптинга 6 в Hosted-среде создает риски. Ошибки типа *«Infinite loop detected»*, упоминаемые в технических блогах 6, свидетельствуют о том, что скриптовый движок выполняется синхронно в контексте приложения. В облачной среде, где ресурсы CPU жестко квотируются, зависший скрипт может привести к принудительному завершению сессии пользователя, что воспринимается как «падение» программы.

---

## **3 . Суверенитет данных и проблема доступа к SQL**

### **3.1. Политика изоляции данных в Hosted-среде**

Одной из самых острых проблем для ꆜ является невозможность прямого доступа к данным. В мире корпоративного ПО доступ к базе данных (SQL Access) является стандартом де -факто для построения кастомной аналитики, интеграций и аудита.

Однако в SoftPro Hosted реализована политика **«Black Box»**. Источники 1 подтверждают, что конечные пользователи не имеют прямого доступа к SQL Server. Это ограничение продиктовано архитектурой безопасности мультиарендной среды. Если бы вендор открыл порт 1433 для внешних подключений, возникли бы два риска:

1. **Безопасность:** Риск компрометации всего сервера через уязвимость в одной учетной записи.  
2. **Стабильность:** Неоптимизированный SQL-запрос (например, SELECT  * по таблице с миллионами записей), запущенный клиентом через Excel или PowerBI, мог бы «положить» сервер, обслуживающий десятки других компаний.

### **3.2. Последствия для бизнес-аналитики (BI) и отчетности**

Отсутствие доступа к SQL Read-Only реплике делает невозможным использование современных BI-инструментов (Tableau, Microsoft Power BI, Domo) в режиме Direct Query. Клиент ꆜ вынужден полагаться на встроенные средства отчетности SoftPro или заказывать разработку кастомных отчетов (Custom Reports & Docs services) у самого вендора за дополнительную плату.7

Это создает ситуацию **Vendor Lock-in** (привязка к вендору). Клиент не владеет своими данными в оперативном смысле; он видит их только через призму интерфейса приложения. Любая попытка выгрузить данные для миграции или глубокого анализа превращается в сложный проект с участием техподдержки вендора.

Попытки обойти это ограничение через экспорт в Excel 7 являются паллиативом, так как теряется реляционная структура данных и актуальность в реальном времени. В эпоху Data-Driven управления это является серьезным конкурентным недостатком.

### **3.3. Миф о VPN-туннелировании к базе данных**

В техническом дискурсе часто упоминается использование VPN (например, SoftEther, GlobalProtect) для доступа к ресурсам.8 Однако важно различать типы доступа. VPN в контексте SoftPro Hosted обеспечивает защищенный транспорт для RDP/ICA протокола (доставка картинки), но не открывает сетевой маршрут к портам базы данных (TCP 1433).

Документация по интеграции с Palo Alto Networks и другими шлюзами 9 показывает возможность настройки сложных туннелей, но для SaaS-провайдеров типа SoftPro предоставление клиенту L3-доступа (сетевой уровень) внутрь своего периметра безопасности — это исключительная редкость. Поэтому, даже имея VPN, клиент ꆜ упирается в прикладной фаервол, блокирующий SQL-трафик.

---

## **4 . Экосистема Resware: Наследие SOAP и риски поглощения**

### **4.1. Архитектурный долг: XML и SOAP против современного мира**

Resware представляет собой другой полюс проблемного поля TPS. Если SoftPro страдает от проблем «толстого клиента» в облаке, то Resware является заложником своей устаревшей архитектуры интеграции, базирующейся на SOAP (Simple Object Access Protocol) и тяжеловесном XML.

Интеграция с Resware не следует современным паттернам RESTful API, привычным разработчикам. Вместо этого используется сложная система «ResWare-to-ResWare Partner Mappings».10  
Для настройки обмена данными необходимо:

1. Вручную прописывать URL-адреса веб -сервисов (часто специфичные для каждого партнера).  
2. Использовать WCF (Windows Communication Foundation) с базовой аутентификацией, что требует координации с поддержкой Adeptive для включения соответствующих биндингов на сервере.12  
3. Манипулировать XML-пакетами, где любая ошибка в схеме или отсутствие обязательного поля (например, RemotePrimaryContactEmployeeID) приводит к сбою всей транзакции с неинформативными ошибками.13

Сравнение с современными API (например, Snapdocs или Qualia API 14) показывает, насколько Resware отстает. Современные системы предоставляют Swagger-документацию, песочницы (sandbox) и используют JSON, который легче и быстрее парсится. Работа с Resware требует от ꆜ содержания штата XML-инженеров или оплаты дорогих консультантов для поддержки работоспособности интеграций.

### **4.2. Стратегический риск: Qualia и будущее Resware**

Приобретение Adeptive Software (разработчика Resware) компанией Qualia в конце 2020 года 16 создало ситуацию экзистенциальной неопределенности для пользователей Resware.  
Qualia активно продвигает свою собственную облачную платформу (Qualia Core/Connect) как единое решение для индустрии.3 В этой стратегии Resware отводится роль «устаревшего актива» (legacy asset), который поддерживается только для удержания клиентской базы до момента их миграции на Qualia.

#### **4.2.1. Судебные маркеры риска**

Иск компании Stewart Title против Qualia 19 является ярким индикатором рыночных настроений. Крупные игроки опасаются, что Qualia может в одностороннем порядке изменить условия лицензирования или прекратить поддержку Resware, чтобы форсировать переход на свои продукты. Для проекта P⁎ это означает, что любые инвестиции в кастомизацию Resware сегодня могут оказаться списанными убытками завтра, если платформа будет объявлена EOL (End-of-Life).

#### **4.2.2. Пользовательский опыт и стагнация интерфейса**

Отзывы пользователей на профильных форумах 20 характеризуют интерфейс Resware как «prehistoric» (доисторический) и «not user-friendly». Система требует множественного ввода данных и сложной навигации, что увеличивает время обучения персонала и вероятность ошибок. В условиях дефицита кадров и требований к скорости закрытия сделок, такой UX становится тормозом для бизнеса.

### **4.3. Интеграционные ограничения Resware**

Несмотря на заявленную открытость через XML, интеграция с новыми сервисами остается сложной. Например, интеграция с платформой нотариата Proof (ранее Notarize) требует настройки трех различных типов маппинга (Order Placement, Note/Document, Signings) и использования четырех различных REST API вызовов только для возврата документов.11 Это гибридное использование старых SOAP и новых REST методов создает «зоопарк» технологий внутри одной интеграции, усложняя отладку и мониторинг.

---

## **5 . Интеграционные шлюзы и политика «Walled Garden»**

### **5.1. SoftPro 360: Монетизация доступа и «бутылочное горлышко»**

SoftPro 360 позиционируется как универсальный портал для заказа услуг.22 Однако технически это классический Middleware, который выполняет функцию шлюза.  
Для ꆜ это означает:

1. **Ограничение выбора:** Клиент может работать только с теми вендорами, которые прошли сертификацию SoftPro и интегрированы в сеть 360 . Подключение локального поставщика услуг, не входящего в этот список, невозможно без участия SoftPro, что занимает месяцы и стоит дорого.  
2. **Финансовая нагрузка:** Бизнес-модель SoftPro 360 часто предполагает взимание транзакционных комиссий (click fees) за каждый заказ услуги. Это скрытый налог на эффективность, который увеличивает операционные расходы (OpEx) агентства.  
3. **Отсутствие кастомизации:** Данные передаются в жестко заданном формате. Если ꆜ хочет передать специфическое поле данных партнеру (например, код кампании в маркетинговую систему), стандартный коннектор 360 может это не поддерживать, и изменить это самостоятельно клиент не может.22

### **5.2. SoftPro Sync и ограничения API**

Существует функционал SoftPro Sync 24, позволяющий обмениваться данными между различными инсталляциями SoftPro (например, между агентом и андеррайтером). Однако это закрытый протокол «SoftPro-to-SoftPro». Он не решает задачу интеграции с внешним миром (CRM, ERP, HR-системы).

Документация упоминает наличие API 23, но для клиентов Hosted-версии возможности его использования ограничены запретом на установку стороннего кода (Custom Assemblies) на сервере приложений. Это вынуждает клиентов использовать RPA (Robotic Process Automation) как «костыль» для интеграции.

---

## **6 . Анализ сторонних интеграторов: AI и автоматизация коммуникаций**

### **6.1. Alanna.ai: Потенциал AI против реальности Legacy**

Alanna.ai предлагает революционный подход — диалоговый AI для ответов на вопросы клиентов.25 Однако эффективность AI напрямую зависит от доступа к данным.

* **Техническое противоречие:** Для того чтобы Alanna могла ответить на вопрос «Где мои документы?», она должна прочитать статус заказа и содержимое документов из TPS.  
* **Методы интеграции:** Alanna заявляет о глубокой интеграции с SoftPro и Resware.27 В случае с SoftPro On-Premise это реализуется через прямой SQL-запрос или установку локального агента. В случае SoftPro Hosted, Alanna вынуждена работать через ограниченный API SoftPro 360 или требовать от SoftPro открытия специальных доступов, что часто встречает сопротивление со стороны IT-безопасности вендора.  
* **Ограничения функционала:** Без полного доступа к данным AI превращается в простой чат-бот, работающий по скриптам, что нивелирует его ценность. Проблема ꆜ может заключаться именно в том, что в их конфигурации (Hosted) Alanna не может реализовать свой потенциал «умного помощника».

### **6.2. CloseSimple: Автоматизация с ручным управлением**

CloseSimple предлагает «Pizza Tracker» для сделок.29 Анализ документации вскрывает важный нюанс: существует три режима работы интеграции — Manual, Automated и Combination.

* **Manual:** Пользователь должен вручную нажать кнопку в SoftPro, чтобы отправить обновление статуса. Это не уменьшает нагрузку на персонал, а просто меняет инструмент.  
* Automated: Требует настройки триггеров в SoftPro Automation Services. В Hosted-среде доступ к этому конфигуратору часто закрыт для клиента.  
  Таким образом, ꆜ может платить за сервис автоматизации, но использовать его в ручном режиме из -за ограничений прав доступа в облаке SoftPro.

---

## **7 . Роль RPA: UiPath и Automation Anywhere как вынужденная мера**

В условиях закрытых API и отсутствия доступа к БД, индустрия все чаще обращается к **RPA (Robotic Process Automation)**. Инструменты вроде UiPath и Automation Anywhere 31 используются для эмуляции действий пользователя.

**Сценарий использования:** Робот запускает Citrix-сессию SoftPro Hosted, распознает изображение на экране (OCR/Computer Vision), находит нужные поля, копирует данные и вставляет их в веб -портал андеррайтера или CRM.

**Плюсы:**

* Не требует API и разрешений вендора (работает через пользовательский интерфейс).  
* Позволяет связать несвязанные системы («Swivel chair automation»).

**Минусы и риски:**

* **Хрупкость:** Малейшее изменение разрешения экрана, шрифта или расположения кнопки в SoftPro Hosted приведет к сбою робота.  
* **Скорость:** RPA через Citrix работает медленно, так как зависит от отрисовки графики.  
* **Стоимость:** Лицензии Enterprise RPA платформ (UiPath) дороги, а разработка и поддержка роботов требуют квалифицированных кадров.

Для ꆜ использование RPA — это признак того, что штатные средства интеграции TPS провалились. Это дорогостоящий «пластырь» на архитектурную проблему.

---

## **8 . Сравнительная таблица рисков и ограничений**

Ниже представлена сводная матрица анализа ключевых проблемных зон для SoftPro и Resware, сформированная на основе изученных данных.

| Категория риска | SoftPro Select (Hosted) | Resware (Qualia) | Влияние на проект P⁎ |
| :---- | :---- | :---- | :---- |
| **Доступ к данным** | **Блокирующий.** Нет прямого SQL доступа. Данные изолированы в "черном ящике". 1 | **Сложный.** Возможен через XML-выгрузки, но требует парсинга. Прямой доступ к БД зависит от хостинга. | Невозможность построения BI, зависимость от вендора при миграции. |
| **Интеграция** | **Walled Garden.** Только через SoftPro 360 . Сторонние API ограничены. 22 | **Legacy.** SOAP/XML. Требует сложного маппинга и настройки WCF. 11 | Высокие затраты на подключение новых партнеров. Ограничение инноваций. |
| **Производительность** | **Зависимая.** RDP/Citrix чувствительны к латентности сети. Проблемы с печатью. 5 | **Стабильная**, но интерфейс перегружен и требует много кликов (UX friction). 20 | Снижение производительности сотрудников, фрустрация пользователей. |
| **Будущее платформы** | **Стагнация.** "Облако" как маркетинговая обертка для старого ПО. 2 | **Угроза EOL.** Риск закрытия продукта в пользу Qualia Core. 19 | Риск потери инвестиций в настройку и обучение. |
| **Автоматизация** | **Ограниченная.** Скрипты IronPython могут блокироваться. 6 | **Мощная**, но сложная в настройке (Action Lists). Требует экспертных знаний. | Сложность реализации сквозных процессов без ручного вмешательства. |

---

## **9 . Заключение и стратегические рекомендации**

Проведенный глубокий анализ подтверждает, что проблемы, с которыми столкнулся клиент ꆜ в рамках проекта P⁎, носят системный и архитектурный характер. Они не являются следствием локальных ошибок конфигурации, а проистекают из фундаментальных стратегий вендоров (SoftPro и Qualia), направленных на удержание контроля над экосистемой и данными клиентов.

**Ключевые выводы:**

1. **Архитектурный тупик SoftPro Hosted:** Переход на Hosted-версию SoftPro Select для требовательного клиента с потребностью в данных и интеграциях является шагом назад. Это решение сочетает недостатки десктопного ПО (ресурсоемкость, сложность обновлений) с недостатками облака (зависимость от канала, потеря контроля над БД), не предлагая преимуществ истинного SaaS.  
2. **Токсичность актива Resware:** Использование Resware в долгосрочной стратегии представляет собой высокий риск. Платформа находится под угрозой каннибализации со стороны материнской компании Qualia. Технический долг в виде SOAP/XML архитектуры делает поддержку интеграций неоправданно дорогой.  
3. **Барьеры для Инноваций:** Внедрение AI (Alanna) и автоматизации (CloseSimple) на базе текущих TPS сталкивается с искусственными барьерами. Вендоры TPS заинтересованы в продаже собственных, зачастую уступающих по качеству, аддонов, и поэтому ограничивают возможности интеграции для сторонних передовых решений.

**Стратегические рекомендации для ꆜ:**

* **Сценарий А (Восстановление контроля):** Если бизнес-процессы жестко завязаны на функционал SoftPro Select, рассмотреть возврат к модели **On-Premise** (или IaaS — Infrastructure as a Service, где клиент арендует серверы, но управляет ими сам). Это вернет прямой доступ к SQL, позволит настраивать VPN-туннели для данных и использовать локальные интеграции.  
* **Сценарий Б (Модернизация):** Начать планирование миграции на современную **Cloud-Native TPS** (например, Qualia Core, если устраивает их экосистема, или независимые игроки типа Spruce/Endpoint, если они доступны на рынке). Это решит проблемы производительности интерфейса и API-доступности, но потребует полной перестройки процессов.  
* **Сценарий В (Гибридная автоматизация):** В текущей конфигурации инвестировать в **RPA** как временное решение для преодоления интеграционных разрывов, понимая высокую стоимость владения и хрупкость этого решения. Отказаться от попыток построить Real-time BI на базе Hosted-данных, перейдя на асинхронную отчетность (ежедневные выгрузки).

Ситуация требует от ꆜ принятия жестких решений: либо смириться с ролью пассивного пользователя в «огороженном саду» вендора, либо инвестировать в собственную инфраструктуру для возвращения цифрового суверенитета.

---

*Конец отчета.*

#### **Works cited**

1. SoftPro Select System Requirements, accessed November 20, 2025, [https://www.softprocorp.com/softpro-system-requirements-select/](https://www.softprocorp.com/softpro-system-requirements-select/)  
2. Real Estate Hosted Software Data  - SoftPro, accessed November 20, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-hosted-software/](https://www.softprocorp.com/real-estate-software-solutions/softpro-hosted-software/)  
3. Resware  - Qualia, accessed November 20, 2025, [https://www.qualia.com/resware/](https://www.qualia.com/resware/)  
4. SoftPro System Requirements – Hosted, accessed November 20, 2025, [https://www.softprocorp.com/softpro-system-requirements-hosted/](https://www.softprocorp.com/softpro-system-requirements-hosted/)  
5. SoftPro Support: The Most Common Issues & How to Solve Them  - Premier One, accessed November 20, 2025, [https://premier-one.com/softpro-support-the-most-common-issues-how-to-solve-them/](https://premier-one.com/softpro-support-the-most-common-issues-how-to-solve-them/)  
6. Error | Home on the web  ~ Dan Van Fleet, accessed November 20, 2025, [http://danvanfleet.com/index.php/tag/error/](http://danvanfleet.com/index.php/tag/error/)  
7. Custom Reports & Docs  - SoftPro, accessed November 20, 2025, [https://www.softprocorp.com/software-services/custom-reports-and-docs/](https://www.softprocorp.com/software-services/custom-reports-and-docs/)  
8. SoftEther VPN vs. SoftPro Comparison  - SourceForge, accessed November 20, 2025, [https://sourceforge.net/software/compare/SoftEther-VPN-vs-SoftPro/](https://sourceforge.net/software/compare/SoftEther-VPN-vs-SoftPro/)  
9. Sitemap  - Palo Alto Networks, accessed November 20, 2025, [https://docs.paloaltonetworks.com/sitemap](https://docs.paloaltonetworks.com/sitemap)  
10. ResWare/A.S.K. Search Integration User Guide  - Stewart Title, accessed November 20, 2025, [https://www.stewart.com/content/dam/stewart/education-and-training/PDFs/resware-a.s.k-search-integration-user-guide.pdf](https://www.stewart.com/content/dam/stewart/education-and-training/PDFs/resware-a.s.k-search-integration-user-guide.pdf)  
11. Resware & Notarize | How it Works, accessed November 20, 2025, [https://www.notarize.com/blog/resware-notarize](https://www.notarize.com/blog/resware-notarize)  
12. Resware to Resware Mappings  -  - The Docs, accessed November 20, 2025, [https://www.getroo.io/docs/resware/partner-resware-to-resware/](https://www.getroo.io/docs/resware/partner-resware-to-resware/)  
13. Common error messages in ResWare  - Proof Help Center, accessed November 20, 2025, [https://support.proof.com/hc/en-us/articles/1500002944961-Common-error-messages-in-ResWare](https://support.proof.com/hc/en-us/articles/1500002944961-Common-error-messages-in-ResWare)  
14. Snapdocs Scheduling Open API  - Support Hub, accessed November 20, 2025, [https://support.snapdocs.com/open-api](https://support.snapdocs.com/open-api)  
15. Qualia API, accessed November 20, 2025, [https://www.qualia.com/qualia-api/](https://www.qualia.com/qualia-api/)  
16. Qualia Acquires Developer of ResWare  - ALTA, accessed November 20, 2025, [https://www.alta.org/news-and-publications/news/20201222-Qualia-Acquires-Developer-of-ResWare](https://www.alta.org/news-and-publications/news/20201222-Qualia-Acquires-Developer-of-ResWare)  
17. Our Next Stage  - Qualia Insight, accessed November 20, 2025, [https://blog.qualia.com/qualia-acquires-adeptive-resware/](https://blog.qualia.com/qualia-acquires-adeptive-resware/)  
18. Resware Comparison  - Qualia, accessed November 20, 2025, [https://www.qualia.com/resware-comparison/](https://www.qualia.com/resware-comparison/)  
19. Stewart Title files suit against Qualia over software license | News  - The Title Report, accessed November 20, 2025, [https://www.thetitlereport.com/Articles/Stewart-Title-files-suit-against-Qualia-over-softw-90030.aspx](https://www.thetitlereport.com/Articles/Stewart-Title-files-suit-against-Qualia-over-softw-90030.aspx)  
20. Is it just me or do people also feel that there needs to be better settlement/closing software for title insurance companies? : r/RealEstate  - Reddit, accessed November 20, 2025, [https://www.reddit.com/r/RealEstate/comments/3r2mz4/is _it _just _me _or _do _people _also _feel _that _there/](https://www.reddit.com/r/RealEstate/comments/3r2mz4/is_it_just_me_or_do_people_also_feel_that_there/)  
21. Real Estate Software : r/paralegal  - Reddit, accessed November 20, 2025, [https://www.reddit.com/r/paralegal/comments/qdf7wc/real _estate _software/](https://www.reddit.com/r/paralegal/comments/qdf7wc/real_estate_software/)  
22. SoftPro 360 Integrations, accessed November 20, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/](https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/)  
23. SoftPro Select  - Real Estate Closing Software, accessed November 20, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-select/](https://www.softprocorp.com/real-estate-software-solutions/softpro-select/)  
24. Resources for the SoftPro Sync integration in SoftPro 360, accessed November 20, 2025, [https://info.softprocorp.com/resources-for-softpro-sync-integration-in-softpro-360](https://info.softprocorp.com/resources-for-softpro-sync-integration-in-softpro-360)  
25. Softpro intgeration | alanna.ai, accessed November 20, 2025, [https://www.alanna.ai/softpro-integration/](https://www.alanna.ai/softpro-integration/)  
26. Why AI Will Actually Restore Some of our Humanity  - American Land Title Association, accessed November 20, 2025, [https://www.alta.org/news-and-publications/news/20250123-Why-AI-Will-Actually-Restore-Some-of-Our-Humanity](https://www.alta.org/news-and-publications/news/20250123-Why-AI-Will-Actually-Restore-Some-of-Our-Humanity)  
27. Pythonic.ai vs Alanna.ai, accessed November 20, 2025, [https://www.alanna.ai/pythonic-vs-alanna/](https://www.alanna.ai/pythonic-vs-alanna/)  
28. Alanna.ai vs CloseSimple Review, accessed November 20, 2025, [https://www.alanna.ai/alanna-ai-vs-closesimple/](https://www.alanna.ai/alanna-ai-vs-closesimple/)  
29. CloseSimple  + SoftPro; Elevate Your Closing Experience, accessed November 20, 2025, [https://www.closesimple.com/resources/softpro-white-paper](https://www.closesimple.com/resources/softpro-white-paper)  
30. CloseSimple  + ResWare; Elevate Your Closing Experience, accessed November 20, 2025, [https://www.closesimple.com/resources/resware-white-paper](https://www.closesimple.com/resources/resware-white-paper)  
31. The Top 9 Digital Transformation Solutions for Credit Unions in 2026 | Proof, accessed November 20, 2025, [https://www.proof.com/blog/the-top-9-digital-transformation-solutions-for-credit-unions-in-2026](https://www.proof.com/blog/the-top-9-digital-transformation-solutions-for-credit-unions-in-2026)  
32. Maximize Efficiency in Your Title Business with AI, accessed November 20, 2025, [https://www.skylinetitlesupport.com/blog/maximize-efficiency-in-your-title-business-with-ai](https://www.skylinetitlesupport.com/blog/maximize-efficiency-in-your-title-business-with-ai)

# 15.
## 15.1.
`D𐊑⠿` ≔ ⠿~ (Заблуждения `ꆜ` относительно `P⁎`)

## 15.2.
`D𐊑ᵢ` : `D𐊑⠿`

## 15.3.
`Pⰳ(D𐊑ᵢ)` ≔
```
Правдоподобность `D𐊑ᵢ`.
Правдоподобность заблуждения `D𐊑ᵢ` означает оценку того, насколько утверждение `D𐊑ᵢ` действительно является заблуждением `ꆜ`. 
```

# 16. Анализ `D𐊑⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/94bacc2fc0cf

## 1. Идентификация потенциальных заблуждений `ꆜ` (`D𐊑⠿`)

Анализ проекта `P⁎`, предложенного клиентом (`ꆜ`), направлен на создание локально устанавливаемого приложения (`T⁎`) для прямого извлечения данных из SQL-баз систем производства титулов (TPS) и их отправки в CRM TitleSphere. Цель — автоматизировать процесс, который сейчас выполняется через ручной экспорт CSV (`O.md`::`P†`).

Исследование задачи в контексте онтологии `᛭O` и анализа рынка (`O.md`::§14) выявило, что видение проекта основано на нескольких критических предположениях, которые с высокой степенью вероятности являются заблуждениями (`D𐊑⠿`). Эти заблуждения касаются технической осуществимости, организационной приемлемости и сложности реализации предложенного решения.

`D𐊑⠿` ≔ ⠿{`D𐊑₁`, `D𐊑₂`, `D𐊑₃`, `D𐊑₄`}

### 1.1. `D𐊑₁`

`D𐊑₁` ≔

```
Предположение об универсальной доступности прямого доступа к SQL-базам данных TPS.
```

### 1.2. `D𐊑₂`

`D𐊑₂` ≔

```
Игнорирование организационных, регуляторных барьеров и политик безопасности (IT Friction).
```

### 1.3. `D𐊑₃`

`D𐊑₃` ≔

```
Предположение о гомогенности технологического ландшафта TPS и универсальности предложенного решения.
```

### 1.4. `D𐊑₄`

`D𐊑₄` ≔

```
Недооценка сложности извлечения данных (ETL) и стоимости поддержки прямой SQL-интеграции.
```

## 2. Анализ и оценка `D𐊑⠿`

### 2.1. Анализ `D𐊑₁`: Универсальная доступность SQL

Клиент предполагает, что установка приложения на "locally hosted server" позволит "regularly query the TPS system's SQL database" (`O.md`::§10).

#### 2.1.1. Доводы за `Pⰳ(D𐊑₁)` (Это заблуждение)

1.  **Распространенность Hosted-сред:** Значительная часть рынка использует Hosted-решения (например, SoftPro Hosted). Это не истинные облачные решения, а виртуализация десктопных приложений (RDP/Citrix) (`O.md`::§14.2.2).
2.  **Политика "Black Box":** В Hosted-средах вендоры контролируют инфраструктуру и блокируют прямой доступ к SQL Server для обеспечения безопасности и стабильности мультиарендной среды (`O.md`::§14.3.1). Доступ к портам базы данных извне не предоставляется (`O.md`::§14.3.3).
3.  **Архитектура N-Tier:** Даже при локальном (On-Premise) развертывании системы, такие как SoftPro Select, используют многоуровневую архитектуру. Доступ к базе данных осуществляется исключительно через сервер приложений, а не напрямую конечными пользователями или сторонними приложениями (`O.md`::§14.2.1).

#### 2.1.2. Доводы против `Pⰳ(D𐊑₁)` (Это не заблуждение)

1.  **Сегмент On-Premise:** Существуют истинные локальные инсталляции, где титульная компания полностью контролирует сервер и технически может предоставить доступ к SQL.
2.  **Целевой фокус:** Возможно, `ꆜ` осознанно фокусируется только на сегменте On-Premise, считая его достаточным.

#### 2.1.3. Вердикт

Заблуждение заключается в генерализации подхода. Решение, основанное исключительно на прямом доступе к SQL, неприменимо к значительному и растущему сегменту Hosted-решений. Предложенное техническое решение (`T⁎`) не может служить универсальным интеграционным продуктом для всей клиентской базы.

**`Pⰳ(D𐊑₁)` ≔ 85/100**

-----

### 2.2. Анализ `D𐊑₂`: Игнорирование барьеров безопасности и комплаенса

Предположение, что титульные компании согласятся установить стороннее ПО и предоставить ему прямой доступ к своим производственным базам данных.

#### 2.2.1. Доводы за `Pⰳ(D𐊑₂)`

1.  **Регуляторная среда (NPI/GLBA):** Индустрия титульного страхования обрабатывает крайне чувствительные персональные и финансовые данные (Non-public Personal Information - NPI) и строго регулируется (например, законом Gramm-Leach-Bliley Act - GLBA).
2.  **Отраслевые стандарты (ALTA Best Practices):** Стандарты ALTA требуют строгого контроля доступа к NPI, применения принципа наименьших привилегий (PoLP) и формализованного управления рисками поставщиков (Vendor Risk Management).
3.  **Критические риски безопасности:** Прямой доступ к базе данных значительно увеличивает поверхность атаки (утечка учетных данных, SQL-инъекции) и позволяет обойти механизмы контроля и аудита, реализованные на уровне приложения TPS.
4.  **Риски стабильности и производительности:** IT-отделы будут блокировать установку стороннего ПО на критически важные серверы из-за опасений, что прямые SQL-запросы могут вызвать замедление работы или сбои в производственной системе (`O.md`::§14.3.1).

#### 2.2.2. Доводы против `Pⰳ(D𐊑₂)`

1.  **Бизнес-мотивация:** Клиенты заинтересованы в автоматизации трудоемкого ручного процесса экспорта CSV (`O.md`::`P†`).
2.  **Снижение рисков:** Доступ можно ограничить учетной записью только на чтение (Read-Only) или доступом к реплике базы данных.

#### 2.2.3. Вердикт

Это наиболее критическое заблуждение. В строго регулируемой финансовой индустрии организационные и безопасностные барьеры являются определяющими. Получение разрешения на установку такого агента будет чрезвычайно сложным. IT и комплаенс-отделы клиентов с высочайшей вероятностью заблокируют такую инициативу из-за неприемлемых рисков.

**`Pⰳ(D𐊑₂)` ≔ 95/100**

-----

### 2.3. Анализ `D𐊑₃`: Гомогенность ландшафта и универсальность решения

Клиент запрашивает "an application" для интеграции с "Title Production Systems (e.g. SoftPro, Resware)" (`O.md`::§2.3) путем запроса к "SQL database", подразумевая единый подход.

#### 2.3.1. Доводы за `Pⰳ(D𐊑₃)`

1.  **Фундаментальные различия архитектур:** SoftPro и Resware имеют принципиально разные технологические стеки. SoftPro базируется на .NET/MS SQL (`O.md`::§14.2.1). Resware использует устаревшую архитектуру интеграции на основе SOAP/XML и WCF (`O.md`::§14.4.1). Прямой доступ к SQL не является стандартным методом интеграции для Resware.
2.  **Разнообразие моделей развертывания:** Разные модели хостинга (On-Premise vs. Hosted) требуют разных подходов к интеграции. Там, где SQL недоступен, могут потребоваться альтернативные методы, такие как RPA (Robotic Process Automation) (`O.md`::§14.7) или использование вендорских API.
3.  **Стратегия "Walled Garden":** Вендоры продвигают собственные контролируемые интеграционные шлюзы (например, SoftPro 360) (`O.md`::§14.5.1), создавая фрагментированный ландшафт.

#### 2.3.2. Доводы против `Pⰳ(D𐊑₃)`

1.  **Модульная архитектура:** Под "an application" можно подразумевать модульную систему с различными адаптерами (SQL, API, RPA), хотя описание проекта фокусируется исключительно на SQL.

#### 2.3.3. Вердикт

Предложенный технический подход (запрос к SQL) не является универсальным. Он неприменим к Resware и облачным версиям SoftPro. Создание надежной интеграции потребует разработки отдельных коннекторов для каждого вендора и типа развертывания.

**`Pⰳ(D𐊑₃)` ≔ 90/100**

-----

### 2.4. Анализ `D𐊑₄`: Недооценка сложности ETL и стоимости поддержки

Клиент ожидает, что решение будет "seamless and automated", и подкрепляет это аргументом о малом объеме данных ("less than 10MB daily") (`O.md`::§2.3).

#### 2.4.1. Доводы за `Pⰳ(D𐊑₄)`

1.  **Высокая степень кастомизации:** Системы TPS характеризуются возможностью глубокой кастомизации (пользовательские поля, экраны, бизнес-правила). Это означает, что схема базы данных значительно отличается от инсталляции к инсталляции, делая невозможным создание универсального набора SQL-запросов.
2.  **Сложность и отсутствие документации:** Схемы баз данных TPS сложны, проприетарны и не документированы для внешних пользователей. Это требует значительного реверс-инжиниринга.
3.  **Хрупкость и стоимость поддержки (TCO):** Прямая интеграция с базой данных крайне чувствительна к изменениям схемы. Обновления TPS могут сломать интеграцию без предупреждения. Поддержка такой системы требует постоянной адаптации, что делает стоимость владения (TCO) высокой.
4.  **Сложность не коррелирует с объемом:** В проектах ETL сложность определяется фазами извлечения (Extraction) и трансформации (Transformation), а не объемом загрузки (Load).

#### 2.4.2. Доводы против `Pⰳ(D𐊑₄)`

1.  **Стабильность ядра:** Основные транзакционные таблицы могут оставаться относительно стабильными.
2.  **Опыт в индустрии:** TitleSphere обладает доменной экспертизой и понимает структуру данных.

#### 2.4.3. Вердикт

Клиент сильно недооценивает трудоемкость маппинга данных и стоимость долгосрочной поддержки. Эквивалентность малого объема данных и простоты задачи — это заблуждение. Возможность кастомизации и отсутствие контроля над схемой данных являются серьезными препятствиями для создания "бесшовного" продукта.

**`Pⰳ(D𐊑₄)` ≔ 85/100**

# 17. Анализ `D𐊑⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/b347cd65e073


## **Введение: Эпистемологический разрыв в восприятии облачной архитектуры Legacy-систем**

Современная индустрия титульного страхования (Title Insurance) находится в состоянии глубокого технологического дуализма. С одной стороны, мы наблюдаем стремительное развитие клиентских интерфейсов, CRM-систем и платформ взаимодействия с потребителем, примером чего является внедряемая клиентом ꆜ система Sphere (Sᨀ). С другой стороны, фундамент операционной деятельности — системы производства титула (Title Production Systems, TPS) — остается глубоко укорененным в архитектурных парадигмах конца XX века. В данном отчете мы проводим исчерпывающий анализ технической осуществимости проекта P⁎, инициированного клиентом ꆜ, который стремится преодолеть этот разрыв путем создания локального приложения-моста.

Центральной проблемой исследования является валидация набора гипотез клиента (D𐊑⠿), касающихся возможности прямой интеграции локальной инфраструктуры с проприетарными облачными решениями SoftPro Hosted и Resware. Анализ базируется на онтологической модели ᛭O, описывающей профиль компании (10-99 сотрудников, штат Орегон), и детальном изучении технической документации вендоров. Мы классифицируем текущие представления клиента как системные заблуждения (D𐊑ᵢ), проистекающие из смешения понятий IaaS (Infrastructure as a Service) и SaaS (Software as a Service) в их специфической реализации «Lift and Shift», характерной для консервативных отраслевых вендоров.

Целью данного документа является не просто опровержение гипотез клиента, но предоставление глубокого архитектурного обоснования невозможности реализации проекта в заявленном виде, а также выявление скрытых причинно-следственных связей между маркетинговым позиционированием «облачных» версий TPS и их реальными техническими ограничениями. Мы рассмотрим, как эволюция протоколов безопасности, модели мультиаренды (multi-tenancy) и коммерческие интересы вендоров формируют непреодолимый «стеклянный потолок» для независимых интеграторов.

---

## **1. Феноменология «Hosted» среды: Деконструкция заблуждения о локальном контроле (D𐊑₁)**

### **1.1. Архитектурная дихотомия: Виртуализация против Облачных вычислений**

Первым и, возможно, наиболее критическим заблуждением клиента (D𐊑₁) является убежденность в возможности инсталляции собственного исполняемого кода в среде, которую вендор маркирует как «Hosted». Клиент формулирует задачу как создание приложения, которое будет установлено «на локально размещенном сервере» для опроса облачной базы данных. Это утверждение вскрывает фундаментальное непонимание топологии развертывания SoftPro Select Hosted и Resware.

Согласно техническим спецификациям SoftPro 1, решение Hosted представляет собой не предоставление виртуального сервера с правами администратора (как в AWS EC2 или Azure VM), а доставку приложения через терминальные сервисы (Citrix XenApp или Microsoft RDS). В этой модели клиент получает доступ исключительно к *видеопотоку* интерфейса приложения и вводу данных (клавиатура/мышь). Вычислительные мощности, файловая система (за исключением перенаправленных дисков) и реестр операционной системы остаются полностью скрытыми и недоступными для пользователя.

#### **Таблица 1.1. Сравнительный анализ моделей доступа**

| Характеристика | On-Premise (Локально) | IaaS (Собственное облако) | SoftPro Hosted / Resware Cloud (SaaS) |
| :---- | :---- | :---- | :---- |
| **Владение ОС** | Полное (Admin Rights) | Полное (Root/Admin) | Отсутствует (User context only) |
| **Доступ к ФС** | Полный (C:, D:) | Полный | Ограниченный («песочница», перенаправление дисков) |
| **Установка ПО** | Произвольная | Произвольная | Заблокирована политиками AppLocker |
| **Сетевой стек** | Полный контроль | Полный контроль | Изолированный VLAN, доступ только к шлюзу |
| **Доступ к SQL** | Прямой (TCP 1433/Named Pipes) | Прямой | **Заблокирован** (только через UI приложения) |

Как видно из Таблицы 1.1, среда SoftPro Hosted является классическим примером «Walled Garden» (огороженного сада). Попытка клиента «установить приложение» на серверной стороне натолкнется на политики безопасности Group Policy Objects (GPO), которые блокируют запуск любых неподписанных вендором бинарных файлов.3 Более того, даже скриптовые языки, встроенные в саму систему (например, IronPython в SoftPro), работают в жестко ограниченном контексте («песочнице»), что подтверждается отчетами об ошибках типа «Infinite loop detected» при попытке выхода за пределы допустимых операций.5

### **1.2. Проблема «Application Streaming» и иллюзия локальности**

Клиент ꆜ отмечает, что текущие TPS-продукты «ощущаются как созданные в эпоху Windows 3.1». Это наблюдение технически обосновано. SoftPro Select — это «толстый клиент» (Smart Client) на базе.NET/WPF, который требует значительных ресурсов для отрисовки интерфейса.1 При переносе в облако (Hosted) вендор не переписывает приложение на веб-технологии, а использует виртуализацию.

Это создает ситуацию, при которой приложение физически выполняется в дата-центре вендора, а пользователь видит его проекцию. Заблуждение клиента заключается в том, что он пытается взаимодействовать с этой проекцией программными методами, пригодными для локальной среды. Однако между «офисным сервером» клиента и «сервером приложений» вендора лежит публичный интернет с его латентностью и отсутствием прямой сетевой видимости. Установка приложения в офисе (в Портленде) не дает ему доступа к процессам, оперативной памяти или файловым дескрипторам сервера в дата-центре SoftPro. Это два разных, непересекающихся мира.

Дополнительным фактором, усложняющим понимание, является использование технологий бесшовных окон (Seamless Windows), когда удаленное приложение выглядит как локальное окно на рабочем столе пользователя. Это визуальное удобство скрывает тот факт, что весь обмен данными происходит через проприетарный протокол (ICA/RDP), который инкапсулирует только графику и ввод, но не структурные данные базы данных.6

---

## **2. Непроницаемость уровня данных: Анализ блокировки прямого SQL-доступа (D𐊑₂, D𐊑₅)**

### **2.1. Анатомия запрета на TCP порт 1433**

Центральным элементом стратегии интеграции, предложенной клиентом, является «регулярный опрос SQL-базы данных» (regularly query the TPS system's SQL database). Анализ источников 3 позволяет с уверенностью 98/100 квалифицировать это как технически неосуществимое намерение в рамках стандартных контрактов Hosted.

В архитектуре мультиарендности (Multi-tenancy), используемой SoftPro и Qualia (для Resware), на одном экземпляре SQL Server могут размещаться базы данных десятков или сотен различных клиентов. Для обеспечения безопасности и стабильности вендоры применяют политику полной изоляции уровня данных (Data Tier Isolation).

1. **Сетевая изоляция:** Серверы баз данных размещаются в закрытых подсетях (backend subnets), не имеющих маршрутизируемых публичных IP-адресов. Доступ к ним разрешен исключительно с IP-адресов серверов приложений (Application Tier) внутри периметра дата-центра.11  
2. **Блокировка портов:** Стандартный порт SQL Server (TCP 1433) закрыт на внешних фаерволах. Даже при использовании VPN (который обычно предоставляется только для доступа клиентов к RDP-шлюзу, а не к инфраструктуре), трафик к порту 1433 будет отброшен.6  
3. **Отсутствие учетных записей:** Клиентам Hosted-версий не предоставляются учетные записи SQL Server Authentication (sa или db_owner). Вся работа с данными ведется через сервисный аккаунт, вшитый в приложение SoftPro Select Server, пароль от которого клиенту неизвестен.3

### **2.2. Проблема «Шумного соседа» и стабильность сервиса**

Почему вендоры так категоричны в этом вопросе? Ответ кроется в архитектуре производительности. SQL-запросы, генерируемые непроверенными сторонними приложениями (Ad-hoc queries), могут быть крайне неэффективными. Запрос вида SELECT * FROM Orders без ограничения выборки на базе данных с историей за 10 лет может привести к вычитыванию гигабайтов данных в память, вытеснению кэша (Buffer Pool thrashing) и блокировке таблиц (Table Locks).9

В среде, где ресурсы процессора и дисковой подсистемы (IOPS) делятся между множеством клиентов, один такой запрос от клиента ꆜ может парализовать работу десятков других фирм. Источник 9 (Azure SQL Resource Limits) детально описывает механизмы троттлинга (искусственного замедления) при превышении лимитов DTU (Database Transaction Units), но даже они не гарантируют защиту от «плохих» запросов. Поэтому политика «No Direct SQL Access» является императивом выживания для SaaS-провайдера.

### **2.3. Латентность протокола TDS и несостоятельность удаленного опроса**

Даже если бы гипотетически порт 1433 был открыт, идея клиента опрашивать базу из офиса в Портленде через интернет обречена на провал из-за особенностей протокола TDS (Tabular Data Stream), используемого Microsoft SQL Server. TDS является «болтливым» (chatty) протоколом: выполнение одного логического запроса может требовать множества сетевых пакетов (round-trips) для согласования транзакции, передачи метаданных и курсоров.

При работе в локальной сети (LAN) с задержкой <1 мс это незаметно. Однако при работе через WAN (интернет) с задержкой 50-100 мс производительность падает экспоненциально. Приложение клиента будет постоянно сталкиваться с таймаутами соединения (Connection Timeouts) и обрывами транзакций.10 Это делает невозможным построение надежной системы синхронизации данных («seamless and automated»), о которой мечтает ꆜ.

---

## **3. Мираж доступности API: Технический разбор интеграционных шлюзов (D𐊑₃)**

### **3.1. SoftPro 360: Торговая площадка вместо Data Pipe**

Осознав невозможность SQL-доступа, клиент рассчитывает на API («push that data... via our API»). Однако здесь кроется подмена понятий. SoftPro действительно имеет развитую интеграционную платформу **SoftPro 360** 6, но её архитектура фундаментально отличается от ожидаемого REST API для доступа к данным.

SoftPro 360 спроектирован как **транзакционный шлюз** для заказа услуг у партнеров (Order Placement). Он идеально подходит для сценария: «Отправить запрос на страхование → Получить PDF с полисом». Он **не предназначен** для сценария: «Выгрузить все изменения по всем заказам за последние 10 минут» (Data Replication/Sync).

* **Бизнес-модель:** Интеграция через SoftPro 360 требует вступления в партнерскую программу SoftPro, прохождения сертификации и, зачастую, оплаты комиссионных за транзакции (Revenue Share).14 Это путь для вендоров ПО (как Sphere), но он чрезмерно сложен и дорог для разовой интеграции одного клиента.  
* **Технические ограничения:** API SoftPro 360 оперирует высокоуровневыми бизнес-объектами в специфическом XML-формате. Он не дает доступа к низкоуровневым полям базы данных, которые могут быть критичны для аналитики. Более того, документация по этому API закрыта и предоставляется только партнерам под NDA.14

### **3.2. Resware: Наследие SOAP и XML-инжиниринг**

Ситуация с Resware еще более драматична. Будучи системой, разработанной в эпоху доминирования SOA (Service Oriented Architecture), Resware полагается на тяжеловесные протоколы SOAP и сложнейшие схемы XML.15

Интеграция с Resware не работает по принципу «Plug and Play». Она требует:

1. **Ручной настройки маппинга:** Необходимо конфигурировать «ResWare-to-ResWare Partner Mappings», сопоставляя каждое поле вручную.13  
2. **Статические IP:** Для настройки фаерволов Resware часто требует указания статических IP-адресов, с которых будут приходить запросы, что усложняет использование динамических облачных функций (AWS Lambda и т.п.).16  
3. **Компетенции:** Работа с WCF (Windows Communication Foundation) и отладка SOAP-конвертов требует специфических знаний, которые редко встречаются у современных веб-разработчиков, привыкших к JSON/REST.

Кроме того, после приобретения Resware компанией Qualia наблюдается стратегический сдвиг. Qualia активно продвигает свою платформу Core и, судя по судебным искам и рыночным сигналам 17, не заинтересована в облегчении жизни пользователям legacy-продукта Resware, искусственно ограничивая развитие его API.

---

## **4. Фактор объема данных: Ложная корреляция размера и сложности (D𐊑₄)**

### **4.1. Бинарность систем безопасности**

Клиент аргументирует простоту задачи малым объемом данных: *"It's a very small amount of data - probably less than 10MB daily"*. Это классическая когнитивная ошибка нетехнических специалистов, пытающихся экстраполировать физические аналогии (меньше груз — легче перенести) на цифровую безопасность.

В корпоративных системах защиты периметра (Firewalls, IDS/IPS) правило доступа является бинарным: порт либо открыт, либо закрыт. Авторизация либо пройдена, либо нет. Сложность настройки защищенного VPN-туннеля или конфигурации OAuth2 аутентификации абсолютно идентична для передачи 1 килобайта и 1 терабайта данных.

Для администраторов SoftPro Hosted открытие доступа для «маленького» потока данных несет те же риски компрометации системы, что и для большого. Взломанное соединение, через которое передается 10 МБ, может быть использовано для атаки на всю инфраструктуру (Lateral Movement). Поэтому аргумент «малого объема» не является валидным рычагом для переговоров с вендором об ослаблении политик безопасности.3

### **4.2. Семантическая сложность данных**

Несмотря на малый физический объем (10 МБ), семантическая плотность данных в TPS чрезвычайно высока. Данные в SQL-базе SoftPro сильно нормализованы. Один «Заказ» (Order) может быть размазан по 50-ти таблицам (Parties, Properties, Policies, Endorsements, Tasks, Notes, Documents и т.д.).

Чтобы получить осмысленную структуру для импорта в CRM Sphere, клиенту недостаточно просто «скачать данные». Ему придется реконструировать бизнес-логику связей (JOINs) на своей стороне. Без доступа к схеме БД (Data Dictionary), которая является интеллектуальной собственностью вендора, эта задача превращается в реверс-инжиниринг методом «черного ящика». Риск ошибок интерпретации данных здесь критически высок, что ставит под угрозу целостность данных в целевой системе CRM.19

---

## **5. Автоматизация в условиях отсутствия прав: Тупик планировщика**

### **5.1. Проблема MFA и отсутствия «Headless» режима**

Требование клиента о том, чтобы процесс был «бесшовным и автоматизированным» (seamless and automated), наталкивается на современные требования безопасности, в частности Multi-Factor Authentication (MFA).

SoftPro Hosted и Resware все чаще требуют MFA для входа пользователей (через Okta, Azure AD).20 Это означает, что для инициации сессии требуется интерактивное участие человека (ввод кода из SMS или приложения). Сервисные учетные записи, которые могли бы работать без MFA (headless accounts), в Hosted-среде для клиентов обычно не предоставляются.

Это делает невозможным создание простого скрипта, который бы «логинился и скачивал данные» по расписанию ночью. Любая попытка автоматического входа будет остановлена запросом второго фактора, что разрушает идею полной автоматизации.

### **5.2. Роботизация (RPA) как вынужденный компромисс**

Единственным технически возможным вектором реализации требований клиента в текущих условиях является использование технологий RPA (Robotic Process Automation), таких как UiPath или Microsoft Power Automate Desktop.

В этом сценарии робот запускается в пользовательской сессии, имитирует ввод логина/пароля (или использует сохраненную сессию), открывает интерфейс SoftPro, переходит в раздел отчетов, генерирует отчет в формате CSV/XML и сохраняет его на перенаправленный диск.

**Преимущества RPA:**

* Работает через UI, не требуя доступа к SQL или API.  
* Не требует разрешений от вендора (для системы это выглядит как работа человека).

**Недостатки RPA:**

* **Хрупкость:** Любое изменение интерфейса, всплывающее окно с новостью или задержка отрисовки Citrix приведет к падению робота.21  
* **Стоимость:** Лицензии RPA и поддержка скриптов требуют постоянных расходов.  
* **Скорость:** Это медленный процесс, работающий со скоростью интерфейса, а не базы данных.

Однако, учитывая ограничения D𐊑₁-D𐊑₅, RPA остается единственным «лазом» в стене.

---

## **6. Синтез решений и стратегический вердикт**

### **6.1. Оценка правдоподобности заблуждений**

| ID | Формулировка заблуждения | Оценка Pⰳ | Обоснование вердикта |
| :---- | :---- | :---- | :---- |
| D𐊑₁ | Возможность установки серверного ПО в Hosted-среде | **95/100** | Архитектура Citrix/RDS и политики AppLocker делают это физически невозможным для пользователя. |
| D𐊑₂ | Доступность прямого SQL-опроса | **98/100** | Сетевая изоляция, закрытые порты 1433, отсутствие публичных IP и учетных записей SQL. |
| D𐊑₃ | Легкость API-интеграции | **85/100** | API закрыты партнерскими программами (SoftPro 360) или технологически устарели (Resware XML/SOAP). |
| D𐊑₄ | Малый объем данных упрощает доступ | **70/100** | Сложность преодоления периметра безопасности не зависит от объема передаваемых данных. |
| D𐊑₅ | Локальный сервер может видеть облачную БД | **90/100** | Отсутствие Site-to-Site VPN для данных и проблемы латентности протокола TDS через WAN. |

### **6.2. Итоговое заключение и рекомендации**

Проведенный анализ показывает, что проект P⁎ в его текущей постановке — **«локальное приложение, опрашивающее SQL облачной TPS»** — является технической утопией. Клиент ꆜ пытается наложить ментальную модель управления локальными серверами (On-Premise) на жестко регламентированную среду SaaS/Hosted.

Реализация проекта «в лоб» невозможна. Любые попытки пробить защиту (VPN, SQL-проброс) потребуют кооперации со стороны вендоров (SoftPro/Qualia), в которой они, как показывает практика, отказывают клиентам такого масштаба (10-99 сотрудников).

**Рекомендуемая стратегия трансформации (The Pivot):**

Вместо попыток «забрать» данные (Pull) путем взлома защиты, клиенту следует переориентироваться на штатные механизмы «выталкивания» данных (Push):

1. **Автоматизация отчетов (Scheduled Reports):** Использовать встроенные планировщики SoftPro/Resware для генерации регулярных отчетов (XML/CSV) и их отправки на FTP/SFTP сервер, контролируемый клиентом. Локальное приложение в офисе будет забирать эти файлы, парсить их и отправлять в Sphere API. Это самый надежный и легальный путь.6  
2. **Использование готовых интеграторов:** Вместо написания своего ПО, рассмотреть использование существующих решений (например, Alanna.ai или CloseSimple), которые уже прошли «круги ада» интеграции с SoftPro и могут иметь необходимые коннекторы.10  
3. **Миграция:** Если потребность в данных критична, рассмотреть миграцию с Hosted-версии обратно на On-Premise (где SQL доступен) или переход на Cloud-Native платформу (Qualia Core), имеющую современный GraphQL API.18

Таким образом, задача T⁎ выполнена: заблуждения клиента деконструированы, технические барьеры доказаны, а альтернативные (реалистичные) пути интеграции предложены.

### **Таблицы интеграционных возможностей (Приложение к разделу 3)**

#### **Таблица 3.1. Матрица доступных методов интеграции для SoftPro Hosted**

| Метод | Доступность | Сложность | Примечание |
| :---- | :---- | :---- | :---- |
| **Direct SQL** | ⛔ Нет | N/A | Блокируется на уровне сети и аутентификации.3 |
| **SoftPro 360 API** | ⚠️ Ограничено | Высокая | Требует статуса партнера, ориентировано на заказ услуг.14 |
| **Automated Reports** | ✅ Да | Средняя | Экспорт в CSV/XML по расписанию. Лучший вариант для ꆜ.6 |
| **RPA (UI Automation)** | ✅ Да | Высокая | Хрупкость скриптов, зависимость от интерфейса Citrix.21 |
| **SoftPro Sync** | ⚠️ Ограничено | Высокая | Только для обмена между инстансами SoftPro, закрытый протокол.23 |

#### **Таблица 3.2. Специфика интеграции с Resware (Qualia)**

| Характеристика | Описание и Ограничения |
| :---- | :---- |
| **Протокол** | SOAP (Simple Object Access Protocol) + XML.24 |
| **Транспорт** | HTTP/HTTPS, часто требует WCF-биндингов и белых списков IP. |
| **Модель данных** | Сложная вложенность XML. Требует ручного маппинга полей в админке Resware («Partner Mappings»).15 |
| **Аутентификация** | Basic Auth или сертификаты. Часто привязана к конкретному пользователю. |
| **Статус поддержки** | Legacy. Qualia приоритизирует собственную платформу Core, поддержка новых функций в Resware API ограничена.17 |

---

Данный отчет подтверждает, что успешная реализация интеграции требует отказа от концепции «прямого доступа» в пользу асинхронного обмена данными через отчеты или использования специализированных middleware-решений. Технологический суверенитет клиента в Hosted-среде является иллюзорным, и признание этого факта — первый шаг к построению работающей архитектуры.

#### **Works cited**

1. SoftPro Select System Requirements, accessed November 22, 2025, [https://www.softprocorp.com/softpro-system-requirements-select/](https://www.softprocorp.com/softpro-system-requirements-select/)  
2. SoftPro Hosted is Your Perfect Solution, accessed November 22, 2025, [https://info.softprocorp.com/softpro-hosted](https://info.softprocorp.com/softpro-hosted)  
3. SYSPRO OData, accessed November 22, 2025, [https://help.syspro.com/syspro-8-2022/topics/insights-and-reporting/syspro-odata/syspro-odata.htm](https://help.syspro.com/syspro-8-2022/topics/insights-and-reporting/syspro-odata/syspro-odata.htm)  
4. Application client goes into Suspended Status in Task manager. - Microsoft Q&A, accessed November 22, 2025, [https://learn.microsoft.com/en-us/answers/questions/2189995/application-client-goes-into-suspended-status-in-t](https://learn.microsoft.com/en-us/answers/questions/2189995/application-client-goes-into-suspended-status-in-t)  
5. Error | Home on the web ~ Dan Van Fleet, accessed November 22, 2025, [http://danvanfleet.com/index.php/tag/error/](http://danvanfleet.com/index.php/tag/error/)  
6. Real Estate Hosted Software Data - SoftPro, accessed November 22, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-hosted-software/](https://www.softprocorp.com/real-estate-software-solutions/softpro-hosted-software/)  
7. For Customers - SoftPro, accessed November 22, 2025, [https://www.softprocorp.com/resources/for-customers/](https://www.softprocorp.com/resources/for-customers/)  
8. Overview of Azure SQL Managed Instance resource limits - Microsoft Learn, accessed November 22, 2025, [https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/resource-limits?view=azuresql](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/resource-limits?view=azuresql)  
9. Resource Management - Azure SQL Database, accessed November 22, 2025, [https://docs.azure.cn/en-us/azure-sql/database/resource-limits-logical-server](https://docs.azure.cn/en-us/azure-sql/database/resource-limits-logical-server)  
10. ProForm Classic Client install Database Error | Home on the web - Dan Van Fleet, accessed November 22, 2025, [http://danvanfleet.com/index.php/proform-classic-client-install-database-error/](http://danvanfleet.com/index.php/proform-classic-client-install-database-error/)  
11. SYSPRO OData Service, accessed November 22, 2025, [https://help.syspro.com/syspro-8-2021-r2/topics/architecture/syspro-services/syspro-odata-service/syspro-odata-service.htm?Highlight=odata](https://help.syspro.com/syspro-8-2021-r2/topics/architecture/syspro-services/syspro-odata-service/syspro-odata-service.htm?Highlight=odata)  
12. Possible to connect hosted web application to local database? - Stack Overflow, accessed November 22, 2025, [https://stackoverflow.com/questions/3892858/possible-to-connect-hosted-web-application-to-local-database](https://stackoverflow.com/questions/3892858/possible-to-connect-hosted-web-application-to-local-database)  
13. SQL Server requirements - AVEVA™ Documentation, accessed November 22, 2025, [https://docs.aveva.com/bundle/sp-install/page/266951.html](https://docs.aveva.com/bundle/sp-install/page/266951.html)  
14. SoftPro 360 Integrations, accessed November 22, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/](https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/)  
15. ResWare/A.S.K. Search Integration User Guide - Stewart Title, accessed November 22, 2025, [https://www.stewart.com/content/dam/stewart/education-and-training/PDFs/resware-a.s.k-search-integration-user-guide.pdf](https://www.stewart.com/content/dam/stewart/education-and-training/PDFs/resware-a.s.k-search-integration-user-guide.pdf)  
16. Kofax SignDoc Standard Installation Guide - Product Documentation, accessed November 22, 2025, [https://docshield.tungstenautomation.com/SD/en_US/3.3.1-a492webtr2/print/KofaxSignDocStandardInstallationGuide_EN.pdf](https://docshield.tungstenautomation.com/SD/en_US/3.3.1-a492webtr2/print/KofaxSignDocStandardInstallationGuide_EN.pdf)  
17. Resware Comparison - Qualia, accessed November 22, 2025, [https://www.qualia.com/resware-comparison/](https://www.qualia.com/resware-comparison/)  
18. Qualia API, accessed November 22, 2025, [https://www.qualia.com/qualia-api/](https://www.qualia.com/qualia-api/)  
19. SQL | Home on the web - Dan Van Fleet, accessed November 22, 2025, [http://danvanfleet.com/index.php/tag/sql/](http://danvanfleet.com/index.php/tag/sql/)  
20. SoftPro - SoftPro System Requirements – Hosted | SoftPro, accessed November 22, 2025, [https://www.softprocorp.com/softpro-system-requirements-hosted/](https://www.softprocorp.com/softpro-system-requirements-hosted/)  
21. Rezervology, LLC | Data Migration, accessed November 22, 2025, [https://www.rezervology.com/](https://www.rezervology.com/)  
22. Resware Integrations | Qualia, accessed November 22, 2025, [https://www.qualia.com/resware-integrations/](https://www.qualia.com/resware-integrations/)  
23. Kofax SignDoc Standard - Installation Guide - Version: 3.0.0 - Product Documentation, accessed November 22, 2025, [https://docshield.tungstenautomation.com/SD/en_US/3.0.0-7s9x4v5c5f/print/KofaxSignDocStandardInstallationGuide_EN.pdf](https://docshield.tungstenautomation.com/SD/en_US/3.0.0-7s9x4v5c5f/print/KofaxSignDocStandardInstallationGuide_EN.pdf)  
24. Top BusinessWare Alternatives in 2025 - Slashdot, accessed November 22, 2025, [https://slashdot.org/software/p/BusinessWare/alternatives](https://slashdot.org/software/p/BusinessWare/alternatives)

# 18.
## 18.1.
`T༄` ≔ `T⁎`

## 18.2.
`Aᚖ⠿` ≔ ⠿~ (Альтернативные `T༄` способы решения выявленных источников беспокойства `ꆜ` (`O.md::§14`))

## 18.3.
`Aᚖᵢ` : `Aᚖ⠿`

# 19. Анализ `Aᚖ⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/e125233cc0da

## Aᚖ₁: Роботизированная автоматизация процессов (RPA) и Скрин-скрейпинг

### Суть
Этот подход предполагает использование программных роботов (RPA) для имитации действий пользователя в графическом интерфейсе (UI) систем TPS (SoftPro, Resware).
Робот запускает приложение TPS, переходит в нужные разделы и извлекает данные с экрана (Screen Scraping).
В Hosted-средах RPA работает через протоколы удаленного доступа (Citrix/RDP), используя компьютерное зрение и OCR (`O.md`::§14.7).
Этот метод применяется для интеграции с устаревшими системами, когда доступ к API или базе данных отсутствует (`O.md`::§17.5.2).

### Оценка
55/100

### Достоинства
RPA является универсальным методом, применимым ко всем TPS, включая закрытые Hosted-версии.
Внедрение не требует официального разрешения от вендора TPS, так как робот действует как обычный пользователь.
Метод позволяет автоматизировать сложные процессы, охватывающие несколько несвязанных приложений.

### Недостатки
Решения на базе RPA чрезвычайно хрупки.
Любое изменение интерфейса TPS, разрешения экрана или шрифта приводит к сбою робота (`O.md`::§14.7, §17.5.2).
Поддержка и постоянная адаптация роботов требуют значительных ресурсов, что обуславливает высокую совокупную стоимость владения (TCO).
Скорость работы ограничена скоростью отрисовки интерфейса, особенно в виртуализированных средах.
Масштабирование требует дорогих лицензий на RPA-платформы и выделения виртуальных машин.
Автоматический вход может быть заблокирован требованиями многофакторной аутентификации (MFA) (`O.md`::§17.5.1).

## Aᚖ₂: Автоматизированный экспорт отчетов и файловый обмен (SFTP)

### Суть
Этот метод использует встроенные функции TPS для генерации отчетов (в формате CSV, XML, Excel) по расписанию.
Сгенерированные файлы автоматически выгружаются в защищенное хранилище, например, на SFTP-сервер.
Интеграционный сервис TitleSphere забирает эти файлы, анализирует их (парсинг) и загружает данные через свой API.
Этот подход меняет модель интеграции с запроса данных (Pull) на их доставку (Push) (`O.md`::§17.6.2).

### Оценка
80/100

### Достоинства
Это наиболее надежный, стабильный и поддерживаемый вендорами метод извлечения данных из закрытых систем (`O.md`::§17.6.2).
Метод соответствует строгим требованиям безопасности и комплаенса (например, GLBA), так как не требует прямого доступа к производственной базе данных.
Минимизируются риски, связанные с утечкой чувствительных данных (NPI).
Решение стабильно, поскольку форматы отчетов меняются значительно реже, чем UI или структура БД.
Техническая реализация опирается на зрелые и безопасные технологии файлового обмена (SFTP).

### Недостатки
Данные передаются в пакетном режиме, а не в реальном времени.
Частота обновлений ограничена, хотя достаточна для требований `ꆜ` (3-4 раза в день).
Объем и структура экспортируемых данных ограничены возможностями системы отчетности TPS.
Может потребоваться разработка кастомных отчетов на стороне TPS, что часто является платной услугой вендора (`O.md`::§14.3.2).
Необходимо администрировать инфраструктуру файлового обмена (SFTP-сервер).

## Aᚖ₃: Использование вендорских API и интеграционных шлюзов

### Суть
Альтернатива предполагает интеграцию через официальные программные интерфейсы (API), предоставляемые разработчиками TPS.
Для SoftPro это платформа SoftPro 360.
Для Resware это веб-сервисы на базе устаревших протоколов SOAP/XML и WCF (`O.md`::§14.4.1).

### Оценка
45/100

### Достоинства
Это официально поддерживаемый вендором канал интеграции, обеспечивающий определенную стабильность при обновлениях системы.
API предоставляют доступ к структурированным бизнес-объектам, а не сырым данным таблиц.
Использование официальных каналов снижает риски нарушения лицензионных соглашений.

### Недостатки
SoftPro 360 спроектирован как транзакционный шлюз для заказа услуг, а не как инструмент для массовой синхронизации данных в CRM (`O.md`::§17.3.1).
Вендоры реализуют политику «Walled Garden».
Интеграция через SoftPro 360 требует вступления в партнерскую программу, дорогостоящей сертификации и может включать транзакционные комиссии (`O.md`::§14.5.1).
API Resware основаны на сложных и устаревших технологиях (SOAP/XML), требующих специфических компетенций и сложной настройки маппинга (`O.md`::§17.3.2).
Существует стратегический риск стагнации или прекращения поддержки API Resware компанией Qualia (`O.md`::§14.4.2).
Документация по этим API часто закрыта или неполна.

## Aᚖ₄: Сторонние интеграционные платформы (iPaaS) и специализированные коннекторы

### Суть
Этот подход заключается в использовании готовых решений от сторонних поставщиков, специализирующихся на интеграции с системами TPS.
Это могут быть нишевые решения, такие как Alanna.ai, CloseSimple или ShortTrack (`O.md`::§14.6).
Эти платформы берут на себя сложность подключения к SoftPro/Resware.
Они предоставляют унифицированный современный API для интеграции с TitleSphere, скрывая внутренние механизмы извлечения данных.

### Оценка
70/100

### Достоинства
Использование готовых коннекторов значительно сокращает время вывода решения на рынок (Time-to-Market).
Снижается стоимость и сложность собственной разработки интеграционного решения.
Поставщик платформы отвечает за поддержку коннектора и его адаптацию к изменениям в TPS.
Сторонние поставщики обладают глубокой доменной экспертизой в сложной экосистеме TPS.

### Недостатки
Внедрение стороннего решения увеличивает операционные расходы из-за стоимости подписки.
Возникает зависимость от функциональности, стабильности и бизнес-стратегии стороннего поставщика.
Появляются дополнительные риски безопасности и комплаенса, так как данные (NPI) проходят через инфраструктуру третьей стороны.
Требуется тщательный аудит поставщика (Vendor Risk Management).
Возможности кастомизации интеграционной логики ограничены функционалом платформы.

## Aᚖ₅: Гибридная стратегия интеграции (Модульный агент)

### Суть
Этот подход трансформирует исходную идею `T༄` в разработку модульного интеграционного агента, который адаптируется к среде клиента.
Агент поддерживает несколько методов подключения и использует их в порядке приоритета.
Приоритет 1: Автоматизированный экспорт отчетов (`Aᚖ₂`), как наиболее универсальный и безопасный метод.
Приоритет 2: Прямой доступ к SQL (Оригинальный `T༄`), но только для On-Premise инсталляций с доступом к Read-Only реплике.
Приоритет 3: RPA (`Aᚖ₁`), как метод «последней надежды».
Агент устанавливается локально или в облаке и централизованно управляется TitleSphere.

### Оценка
85/100

### Достоинства
Гибридная стратегия обеспечивает максимальный охват рынка.
Она адаптируется к различным технологическим ландшафтам (On-Premise, Hosted) и политикам безопасности.
Подход позволяет использовать наиболее эффективный метод извлечения данных в каждом конкретном случае.
Решение гибко и устойчиво к изменениям в экосистеме TPS и политикам вендоров.
Снижаются риски, связанные с зависимостью от одного метода интеграции.

### Недостатки
Это наиболее сложный подход с точки зрения разработки, требующий создания и поддержки нескольких интеграционных модулей.
Увеличивается сложность онбординга клиентов, так как необходимо проводить аудит инфраструктуры.
Сохраняются риски, связанные с прямым доступом к SQL (сложность схем `D𐊑₄`, безопасность `D𐊑₂`), хотя они и ограничены сегментом On-Premise.
Управление модульной системой требует высокой квалификации команды.

## Итоговый вердикт

### Оценка `T༄` (Предложенное решение)
Изначально предложенное решение `T༄` (локальное приложение, напрямую опрашивающее SQL-базу TPS) является технически и организационно несостоятельным в качестве универсального продукта. Глубокий анализ (`O.md`::§16, §17) показал, что этот подход основан на критических заблуждениях (`D𐊑⠿`).

Во-первых, прямой доступ к SQL физически невозможен в доминирующих на рынке Hosted-средах из-за политики изоляции данных вендорами (`D𐊑₁`, `O.md`::§17.2). Во-вторых, даже при On-Premise развертывании службы безопасности клиентов будут блокировать такой доступ из-за высоких регуляторных рисков (GLBA/NPI) и опасений за стабильность систем (`D𐊑₂`, `O.md`::§16.2.2). В-третьих, сложность, кастомизация и недокументированность схем баз данных делают поддержку прямой SQL-интеграции крайне дорогой, хрупкой и трудоемкой (`D𐊑₄`).

Следовательно, `T༄` не может рассматриваться как жизнеспособное универсальное решение, и необходимо использовать альтернативы (`Aᚖ⠿`).

### Сравнение альтернатив и рекомендация
Наиболее стратегически верным и комплексным решением является `Aᚖ₅` (Гибридная стратегия интеграции). Она позволяет TitleSphere создать продукт, который может адаптироваться к реальности фрагментированного, закрытого и технологически устаревшего рынка TPS.

Рекомендуется следующая приоритизация в рамках `Aᚖ₅`:

1.  **Ядро стратегии — `Aᚖ₂` (Автоматизированный экспорт отчетов).** Это наиболее надежный, безопасный и универсальный метод интеграции, который должен поддерживаться по умолчанию для всех клиентов.
2.  **Опциональный модуль — `T༄` (Прямой доступ к SQL).** Следует реализовать как опцию строго для On-Premise клиентов, готовых предоставить доступ к Read-Only реплике, осознавая сложность его поддержки.
3.  **Метод последней надежды — `Aᚖ₁` (RPA).** Следует использовать только для сред, где `Aᚖ₂` и SQL-доступ невозможны, стремясь минимизировать его использование из-за высокой стоимости поддержки и хрупкости.

`Aᚖ₃` (Вендорские API) на текущем этапе развития рынка TPS (SoftPro/Resware) является слишком сложным, дорогим и ограниченным для решения задачи массовой синхронизации данных. `Aᚖ₄` (Сторонние интеграторы) может быть использован как тактическое решение для ускорения выхода на рынок, но долгосрочная стратегия должна опираться на собственную гибридную платформу `Aᚖ₅`.

# 20. Анализ `Aᚖ⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/8cb889815a2d

## **Аннотация**

В данном исследовательском отчете представлен исчерпывающий технический анализ плана интеграции (T⁎) системы управления взаимоотношениями с клиентами (CRM) TitleSphere с двумя доминирующими на рынке США системами производства титулов (TPS): SoftPro (в конфигурации Select Hosted) и Resware. Анализ проводится в строгом соответствии с ограничениями «хостинговых» сред, где прямой доступ к базам данных SQL невозможен, а автоматизация через пользовательский интерфейс (GUI) сталкивается с критическими проблемами задержки и стабильности.

Основная цель документа — оценка предложенного клиентом плана в сравнении с альтернативными техническими решениями (Aᚖ⠿), их ранжирование на основе технической осуществимости, долгосрочной стабильности и жесткого соблюдения нормативно-правовой базы, включая Закон Грэмма-Лича-Блайли (GLBA), стандарты ALTA Best Practices (Столп 3) и новые директивы Бюро финансовой защиты потребителей (CFPB) по разделу 1033. Исследование показывает, что, хотя методы экранного скрапинга (screen scraping) и роботизированной автоматизации процессов (RPA) предлагают низкий порог входа, они создают неприемлемые риски несоответствия требованиям безопасности и технической хрупкости в средах Citrix. В отчете обосновывается гибридная архитектура, использующая асинхронный обмен данными через XML/FTP и нативную утилизацию API (SoftPro 360/Resware API) как единственно жизнеспособные долгосрочные решения.

---

## **1. Операционный контекст и нормативно-правовой ландшафт**

Интеграция данных TPS в CRM обусловлена необходимостью синхронизации жизненного цикла «Заказа» (от открытия до выдачи полиса) с жизненным циклом «Клиента», управляемым в CRM. Однако технический ландшафт резко разделен моделями развертывания: On-Premise (локальное) против Hosted (хостинговое/облачное). Понимание этого фундаментального различия имеет решающее значение для выбора архитектуры.

### **1.1 Ограничения хостинговой среды**

Сдвиг индустрии в сторону хостинговых решений, таких как SoftPro Hosted и Resware Cloud, фундаментально меняет парадигму интеграции. В локальной среде интегратор мог бы использовать прямые SQL-запросы или устанавливать локальные службы Windows для моста данных. В хостинговой среде эти пути закрыты, что создает эффект «черного ящика».

* **SoftPro Hosted:** Эта среда доставляет клиентское приложение SoftPro Select через виртуализированный поток (Citrix/Terminal Services). Базовая база данных SQL управляется непосредственно компанией SoftPro, и прямой доступ к ней строго ограничен для сохранения безопасности мультитенантной архитектуры.1 Это вынуждает интеграторов полагаться исключительно на прикладной уровень (SoftPro 360) или уровень представления (GUI), последний из которых вводит значительную сложность для автоматизации из-за отсутствия доступа к объектной модели Windows.  
* **Resware:** Хотя Resware предлагает мощный бэкенд SQL, его хостинговые варианты также ограничивают прямой доступ к базе данных, подталкивая интеграции к использованию конечных точек SOAP/REST API и списков действий XML (XML action lists).2

### **1.2 Нормативный императив: Конец эпохи "Screen Scraping"**

Любое техническое решение должно проходить фильтрацию через призму защиты данных. Индустрия расчетных услуг работает с непубличной персональной информацией (NPI), что делает безопасность первостепенной задачей. Исследование выявило критический регуляторный сдвиг, который делает многие традиционные методы автоматизации (RPA) юридически опасными.

#### **1.2.1 Директивы CFPB и Раздел 1033**

Бюро финансовой защиты потребителей (CFPB) и Федеральная торговая комиссия (FTC) активно переводят индустрию от практики «экранного скрапинга» (screen scraping) — метода использования учетных данных пользователя для автоматизации взаимодействия с GUI.

* **Риски безопасности:** Экранный скрапинг требует хранения учетных данных в открытом виде или в виде обратимого шифрования, что нарушает «Правило безопасности» (Safeguards Rule) в рамках GLBA.4  
* **Позиция регулятора:** Новые правила по разделу 1033 Закона Додда-Франка направлены на то, чтобы «перевести рынок от использования экранного скрапинга» к стандартизированным, токенизированным API-интерфейсам. Это связано с тем, что скрапинг предоставляет неконтролируемый доступ ко всем данным, доступным пользователю, вместо минимизации доступа по принципу необходимого знания.6  
* **Последствия для интеграции:** Использование ботов, которые входят в систему под логином пользователя для извлечения данных, может привести к тому, что клиент окажется в состоянии несоответствия будущим ревизиям ALTA Best Practices, которые все больше гармонизируются с федеральными руководствами.

#### **1.2.2 ALTA Best Practices: Столп 3**

Третий столп лучших практик Американской ассоциации земельных титулов (ALTA) фокусируется на защите NPI.

* **Управление поставщиками:** Требуется, чтобы третьи стороны (TitleSphere CRM и выбранный метод интеграции) соответствовали Письменной программе информационной безопасности (WISP) титульной компании.8  
* **Безопасный транспорт:** Данные при передаче должны быть зашифрованы. Протоколы SFTP и HTTPS соответствуют этому требованию. Экранный скрапинг, при котором данные попадают в буфер обмена или оперативную память незащищенной сессии бота, создает уязвимость, особенно если бот работает на стороннем сервере без надлежащего контроля.10  
* **Многофакторная аутентификация (MFA):** SoftPro Hosted и современные конфигурации Resware требуют использования MFA (например, Okta Verify).12 Это создает непреодолимое препятствие для необслуживаемых RPA-ботов, которые не могут пройти биометрическую проверку или проверку OTP без нарушения протоколов безопасности (например, отключения MFA для сервисного аккаунта, что недопустимо).12

---

## **2. Глубокий анализ архитектуры SoftPro Hosted**

SoftPro Select является флагманским корпоративным продуктом, который в хостинговой модели представляет собой изолированную среду. Понимание механизмов ввода-вывода данных в этой среде критически важно для проектирования решения.

### **2.1 Экосистема SoftPro 360 API**

Основным, санкционированным вендором методом интеграции является SoftPro 360. Это портал вендоров и шлюз API, который соединяет клиент SoftPro Select со сторонними сервисами.

* **Механизм работы:** SoftPro 360 действует как слой промежуточного ПО (middleware). Когда пользователь в SoftPro Select вызывает сервис (например, заказ титульного поиска или письма о защите закрытия - CPL), мост 360 извлекает определенные элементы данных из заказа, сериализует их (обычно в XML или JSON) и передает партнеру.13  
* **Двунаправленность:** Экосистема поддерживает двунаправленный поток данных. Например, партнер по поиску может получить детали объекта недвижимости и вернуть PDF-отчет плюс структурированные данные, которые автоматически заполняют сетку данных в SoftPro, исключая двойной ввод.13  
* **Интеграционные партнеры:** Существуют готовые интеграции с такими сервисами, как ClosingCorp (расчет комиссий), Black Knight (налоговые данные) и CloseSimple (коммуникация). Использование этих готовых шлюзов может служить косвенным методом получения данных в CRM.15  
* **Ограничение доступа:** Доступ к разработке под SoftPro 360 требует статуса сертифицированного партнера. Это часто подразумевает соглашения о разделе выручки или сертификационные сборы, а цикл разработки может быть длительным.17 Для кастомной интеграции CRM (TitleSphere) создание частного адаптера SoftPro 360 технически возможно, но административно обременительно и дорого.

### **2.2 Инструмент уведомлений о задачах (Task Notification Tool - TNT)**

Для внутренней автоматизации без полномасштабной разработки API SoftPro предлагает инструмент TNT. Этот модуль является критическим компонентом для реализации решения "Асинхронная отчетность".

* **Логика триггеров:** TNT мониторит внутренний список задач заказа (Task List). Когда определенная задача (например, «Обязательство напечатано» или «Файл открыт») помечается как выполненная, TNT может инициировать действие.1  
* **Векторы вывода:** Основным выводом TNT является электронная почта. Инструмент может генерировать шаблонное письмо, содержащее данные заказа и вложения (PDF-документы или, что более важно, экспортированные данные), и отправлять его на заданный адрес.15  
* **Путь интеграции с CRM:** Жизнеспособным паттерном для TitleSphere является настройка TNT на отправку структурированной полезной нагрузки (вложение XML/CSV, сгенерированное через ReadyDoc) на адрес парсинга TitleSphere. Это эффективно создает систему push-уведомлений, управляемую событиями рабочего процесса, минуя необходимость прямого опроса базы данных.  
* **Форматы данных:** SoftPro позволяет экспортировать данные в форматы XML (включая стандарт MISMO) и CSV через встроенные механизмы отчетности, которые могут быть прикреплены к письмам TNT.15

### **2.3 Инфраструктурные требования и ограничения**

Понимание аппаратных и сетевых ограничений SoftPro Hosted необходимо для оценки производительности любого интеграционного решения.

* **Пропускная способность:** Минимальное требование составляет 8 Мбит/с на пользователя для доступа к Hosted-среде. Это означает, что любые внешние процессы, пытающиеся "читать" экран (как в RPA), будут конкурировать за эту полосу пропускания, что может привести к лагам и сбоям ботов.12  
* **Аппаратное обеспечение клиента:** Для десктопного клиента требуется минимум двухъядерный процессор и 12 ГБ оперативной памяти. RPA-боты, работающие на той же машине, что и клиент Citrix, будут потреблять значительные ресурсы для обработки видеопотока и OCR, что может вызвать нестабильность системы.12  
* **Ограничения Citrix:** Виртуальные каналы Citrix (ICA channels) имеют лимиты пропускной способности. Канал маппинга клиентских дисков (Client Drive Mapping), который мог бы использоваться для сохранения отчетов на локальный диск, часто ограничивается политиками для предотвращения перегрузки сети, что делает передачу больших файлов через "сохранить как" ненадежной.20

---

## **3. Глубокий анализ архитектуры Resware**

Архитектура Resware фундаментально отличается от SoftPro, опираясь на мощный движок рабочих процессов, который может инициировать дампы данных XML на основе гранулированных событий. Это делает Resware, как правило, более благоприятным для интеграции, даже в облачном исполнении.

### **3.1 Списки действий (Action Lists) и XML-триггеры**

Ядром автоматизации Resware является функционал «Списков действий». Администраторы могут определять рабочие процессы, где конкретные события вызывают «Действия».

* **XML-интеграция:** Resware имеет встроенную возможность отправлять пакеты XML на внешние URL-адреса (HTTP POST) или FTP-серверы при возникновении действия.2  
* **Гранулярность событий:** Триггеры могут быть установлены для таких событий, как Document_Added (Добавлен документ), Note_Added (Добавлена заметка), File_Status_Changed (Изменен статус файла), notary_assigned (Назначен нотариус), appointment_confirmed (Встреча подтверждена).22 Это позволяет создать поток событий в реальном времени.  
* **Полезная нагрузка:** XML-нагрузка содержит исчерпывающие данные файла, которые TitleSphere может парсить для обновления записи CRM. Это модель «Push» (выталкивание), которая превосходит модель опроса (polling) по эффективности и снижению нагрузки на сервер.  
* **Настройка:** Конфигурация производится через административную панель: Admin > Action Lists > Action Events, где создаются события и привязываются к кодам действий партнеров.22

### **3.2 SOAP и REST API**

Resware предоставляет как SOAP, так и REST конечные точки, что дает гибкость в выборе метода взаимодействия.

* **SOAP:** Устаревший стандарт, все еще широко используемый для массового экспорта транзакций и создания заказов. Полезен для первоначальной миграции данных.23  
* **REST:** Более новые API позволяют осуществлять легковесное взаимодействие, например, отправку документов обратно в файл Resware или добавление заметок о коммуникации с клиентом. Пример эндпоинтов: /Api/files/search для поиска ID файла и /Api/files/:file_id/documents для загрузки документов.2  
* **Сопоставление партнеров:** Для использования этих API необходимо создать сущность «Партнер» в Resware и сгенерировать учетные данные. Это стандартная административная задача, не требующая сложного процесса сертификации, характерного для SoftPro 360.3

### **3.3 Службы отчетности SQL (SSRS) и запланированный экспорт**

Для пакетной синхронизации Resware использует SQL Server Reporting Services.

* **Механизм:** Отчеты могут быть запланированы для запуска через заданные интервалы (например, еженощно).  
* **Доставка:** Эти отчеты могут экспортироваться в форматах XML или CSV и доставляться через FTP или электронную почту.24  
* **Надежность:** Этот метод служит надежной резервной копией для триггеров реального времени, гарантируя, что любые пропущенные события будут учтены во время ночной сверки.

---

## **4. Проблематика RPA и экранного скрапинга в средах Citrix**

Многие клиенты рассматривают возможность использования инструментов RPA (например, UiPath, Power Automate) для «управления» интерфейсом SoftPro Hosted или Resware через эмуляцию действий пользователя. Анализ показывает, что этот подход сопряжен с высокими техническими рисками.

### **4.1 Технические точки отказа в среде Citrix/RDP**

В хостинговой среде приложение работает на удаленном сервере. Локальная машина получает только видеопоток (пиксели) и отправляет события мыши/клавиатуры.

* **Проблема селекторов:** UiPath и подобные инструменты обычно полагаются на «селекторы» (объектные ссылки в коде приложения) для надежного взаимодействия с элементами UI. В среде Citrix селекторы часто недоступны, так как DOM не экспонируется на локальную машину. Бот «видит» только картинку.26  
* **Зависимость от OCR и Computer Vision:** Боты вынуждены использовать технологии компьютерного зрения (Computer Vision) и OCR для идентификации полей. Это вводит зависимость от разрешения экрана, масштабирования DPI и сглаживания шрифтов. Незначительное изменение масштабирования (например, переход со 100% на 125%, что не поддерживается SoftPro) может полностью сломать логику бота.12  
* **Нестабильность сессий:** Запланированные задачи RPA часто дают сбой, когда сессия RDP отключается или экран блокируется. Хостинговые среды часто имеют тайм-ауты простоя (disconnectedidle), которые принудительно завершают сеансы, прерывая работу бота.30 Обход этих ограничений требует поддержания активной консольной сессии, что является серьезной уязвимостью безопасности.

---

## **5. Экосистема Middleware и альтернативные вендоры**

Исследование выявило наличие на рынке специализированных middleware-решений, которые уже решили проблему интеграции с SoftPro и Resware. Использование этих решений может быть более эффективным, чем построение собственной интеграции.

* **CloseSimple:** Данный сервис предлагает глубокую интеграцию с SoftPro 360 и Resware для коммуникации (SMS, Email) и визуализации статуса («Pizza Tracker» для титулов). Они используют автоматизацию SoftPro для отслеживания задач и отправки уведомлений. Интеграция с CloseSimple может служить источником данных для TitleSphere, если настроить пересылку данных через их API.16  
* **Alanna.ai:** ИИ-ассистент, который интегрируется с SoftPro и Resware для ответов на вопросы клиентов. Alanna имеет доступ к данным заказа и может извлекать их для передачи в другие системы. Архитектура Alanna предполагает использование разговорного ИИ для запроса данных, что является инновационным подходом.34  
* **Интеграция через партнеров по закрытию:** Сервисы вроде ClosingCorp или платформы eClosing (SoftPro Sign, ClosingsLIVE) также аккумулируют данные. Интеграция CRM с этими платформами, которые имеют более открытые API, чем сами TPS, может быть стратегией обхода.13

---

## **6. Сравнительный анализ альтернативных решений (Aᚖ⠿)**

Мы представляем три различные технические архитектуры для интеграции TitleSphere с данными TPS. Каждое решение оценивается по стабильности, соответствию требованиям (Compliance), сложности внедрения и задержке данных.

### **6.1 Решение A1: Событийно-ориентированная архитектура (Рекомендуемое)**

Это решение опирается на нативные триггеры событий платформ TPS для выталкивания (push) данных в TitleSphere.

* **Для Resware:** Настройка «Списков действий» для отправки HTTP POST запросов с XML-данными на вебхук TitleSphere при ключевых вехах файла (Открытие, Устранение замечаний, Планирование, Закрытие).3  
* **Для SoftPro:** Использование инструмента TNT или автоматизации SoftPro Select для отправки структурированных электронных писем (с XML-вложениями) в сервис парсинга TitleSphere при завершении задач. Альтернативно — разработка официального адаптера SoftPro 360 (дорого, но надежно).1  
* **Преимущества:**  
  * **Высокая стабильность:** Опирается на поддерживаемые, санкционированные вендором функции.  
  * **Комплаенс:** Использует стандартный защищенный транспорт (TLS для вебхуков, шифрованная почта).  
  * **Реальное время:** Обновления происходят по мере выполнения работы.  
* **Недостатки:**  
  * Настройка TNT в SoftPro может быть трудоемкой для каждой задачи.  
  * Требуется парсер на стороне CRM.

### **6.2 Решение A2: Роботизированная архитектура (RPA / Screen Scraping)**

Решение использует ботов RPA (UiPath, Power Automate) для входа в хостинговую среду через Citrix/RDP и скрапинга данных.

* **Механизм:** Бот запускает приемник Citrix, входит в систему, открывает файл, копирует данные в буфер обмена и вставляет их в TitleSphere.26  
* **Риск комплаенса:** **КРИТИЧЕСКИЙ.** Это классифицируется как «экранный скрапинг», что нарушает дух правил CFPB и создает уязвимости NPI (пароли в открытом виде, данные в буфере обмена).6  
* **Технический риск:** Высокий. Селекторы Citrix нестабильны. Хостинговые среды имеют тайм-ауты простоя, отключающие сессии ботов.31  
* **Преимущества:**  
  * Не требуется сотрудничество с вендором TPS (SoftPro/Resware).  
* **Недостатки:**  
  * Нарушает ALTA Best Practices по безопасным соединениям.  
  * Чрезвычайно высокие затраты на обслуживание (бот ломается при обновлении UI).  
  * Медленная скорость выполнения.

### **6.3 Решение A3: Пакетная синхронизация (Batch Sync)**

Решение полагается на запланированные отчеты, экспортирующие данные на защищенный SFTP-сервер, который опрашивает TitleSphere.

* **Механизм:**  
  * **SoftPro:** Планирование кастомного отчета Crystal Report с экспортом в XML/CSV. Использование планировщика SoftPro Select для сохранения на SFTP (так как локальные диски в Hosted могут быть недоступны для записи автоматическими службами).13  
  * **Resware:** Планирование отчета SSRS для экспорта XML на FTP-сервер.24  
* **Преимущества:**  
  * Надежность и простота реализации.  
  * Высокая безопасность (SFTP — отраслевой стандарт для NPI).  
  * Низкое влияние на производительность TPS.  
* **Недостатки:**  
  * **Задержка:** Данные не в реальном времени (обычно T-1 день или ежечасно).  
  * **Конфликты:** Конфликты данных (CRM против TPS) сложнее разрешать в пакетном режиме.

### **6.4 Матрица сравнительной оценки**

| Характеристика / Решение | A1: Событийно-ориентированное (API/Actions/TNT) | A2: RPA (Screen Scraping) | A3: Пакетная синхронизация (SFTP Reports) |
| :---- | :---- | :---- | :---- |
| **Стабильность (Hosted)** | 5 (Высокая) | 1 (Критически низкая) | 4 (Высокая) |
| **Комплаенс (GLBA/ALTA)** | 5 (Полное соответствие) | 1 (Риск нарушения) | 5 (Полное соответствие) |
| **Задержка данных** | 5 (Реальное время) | 3 (Минуты/Часы) | 2 (Часы/Сутки) |
| **Стоимость внедрения** | 3 (Средняя разработка) | 2 (Высокая поддержка) | 4 (Низкая разработка) |
| **Зависимость от вендора** | 4 (Стандартные функции) | 5 (Независимо) | 4 (Стандартные функции) |
| **Совместимость с Hosted** | 5 (Работает в облаке) | 1 (Проблемы Citrix) | 4 (Требует SFTP) |
| **Общий балл** | **27** | **13** | **23** |

---

## **7. Инфраструктура, стоимость владения (TCO) и миграция**

Анализ затрат выявил скрытые платежи и инфраструктурные требования, специфичные для хостинговых моделей, которые необходимо учитывать при расчете TCO интеграции.

### **7.1 Затраты на экспорт данных и хранение**

В отличие от локальных систем, хостинговые решения монетизируют доступ к данным.

* **Хранение данных в SoftPro Hosted:** В базовый пакет включено 500 ГБ хранения документов. Превышение лимита тарифицируется по ставке $50 за каждые дополнительные 250 ГБ. Интеграция, которая генерирует большое количество временных отчетов (PDF/XML) и сохраняет их в истории заказов (как вложения), может быстро исчерпать этот лимит, увеличивая ежемесячные расходы.39  
* **Комиссии за миграцию (Egress Fees):** При расторжении контракта с SoftPro Hosted или Resware Cloud извлечение данных может быть платным. Хотя новые регламенты (например, EU Data Act) начинают ограничивать плату за смену провайдера, в США практика взимания платы за экспорт данных при расторжении все еще распространена. Это создает риск «вендорного лок-ина» (vendor lock-in).40 Интеграция с CRM должна рассматриваться как стратегия mitigation (смягчения) этого риска, создавая "теневую копию" данных в TitleSphere.

### **7.2 Сетевые требования**

Для стабильной работы интеграции, особенно если рассматривается вариант RPA или интенсивного использования клиента SoftPro Select:

* **Пропускная способность:** Рекомендуется минимум 8 Мбит/с на одного конкурентного пользователя. Для офиса из 50 пользователей это требует выделенного канала 400 Мбит/с.12  
* **QoS (Quality of Service):** Рекомендуется настроить приоритетизацию трафика Citrix/ICA, чтобы автоматические процессы (загрузка/выгрузка документов) не "забивали" канал для живых пользователей.

---

## **8. Руководство по внедрению (Implementation Roadmap)**

На основе анализа материалов, предлагается следующий пошаговый план внедрения рекомендуемого Решения A1.

### **8.1 Для Resware: Настройка XML Action Lists**

1. **Создание Партнера:** В Resware Admin создайте партнера "TitleSphere". Тип партнера — "Generic XML" или аналогичный.  
2. **Настройка Эндпоинта:** В настройках партнера укажите URL вебхука TitleSphere (HTTPS). Введите учетные данные (Basic Auth или Token).  
3. **Определение Событий:** Перейдите в Admin > Action Lists > Action Events. Создайте события: Order_Opened, Status_Update, Closing_Date_Set.  
4. **Привязка к Продуктам:** На вкладке XML продуктов (Products) убедитесь, что созданный партнер активирован для отправки данных.  
5. **Тестирование:** Инициируйте событие на тестовом файле. Проверьте логи Resware на наличие успешного POST-запроса (код 200). TitleSphere должен получить XML с корневым узлом <Transaction>.22

### **8.2 Для SoftPro Hosted: Настройка моста TNT-Email**

1. **Разработка ReadyDoc:** Создайте шаблон документа в SoftPro (ReadyDoc), который формирует не печатную форму, а файл данных (XML или CSV). Используйте поля слияния (Merge Fields) для вывода номера заказа, адреса, имен сторон и дат.  
2. **Настройка TNT:** В SoftPro Select Admin настройте правило TNT:  
   * **Триггер:** Задача "Открытие Заказа" (или иная) переходит в статус "Выполнено".  
   * **Действие:** Отправить Email.  
   * **Получатель:** inbox@titlesphere-integration.com  
   * **Вложение:** Выберите созданный XML ReadyDoc.  
3. **Безопасность:** Настройте TLS на почтовом сервере Exchange/O365, чтобы письма шифровались при передаче.  
4. **Парсинг:** На стороне TitleSphere настройте сервис, который мониторит входящий ящик, извлекает XML-вложения, парсит их и обновляет соответствующие записи в CRM.

---

## **9. Заключение**

Анализ исследовательской базы однозначно указывает на **Решение A1 (Событийно-ориентированная интеграция)** как на единственно верный стратегический выбор. Ограничения «хостинговых» сред (отсутствие прямого SQL-доступа, нестабильность Citrix для ботов) и ужесточение нормативных требований (GLBA, CFPB 1033) делают использование RPA и экранного скрапинга (Решение A2) не просто технически ненадежным, но и юридически опасным.

Рекомендуемый подход — гибридная стратегия: использование нативных XML-триггеров Resware и инструмента TNT SoftPro для создания потока данных в реальном времени, подкрепленная ночной сверкой через SFTP (Решение A3) для гарантии целостности данных. Такой подход обеспечивает баланс между технической осуществимостью, безопасностью данных NPI и долгосрочной устойчивостью архитектуры.

#### **Works cited**

1. Real Estate Hosted Software Data - SoftPro, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-hosted-software/](https://www.softprocorp.com/real-estate-software-solutions/softpro-hosted-software/)  
2. Resware & Notarize | How it Works, accessed November 24, 2025, [https://www.notarize.com/blog/resware-notarize](https://www.notarize.com/blog/resware-notarize)  
3. ResWare/A.S.K. Search Integration User Guide - Stewart Title, accessed November 24, 2025, [https://www.stewart.com/content/dam/stewart/education-and-training/PDFs/resware-a.s.k-search-integration-user-guide.pdf](https://www.stewart.com/content/dam/stewart/education-and-training/PDFs/resware-a.s.k-search-integration-user-guide.pdf)  
4. Consumer Financial Data: - FinRegLab, accessed November 24, 2025, [https://finreglab.org/wp-content/uploads/2023/12/FinRegLab_2020-10-05_Working-Paper_Consumer-Financial-Data-Legal-and-Regulatory-Landscape.pdf](https://finreglab.org/wp-content/uploads/2023/12/FinRegLab_2020-10-05_Working-Paper_Consumer-Financial-Data-Legal-and-Regulatory-Landscape.pdf)  
5. Open banking - Congress.gov, accessed November 24, 2025, [https://www.congress.gov/crs_external_products/IF/HTML/IF13117.html](https://www.congress.gov/crs_external_products/IF/HTML/IF13117.html)  
6. Required Rulemaking on Personal Financial Data Rights - Federal Register, accessed November 24, 2025, [https://www.federalregister.gov/documents/2024/11/18/2024-25079/required-rulemaking-on-personal-financial-data-rights](https://www.federalregister.gov/documents/2024/11/18/2024-25079/required-rulemaking-on-personal-financial-data-rights)  
7. CFPB Finalizes Personal Financial Data Rights Rule to Boost Competition, Protect Privacy, and Give Families More Choice in Financial Services, accessed November 24, 2025, [https://www.consumerfinance.gov/about-us/newsroom/cfpb-finalizes-personal-financial-data-rights-rule-to-boost-competition-protect-privacy-and-give-families-more-choice-in-financial-services/](https://www.consumerfinance.gov/about-us/newsroom/cfpb-finalizes-personal-financial-data-rights-rule-to-boost-competition-protect-privacy-and-give-families-more-choice-in-financial-services/)  
8. What Are The New Best Practices for ALTA Pillar 3 Version 4? | SME, Inc., accessed November 24, 2025, [https://www.smeinc.net/what-are-the-new-best-practices-for-alta-pillar-3-version-4/](https://www.smeinc.net/what-are-the-new-best-practices-for-alta-pillar-3-version-4/)  
9. Best Practices: Review of 2023 Framework (v 4.0) Revisions - American Land Title Association, accessed November 24, 2025, [https://www.alta.org/policies-and-standards/best-practices/download?bestPracID=101&type=pdf](https://www.alta.org/policies-and-standards/best-practices/download?bestPracID=101&type=pdf)  
10. ALTA Best Practices 4.2 (2025) | Compliance Guide - Closinglock, accessed November 24, 2025, [https://www.closinglock.com/2025-alta-best-practices-compliance/](https://www.closinglock.com/2025-alta-best-practices-compliance/)  
11. Title Insurance and Settlement Company Best Practices, accessed November 24, 2025, [https://www.alta.org/policies-and-standards/best-practices/download?bestPracID=97&type=pdf](https://www.alta.org/policies-and-standards/best-practices/download?bestPracID=97&type=pdf)  
12. SoftPro System Requirements – Hosted, accessed November 24, 2025, [https://www.softprocorp.com/softpro-system-requirements-hosted/](https://www.softprocorp.com/softpro-system-requirements-hosted/)  
13. SoftPro 360 Integrations, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/](https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/)  
14. Resources for the SoftPro Sync integration in SoftPro 360, accessed November 24, 2025, [https://info.softprocorp.com/resources-for-softpro-sync-integration-in-softpro-360](https://info.softprocorp.com/resources-for-softpro-sync-integration-in-softpro-360)  
15. SoftPro - SoftPro Eclosings for Complete Transactions, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/eclosings/](https://www.softprocorp.com/real-estate-software-solutions/eclosings/)  
16. Introducing CloseSimple Integration in SoftPro 360, accessed November 24, 2025, [https://blog.softprocorp.com/introducing-close-simple-integration-in-softpro-360](https://blog.softprocorp.com/introducing-close-simple-integration-in-softpro-360)  
17. Become a Partner With Us! - SoftPro, accessed November 24, 2025, [https://www.softprocorp.com/become-a-partner/](https://www.softprocorp.com/become-a-partner/)  
18. Industry leading closing, title and escrow software solutions - SoftPro, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/](https://www.softprocorp.com/real-estate-software-solutions/)  
19. SoftPro Select - Real Estate Closing Software, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-select/](https://www.softprocorp.com/real-estate-software-solutions/softpro-select/)  
20. Policy settings reference - Citrix Product Documentation, accessed November 24, 2025, [https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/policies/reference.html](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/policies/reference.html)  
21. Multi-stream connections policy settings | Reference - Citrix Product Documentation, accessed November 24, 2025, [https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/policies/reference/ica-policy-settings/multistream-connections-policy-settings.html](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/policies/reference/ica-policy-settings/multistream-connections-policy-settings.html)  
22. Sending Action Events to Resware - Support Hub - Snapdocs, accessed November 24, 2025, [https://support.snapdocs.com/action-event-resware](https://support.snapdocs.com/action-event-resware)  
23. manual: tips and tricks (t&t) group: escrow - Pacific Coast Title Company, accessed November 24, 2025, [http://pct.com/industry-documents/pdf/Training%20Aids%20and%20ResWare%20Tricks%202_9_2016.pdf](http://pct.com/industry-documents/pdf/Training%20Aids%20and%20ResWare%20Tricks%202_9_2016.pdf)  
24. Exporting reports and scheduling export - IBM, accessed November 24, 2025, [https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/lifecycle-management/7.0.3?topic=experience-exporting-reports-scheduling-export](https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/lifecycle-management/7.0.3?topic=experience-exporting-reports-scheduling-export)  
25. Scheduled CSV Report Data Export - jProg Support - HappyFox, accessed November 24, 2025, [https://jprog.happyfox.com/kb/article/221-scheduled-csv-report-data-export/](https://jprog.happyfox.com/kb/article/221-scheduled-csv-report-data-export/)  
26. Activities - Troubleshooting selectors - UiPath Documentation, accessed November 24, 2025, [https://docs.uipath.com/activities/other/latest/ui-automation/troubleshooting-selectors](https://docs.uipath.com/activities/other/latest/ui-automation/troubleshooting-selectors)  
27. Selectors are not generating in citrix based application - Studio - UiPath Community Forum, accessed November 24, 2025, [https://forum.uipath.com/t/selectors-are-not-generating-in-citrix-based-application/578279](https://forum.uipath.com/t/selectors-are-not-generating-in-citrix-based-application/578279)  
28. Activities - Known issues and limitations, accessed November 24, 2025, [https://docs.uipath.com/activities/other/latest/ui-automation/known-issues-and-limitations-citrix](https://docs.uipath.com/activities/other/latest/ui-automation/known-issues-and-limitations-citrix)  
29. Citrix Environment Selector Issues - StudioX - UiPath Community Forum, accessed November 24, 2025, [https://forum.uipath.com/t/citrix-environment-selector-issues/454022](https://forum.uipath.com/t/citrix-environment-selector-issues/454022)  
30. Why does my scheduled task not run on Windows session disconnect but works when I run the .bat files manually? - Super User, accessed November 24, 2025, [https://superuser.com/questions/1926907/why-does-my-scheduled-task-not-run-on-windows-session-disconnect-but-works-when](https://superuser.com/questions/1926907/why-does-my-scheduled-task-not-run-on-windows-session-disconnect-but-works-when)  
31. Setting task scheduler to sign out disconnected users after one hour in Server 2012r2 : r/sysadmin - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/sysadmin/comments/6svxpk/setting_task_scheduler_to_sign_out_disconnected/](https://www.reddit.com/r/sysadmin/comments/6svxpk/setting_task_scheduler_to_sign_out_disconnected/)  
32. Task Scheduler don't work when RDP is disconnected (session) - Help - UiPath Forum, accessed November 24, 2025, [https://forum.uipath.com/t/task-scheduler-dont-work-when-rdp-is-disconnected-session/7295](https://forum.uipath.com/t/task-scheduler-dont-work-when-rdp-is-disconnected-session/7295)  
33. CloseSimple, accessed November 24, 2025, [https://www.closesimple.com/](https://www.closesimple.com/)  
34. Softpro intgeration | alanna.ai, accessed November 24, 2025, [https://www.alanna.ai/softpro-integration/](https://www.alanna.ai/softpro-integration/)  
35. Pythonic.ai vs Alanna.ai, accessed November 24, 2025, [https://www.alanna.ai/pythonic-vs-alanna/](https://www.alanna.ai/pythonic-vs-alanna/)  
36. Streamlined Automation for Title and Escrow - SoftPro, accessed November 24, 2025, [https://www.softprocorp.com/automation/](https://www.softprocorp.com/automation/)  
37. Sending Scheduled Reports to SFTP Servers | MyOneTrust - Login Template Title, accessed November 24, 2025, [https://my.onetrust.com/s/article/UUID-16ba712c-8d29-fecd-1d91-611779fbdc90](https://my.onetrust.com/s/article/UUID-16ba712c-8d29-fecd-1d91-611779fbdc90)  
38. Topic 2: Automatic Transfer to FTP Server - YouTube, accessed November 24, 2025, [https://www.youtube.com/watch?v=8raIma2JqnA](https://www.youtube.com/watch?v=8raIma2JqnA)  
39. SoftPro LIVE Pricing, accessed November 24, 2025, [https://info.softprocorp.com/hubfs/SoftPro%20LIVE%20Pricing.pdf](https://info.softprocorp.com/hubfs/SoftPro%20LIVE%20Pricing.pdf)  
40. The End of Switching Charges: Commercial Impact and Compliance Priorities, accessed November 24, 2025, [https://kempitlaw.com/insights/the-end-of-switching-charges-commercial-impact-and-compliance-priorities/](https://kempitlaw.com/insights/the-end-of-switching-charges-commercial-impact-and-compliance-priorities/)  
41. SoftPro Pricing 2025: Compare Plans and Costs - TrustRadius, accessed November 24, 2025, [https://www.trustradius.com/products/softpro/pricing](https://www.trustradius.com/products/softpro/pricing)  
42. Data Return Formats After Cloud Termination - Attorney Aaron Hall, accessed November 24, 2025, [https://aaronhall.com/data-return-formats-after-cloud-termination/](https://aaronhall.com/data-return-formats-after-cloud-termination/)  
43. Process in ResWare® Setup Policy Upload - IIS Windows Server, accessed November 24, 2025, [https://registration.firstam.com/EA/AgentNetIntegrationTraining/Content/ResWare/ResWarePolicyUploadProcess.pdf](https://registration.firstam.com/EA/AgentNetIntegrationTraining/Content/ResWare/ResWarePolicyUploadProcess.pdf)





# 21.
## 21.1.
`R⬆⠿` ≔ ⠿~ (Рекомендации для моего ответа `ꆜ` на `P⁎`)

## 21.2.
`R⬆ᵢ` : `R⬆⠿`

# 22. Анализ `R⬆⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/75fa8ec1b5e7

## R⬆₁: Опровергнуть осуществимость универсального SQL-подхода (T⁎)

### Суть
Рекомендуется в ответе прямо указать, что предложенное клиентом решение (`T⁎`) технически неосуществимо в качестве универсального продукта.
Решение предполагает создание приложения для прямого опроса SQL-баз систем производства титулов (TPS).
Эта неосуществимость обусловлена доминированием на рынке хостинговых (Hosted) сред, таких как SoftPro Hosted и Resware Cloud.
Вендоры этих систем блокируют прямой доступ к базам данных на сетевом уровне (TCP 1433) для обеспечения стабильности и безопасности мультиарендной архитектуры (`O.md`::§17.2).
Подход, основанный исключительно на прямом доступе к SQL, не применим к значительной части клиентской базы TitleSphere.

### Оценка
95/100

### Достоинства
Этот подход демонстрирует глубокую экспертизу в специфике технологического ландшафта TPS (SoftPro, Resware).
Честное указание на ограничения предотвращает инвестиции в заведомо неработоспособную архитектуру.
Эта архитектура основана на заблуждениях клиента (`D𐊑₁`, `D𐊑₃`).
Это позволяет немедленно переориентировать диалог на поиск реалистичных альтернатив (`Aᚖ⠿`).
Установление реалистичных ожиданий на старте повышает доверие к исполнителю как к эксперту.

### Недостатки
Существует риск оттолкнуть клиента, который твердо убежден в работоспособности своей идеи.
Клиент может предпочесть менее компетентного исполнителя, который пообещает реализовать предложенное решение.
Требуется тактичная и детально аргументированная подача информации, чтобы избежать конфронтации.

## R⬆₂: Акцентировать регуляторные барьеры и риски безопасности (GLBA/CFPB)

### Суть
Необходимо подчеркнуть, что организационные и регуляторные барьеры являются критическим препятствием для реализации `T⁎` и рискованных альтернатив, таких как RPA.
Индустрия титульного страхования обрабатывает непубличную персональную информацию (NPI) и строго регулируется федеральным законодательством США.
Аргументация должна опираться на требования Закона Грэмма-Лича-Блайли (GLBA) в отношении прямого доступа к SQL.
Также следует ссылаться на директивы Бюро финансовой защиты потребителей (CFPB) в отношении скрин-скрейпинга (RPA).

### Оценка
95/100

### Достоинства
Апелляция к комплаенсу является сильным аргументом в строго регулируемой финансовой индустрии.
Это позиционирует исполнителя как зрелого партнера, понимающего важность защиты данных и соблюдения стандартов ALTA Best Practices (Столп 3) (`O.md`::§20.1.2.2).
Это переводит вопрос из плоскости технической возможности в плоскость юридической недопустимости и неприемлемых бизнес-рисков (`D𐊑₂`).
Прямой доступ к базе данных в обход приложения нарушает «Правило о гарантиях» (Safeguards Rule) Закона GLBA (16 CFR Part 314).
Это правило требует строгого контроля доступа к информации о клиентах.
Пункт 16 CFR § 314.4(c)(1) гласит:
> (1) Implementing and periodically reviewing access controls, including technical and, as appropriate, physical controls to: (i) Authenticate and permit access only to authorized users to protect against the unauthorized acquisition of customer information; and (ii) Limit authorized users' access only to customer information that they need to perform their duties and functions...
> (1) Внедрение и периодический пересмотр мер контроля доступа, включая технические и, при необходимости, физические меры контроля, чтобы: (i) Аутентифицировать и разрешать доступ только авторизованным пользователям для защиты от несанкционированного получения информации о клиентах; и (ii) Ограничивать доступ авторизованных пользователей только той информацией о клиентах, которая необходима им для выполнения своих обязанностей и функций...
Кроме того, использование RPA (скрин-скрейпинг) противоречит позиции CFPB, которая стремится исключить эту практику в рамках регулирования по Разделу 1033 Закона Додда-Франка.
В финальном правиле CFPB по правам на персональные финансовые данные (Personal Financial Data Rights, Документ CFPB-2024-0054) прямо указывается на недопустимость скрин-скрейпинга как метода обеспечения доступа:
> ...the data provider cannot comply with the requirement to make data available to authorized third parties by allowing the third party to engage in “screen scraping,” an access method that uses consumer credentials to log in to consumer accounts to retrieve data.
> ...поставщик данных не может выполнить требование о предоставлении данных авторизованным третьим сторонам, разрешая третьей стороне заниматься «скрин-скрейпингом» — методом доступа, который использует учетные данные потребителя для входа в учетные записи потребителя с целью извлечения данных.

### Недостатки
Клиент может посчитать эти барьеры преувеличенными или управляемыми (например, через доступ только на чтение).
Обсуждение регуляторных требований может усложнить и замедлить процесс согласования проекта.
Клиент может не обладать достаточной экспертизой для оценки этих рисков.

## R⬆₃: Предложить событийно-ориентированную интеграцию как приоритетное решение

### Суть
В качестве основного технического решения следует предложить архитектуру, основанную на нативных триггерах событий платформ TPS (Решение A1 в `O.md`::§20.6.1).
Этот подход меняет модель интеграции с запроса данных (Pull) на их доставку (Push).
Для Resware это предполагает настройку «Списков действий» (Action Lists) для отправки XML-данных через HTTP POST на вебхук TitleSphere (`O.md`::§20.3.1).
Для SoftPro это включает использование инструмента уведомлений о задачах (Task Notification Tool - TNT) или автоматизации SoftPro Select для отправки структурированных электронных писем с вложениями (`O.md`::§20.2.2).

### Оценка
90/100

### Достоинства
Этот подход обеспечивает синхронизацию данных в режиме, близком к реальному времени.
Решение опирается на санкционированные вендором механизмы, что гарантирует высокую стабильность и совместимость.
Событийная модель эффективна, так как снижает нагрузку на серверы по сравнению с постоянным опросом.
Решение полностью соответствует требованиям безопасности и комплаенса (GLBA/ALTA), так как использует защищенный транспорт (HTTPS, TLS).

### Недостатки
Сложность реализации выше, чем у простого экспорта отчетов.
Настройка триггеров (особенно TNT в SoftPro) может быть трудоемкой.
Она требует адаптации под рабочие процессы каждого конечного пользователя TitleSphere.
Требуется разработка логики парсинга и обработки событий (вебхуки, парсинг почты) на стороне TitleSphere.

## R⬆₄: Предложить автоматизированный экспорт отчетов как комплементарный метод

### Суть
В дополнение к событийной интеграции следует предложить использование встроенных функций TPS для генерации отчетов по расписанию (CSV, XML).
Доставка отчетов должна осуществляться через безопасный протокол SFTP (Решение A3 в `O.md`::§20.6.3, `Aᚖ₂`).
Этот метод предназначен для пакетной синхронизации и полной сверки данных.

### Оценка
80/100

### Достоинства
Это наиболее надежный и стабильный метод извлечения данных из закрытых систем (`O.md`::§19.Aᚖ₂).
Решение обладает низкой совокупной стоимостью владения (TCO), так как форматы отчетов меняются редко.
Метод соответствует строгим требованиям безопасности, используя стандартный защищенный протокол SFTP.
Это служит надежной резервной копией для триггеров реального времени, гарантируя целостность данных.

### Недостатки
Данные передаются в пакетном режиме, а не в реальном времени.
Объем и структура экспортируемых данных ограничены возможностями системы отчетности TPS.
Может потребоваться разработка кастомных отчетов на стороне TPS, что часто является платной услугой вендора (`O.md`::§14.3.2).

## R⬆₅: Рекомендовать разработку гибридной модульной платформы (Aᚖ₅)

### Суть
В ответе следует предложить разработку не простого приложения, а комплексной гибридной интеграционной платформы (`Aᚖ₅`).
Эта платформа должна объединять различные методы интеграции.
Платформа должна адаптивно выбирать оптимальный метод в зависимости от среды клиента (тип TPS, модель развертывания, политики безопасности).
Приоритетными методами должны быть событийная интеграция (`R⬆₃`) и экспорт отчетов (`R⬆₄`).
Прямой доступ к SQL следует рассматривать только как опцию для специфических On-Premise инсталляций с доступом к Read-Only реплике.
RPA следует исключить из стратегии из-за высоких регуляторных и технических рисков (`R⬆₂`).

### Оценка
85/100

### Достоинства
Гибридная стратегия обеспечивает максимальный охват рынка TitleSphere, учитывая гетерогенность ландшафта TPS (`D𐊑₃`).
Платформа устойчива к изменениям в экосистеме TPS и политикам отдельных вендоров.
Модульность позволяет поэтапно наращивать функциональность и подключать новые системы.
Предложение комплексного решения демонстрирует стратегическое видение и архитектурный подход.

### Недостатки
Это значительно более сложный и дорогостоящий проект по сравнению с запрошенным клиентом простым приложением.
Клиент может воспринять это как излишнее усложнение архитектуры (over-engineering) или попытку раздуть бюджет.
Увеличивается сложность онбординга клиентов, так как потребуется аудит их инфраструктуры и настройка соответствующего модуля.

## Итоговый вердикт

Анализ контекста проекта `P⁎` и экосистемы TPS (SoftPro, Resware) показывает, что предложенное клиентом техническое решение (`T⁎` — прямой доступ к SQL) является нежизнеспособным.
Оно основано на критических заблуждениях (`D𐊑⠿`) относительно доступности данных в хостинговых средах, сложности ETL и серьезности регуляторных рисков (GLBA, CFPB).

Стратегия ответа на Upwork должна базироваться на тактичном, но твердом пересмотре предложенного подхода и предложении реалистичной альтернативы.

Ключевые элементы ответа должны включать следующие шаги:

1.  **Валидация проблемы и демонстрация экспертизы:** Подтвердить понимание боли клиента (`P†`) и знание специфики SoftPro/Resware.
2.  **Опровержение SQL-подхода (`R⬆₁`)**: Аргументированно объяснить техническую невозможность универсального применения в Hosted-средах.
3.  **Акцент на безопасности и комплаенсе (`R⬆₂`)**: Указать на риски GLBA при прямом доступе к SQL и риски CFPB при использовании RPA, обосновывая отказ от этих методов.
4.  **Предложение оптимальной архитектуры (`R⬆₅`)**: Представить гибридную модульную платформу как единственное надежное, безопасное и масштабируемое решение.
5.  **Детализация технического решения**: Приоритизировать событийную интеграцию (`R⬆₃`) для синхронизации в реальном времени и дополнить её автоматизированным экспортом отчетов (`R⬆₄`) для надежности.

Такой подход позволит выстроить диалог с позиции эксперта, избежать технического тупика и предложить клиенту стратегическое решение его бизнес-задачи.

# 23. Анализ `R⬆⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/e76a42c03e7b


## **Введение**

Интеграция унаследованных систем (legacy systems) с современными облачными платформами представляет собой одну из наиболее острых проблем в секторе LegalTech и PropTech, особенно в индустрии титульного страхования США. Данный отчет посвящен всестороннему анализу задачи («᛭T»), поставленной компанией Sphere («ꆜ»), по разработке локально устанавливаемого приложения для синхронизации данных между Title Production Systems (TPS), такими как SoftPro и Resware, и API платформы Sphere.

Существующий ландшафт программного обеспечения для титульных компаний характеризуется доминированием решений, архитектура которых уходит корнями в клиент-серверные модели конца 1990-х и начала 2000-х годов. Как справедливо отмечает заказчик, многие из этих продуктов функционально и визуально напоминают эпоху «Windows 3.1», что создает существенный технологический разрыв при попытке внедрения современных CRM-инструментов. Проблема («P†») заключается в отсутствии у большинства инсталляций TPS надежных, открытых API для обмена данными в реальном времени, что вынуждает пользователей прибегать к ручному экспорту и импорту CSV-файлов — процессу, который является не только трудоемким, но и подверженным ошибкам человеческого фактора.

Целью данного исследования является выявление оптимального архитектурного решения, которое, с одной стороны, обеспечит автоматизированный («seamless») поток данных, требуемый заказчиком, а с другой — будет соответствовать строгим регуляторным нормам, включая Gramm-Leach-Bliley Act (GLBA) и стандарты American Land Title Association (ALTA). Отчет структурирован таким образом, чтобы предоставить глубокий технический анализ предложенных стратегий («R⬆⠿»), оценить их жизнеспособность в контексте специфики TPS и предложить обоснованный вердикт, подкрепленный юридической и технической аргументацией.

## **Регуляторный ландшафт и требования к безопасности данных**

Любое техническое вмешательство в инфраструктуру титульной компании, предполагающее автоматизированный доступ к базам данных заказов, неизбежно затрагивает вопросы обработки Non-Public Personal Information (NPI). Понимание юридического базиса является не просто формальностью, а критическим условием для проектирования архитектуры, которая не подвергнет конечного пользователя рискам штрафов или потери лицензии.

### **Императивы федерального законодательства: 16 CFR Part 314**

Краеугольным камнем регулирования информационной безопасности в финансовом секторе США, к которому относятся и титульные компании, является «Safeguards Rule», утвержденное Федеральной торговой комиссией (FTC). Обновленная редакция 16 CFR Part 314 вводит жесткие предписания, игнорирование которых при разработке интеграционного ПО недопустимо.

Согласно разделу § 314.4(c)(3), организации обязаны внедрять конкретные технические меры защиты. Официальный текст гласит: «(3) Protect by encryption all customer information held or transmitted by you both in transit over external networks and at rest».1 В переводе это означает императивное требование: «Защищать посредством шифрования всю информацию о клиентах, хранящуюся у вас или передаваемую вами, как во время передачи по внешним сетям, так и в состоянии покоя».

Для разработчика интеграционного решения это требование имеет прямые архитектурные последствия:

1. **Запрет на открытое хранение учетных данных:** Хранение строк подключения к SQL-серверу (connection strings) с логином и паролем в текстовых конфигурационных файлах (например, app.config или settings.json) является прямым нарушением требования о шифровании «at rest» (в покое).  
2. **Шифрование транспортного канала:** Любая передача данных из локальной сети титульного агента в облако Sphere должна осуществляться исключительно по защищенным протоколам (TLS 1.2/1.3).  
3. **Управление ключами:** Механизм хранения ключей шифрования, используемых локальным агентом, должен исключать возможность их легкого извлечения злоумышленником, получившим физический или удаленный доступ к серверу.

Кроме того, раздел § 314.4(a) требует назначения «Квалифицированного лица» (Qualified Individual), ответственного за надзор и внедрение программы информационной безопасности.2 Это означает, что внедрение любого стороннего ПО, такого как предлагаемый коннектор Sphere, должно быть одобрено этим лицом и интегрировано в общую карту рисков компании. Раздел § 314.4(b) обязывает проводить оценку рисков, которая должна выявлять «разумно предсказуемые внутренние и внешние риски для безопасности, конфиденциальности и целостности информации о клиентах».1 Следовательно, архитектура приложения должна быть документирована настолько детально, чтобы позволить IT-директору или CISO титульной компании без труда включить его в свой реестр рисков.

### **Стандарты ALTA Best Practices 4.0**

Помимо федеральных законов, титульная индустрия регулируется стандартами саморегулируемой организации — American Land Title Association (ALTA). Соблюдение «Best Practices» является де-факто обязательным условием для того, чтобы титульные агенты могли работать с крупными ипотечными кредиторами.

В версии 4.0 стандартов ALTA, Столп №3 (Pillar 3) посвящен защите NPI. Документация гласит: «Best Practice: Adopt and maintain a written information security plan (“WISP”) and a written privacy plan to protect NPI as required by local, state, and federal law».3 Это требование перекликается с GLBA, но добавляет специфический отраслевой контекст.

Особое внимание следует уделить разделу, касающемуся управления поставщиками услуг (Service Providers). Стандарт ALTA требует: «Vendors must be selected, reviewed, and monitored based on their ability to protect NPI».4 Для компании Sphere это означает, что предлагаемое программное обеспечение переводит её в статус вендора, подлежащего аудиту. Если архитектура приложения подразумевает, что оно «бесконтрольно» выкачивает данные, это может стать блокирующим фактором для прохождения титульным агентом ежегодной сертификации ALTA.

Нововведения в версии 4.0 также касаются управления паролями и многофакторной аутентификации (MFA). Как отмечается в отраслевых обзорах, «Pillar 3 revisions require greater physical protection of NPI, additional safeguards for cloud-based data, and robust plans for business continuity».5 Это подразумевает, что если локальный агент имеет интерфейс администрирования, доступ к нему должен быть защищен MFA, либо он должен интегрироваться в существующую систему управления доступом (например, Active Directory), чтобы не создавать «теневых» учетных записей.

## **R⬆1-S: Прямое подключение к SQL Server (Direct Database Access)**

### **Суть подхода**

Данная стратегия представляет собой классический подход к интеграции «толстых клиентов» (Rich Client) эпохи клиент-серверной архитектуры. Она подразумевает разработку службы Windows (Windows Service) или фонового демона, который инсталлируется непосредственно на сервер базы данных TPS или на сервер приложений в локальной сети титульной компании.

Техническая реализация базируется на использовании стандартных драйверов доступа к данным, таких как ODBC, OLE DB или ADO.NET, для установления прямого соединения с экземпляром Microsoft SQL Server, обслуживающим TPS. Приложение конфигурируется с использованием строки подключения (Connection String), содержащей адрес сервера, имя базы данных и учетные данные пользователя с правами на чтение (db_datareader).

Алгоритм работы такого решения обычно следующий:

1. Служба просыпается по расписанию (например, каждые 15 минут) или работает в бесконечном цикле с задержкой (polling).  
2. Выполняется SQL-запрос (SELECT) к ключевым таблицам, содержащим информацию о заказах (Orders), контактах (Contacts/Parties), статусах (Tracking Items) и финансовых показателях.  
3. Полученный набор данных (DataSet) трансформируется и сериализуется в формат JSON, соответствующий спецификации API Sphere.  
4. Данные отправляются в облако посредством HTTPS POST/PUT запросов.

Этот подход наиболее точно соответствует формулировке задачи клиента: «regularly query the TPS system's SQL database» (регулярно опрашивать SQL базу данных системы TPS), и является интуитивно понятным первым шагом для любого разработчика.

### **Оценка жизнеспособности**

**65/100**

### **Достоинства**

Главным преимуществом прямого SQL-доступа является **абсолютная гибкость** в выборе данных. Разработчик не ограничен тем набором полей, который вендор TPS решил «открыть» через свой API или механизм экспорта. Если данные существуют в таблице, их можно извлечь. Это особенно критично для кастомизированных инсталляций TPS, где пользователи добавляют собственные поля (Custom Fields) для специфических нужд бизнеса.

Вторым неоспоримым плюсом является **производительность**. Прямой SQL-запрос, при условии наличия корректных индексов, всегда будет работать быстрее, чем обращение через слой объектно-реляционного отображения (ORM) или через веб-сервис SOAP/REST, который добавляет накладные расходы на сериализацию и десериализацию XML/JSON. Для задач массовой выгрузки исторических данных («entire history of their business») прямой доступ к SQL часто является единственным способом получить результат за приемлемое время.

**Экономическая эффективность** также играет роль. Реализация этого метода не требует покупки дополнительных лицензий на модули интеграции, такие как SoftPro 360 или Resware API. Это делает решение привлекательным для малых и средних агентств, чувствительных к стоимости владения ПО.

Наконец, **независимость от GUI**. Служба работает в фоновом режиме (Session 0 в Windows), не требуя активной пользовательской сессии или запущенного клиента SoftPro/Resware. Это обеспечивает стабильность процесса синхронизации, который не прервется, если сотрудник закроет приложение или выйдет из системы на обед.

### **Недостатки**

Несмотря на очевидные плюсы, риски данного подхода существенны и могут перевесить выгоды.

**Риск блокировок (Locking Contention):** Прямое чтение из базы данных OLTP (Online Transaction Processing), которая активно используется сотрудниками для ввода заказов, создает риск блокировок. Если запрос на выборку данных будет слишком «тяжелым» или неоптимизированным (например, Table Scan большой таблицы истории), он может наложить Shared Locks (S-locks), которые заблокируют попытки записи (X-locks) со стороны пользователей. Это приведет к «зависанию» программы у сотрудников, что неприемлемо для операционной деятельности. Использование хинтов NOLOCK или уровня изоляции READ UNCOMMITTED решает проблему блокировок, но создает риск чтения «грязных» данных (Dirty Reads), что может привести к отправке в Sphere некорректной информации.

**Сложность схемы данных:** Базы данных корпоративного уровня, такие как SoftPro Select, имеют высоко нормализованную и сложную схему. Данные по одному заказу могут быть разбросаны по десяткам таблиц (Order, OrderContact, Property, Address, Policy, HUDLine и т.д.). Написание корректных SQL-запросов требует глубокого понимания внутренней структуры БД («реверс-инжиниринг»), которая часто не документирована публично. Более того, вендоры могут изменять схему БД в минорных обновлениях, что приведет к поломке SQL-запросов и отказу интеграции.

**Проблемы с поддержкой вендора:** Лицензионные соглашения многих TPS (EULA) содержат пункты, запрещающие прямое подключение к базе данных сторонними средствами. Обнаружение такой активности может стать формальным поводом для отказа в технической поддержке со стороны SoftPro или Qualia (владельца Resware). Это ставит клиента («ꆜ») в уязвимое положение.

**Вектор атаки на безопасность:** Для работы службы необходимо сохранить учетные данные SQL-пользователя на сервере. Даже если они зашифрованы, сам факт наличия «суперпользователя» с прямым доступом к базе, который используется автоматическим скриптом, создает дополнительную поверхность атаки. Это усложняет прохождение аудитов безопасности и соответствие требованиям 16 CFR Part 314, требующим минимизации привилегий.

**Ограничения хостинговых сред:** Самый критичный недостаток — несовместимость с облачными и гибридными средами. Официальная документация SoftPro Hosted указывает на строгие ограничения доступа к ресурсам. «SoftPro Hosted requires that you install and use the Okta Verify App... Internet dependent applications need QoS...».7 В таких средах, как SoftPro Hosted или Resware Cloud, клиент, скорее всего, не имеет административного доступа к SQL Server и не может открыть порты (обычно 1433) для прямого подключения. Это делает метод R⬆1 неприменимым для растущего сегмента рынка, использующего SaaS-модели.

## **R⬆2-S: Использование нативных механизмов автоматизации (Action Lists / TNT)**

### **Суть подхода**

Данная стратегия представляет собой сдвиг парадигмы с активного опроса («pull») на событийно-ориентированную модель («push»). Вместо того чтобы внешнее приложение «тянуло» данные из базы, мы настраиваем саму TPS на то, чтобы она «выталкивала» данные при наступлении определенных бизнес-событий.

В экосистеме **Resware** этот механизм реализован через «Action Lists». Это мощный встроенный движок workflow, который позволяет администратору системы настраивать триггеры (например, «Создан новый заказ», «Изменен статус файла», «Назначен нотариус»). При срабатывании триггера система может выполнить действие, в том числе отправить XML-пакет данных на внешний URL или сохранить его в папку. Документация Resware описывает процесс настройки интеграции: «You can send action events to Resware through the integration... Step 1: Select Admin > Action Lists > Action Events... Step 3: Add action codes...».8 Это позволяет настроить отправку данных в формате Resware XML, который является стандартом де-факто для этой платформы.

Для **SoftPro Select** аналогом является инструмент «Task Notification Tool» (TNT) или встроенный модуль автоматизации на базе Python (SoftPro Select Automation). TNT позволяет отправлять шаблонизированные письма с вложениями при выполнении задач. В документации указано: «The Task Notification Tool (TNT) for SoftPro Select allows you to send templated emails automatically when specific tasks have met certain criteria. This email can include attachments...».9 Хотя email не является идеальным транспортом для интеграции API, этот механизм демонстрирует возможности встроенной автоматизации. Более продвинутым вариантом является использование SoftPro API в рамках IronPython скриптов, запускаемых триггерами внутри системы, для прямой отправки HTTP-запросов.

### **Оценка жизнеспособности**

**92/100**

### **Достоинства**

**Легитимность и поддержка:** Это единственно «правильный» способ интеграции с точки зрения архитектуры TPS. Используя штатные механизмы (Action Lists, TNT), вы действуете в рамках предусмотренной логики системы. Это гарантирует сохранение целостности транзакций и, что немаловажно, сохранение гарантийной поддержки со стороны вендора. Ни SoftPro, ни Qualia не смогут предъявить претензии за использование функций, которые они сами задокументировали и продали клиенту.

**Безопасность данных (Data Integrity):** Экспорт данных выполняется внутренним движком TPS. Это означает, что система сама заботится о блокировках, уровнях изоляции и консистентности данных. Исключается риск «грязного чтения», присущий прямым SQL-запросам. Если заказ находится в процессе редактирования пользователем и транзакция не закрыта, событие просто не сработает или данные будут взяты из зафиксированного состояния.

**Реальное время (Real-Time):** В отличие от поллинга, который всегда имеет задержку (lag), событийная модель позволяет получать данные мгновенно. Как только менеджер нажал кнопку «Сохранить», Resware может сгенерировать событие и отправить данные в Sphere. Это критично для сценариев, где важна скорость реакции, например, для отправки приветственного письма клиенту сразу после открытия заказа.

**Стандартизация формата:** XML-схемы Resware и форматы данных SoftPro являются устоявшимися стандартами. Работая с ними, разработчик получает структурированные данные, которые легче парсить и валидировать, чем результаты «сырых» SQL-запросов.

### **Недостатки**

**Сложность развертывания:** Главным минусом является то, что настройка Action Lists и триггеров требует **глубоких знаний администрирования конкретной TPS**. Это невозможно полностью автоматизировать через внешний инсталлятор .msi или .exe. Потребуется либо ручная работа инженера внедрения, который зайдет в админку Resware и пропишет нужные правила, либо разработка сложного скрипта конфигурации, использующего административный API TPS (если он доступен). Это противоречит желанию клиента сделать процесс «seamless and automated» (бесшовным и автоматизированным).

**Ограниченность данных:** Набор данных, доступный через стандартные XML-пакеты событий, может быть неполным. Например, событие «Заказ открыт» может передавать основные поля заказа, но не передавать специфические пользовательские поля (UDF) или историю коммуникаций. Для получения этих данных может потребоваться вторичный запрос к API, что усложняет логику.

**Лицензионные требования:** Использование продвинутых функций автоматизации часто требует наличия определенных лицензий. В SoftPro использование API или модуля SoftPro 360 для интеграций обычно является платной опцией. Документация упоминает: «When you order products and services through SoftPro's integrated vendor portal SoftPro 360, the information needed... automatically transfers».10 Если у клиента нет лицензии на 360 или Automation, этот путь может быть закрыт или потребовать дополнительных затрат.

**Зависимость от внутренней логики:** Если администратор клиента решит перенастроить рабочие процессы (Workflows) и удалит или изменит действие, к которому привязана интеграция, поток данных прекратится. Это делает решение зависимым от «человеческого фактора» на стороне клиента.

## **R⬆3-S: Архитектура с промежуточной репликацией (Replica/Log Shipping)**

### **Суть подхода**

Данная стратегия является компромиссом между скоростью прямого доступа (R⬆1) и безопасностью производственной среды. Идея заключается в создании **вторичной копии** (Replica) базы данных TPS, предназначенной исключительно для чтения и аналитики.

Технически это может быть реализовано несколькими способами средствами Microsoft SQL Server:

1. **Transactional Replication:** Данные из основной базы (Publisher) почти в реальном времени транслируются в базу-подписчик (Subscriber).  
2. **Log Shipping:** Журналы транзакций основной базы периодически копируются и восстанавливаются на вторичном сервере. Это создает задержку данных (lag), но является очень надежным и дешевым методом.  
3. **Always On Availability Groups (Read-Only Routing):** В более дорогих редакциях SQL Server Enterprise можно использовать одну из нод кластера для чтения (Read-Only Intent).

Разрабатываемое приложение-коннектор настраивается на подключение именно к этой реплике. Оно может выполнять сколь угодно сложные и «тяжелые» запросы, не опасаясь заблокировать работу менеджеров, вводящих заказы в основной системе.

### **Оценка жизнеспособности**

**80/100**

### **Достоинства**

**Изоляция нагрузки:** Это самое главное преимущество. Аналитическая нагрузка (выгрузка истории за 10 лет) полностью отделена от операционной. Риск того, что интеграция «положит» базу данных в разгар рабочего дня, сведен к нулю.

**Полнота данных:** Как и в случае с R⬆1, мы имеем доступ ко всем таблицам и полям, но в безопасном режиме. Это позволяет строить сложные отчеты и агрегации, необходимые для Sphere, чтобы показать «всю историю их бизнеса».

**Отказоустойчивость:** Реплика базы данных может служить частью стратегии Disaster Recovery (DR). Если основной сервер упадет, данные останутся доступными на реплике, что соответствует требованиям ALTA Best Practices по обеспечению непрерывности бизнеса.

### **Недостатки**

**Высокие требования к ресурсам:** Содержание второй копии базы данных требует **удвоения дискового пространства**. Учитывая, что базы данных титульных компаний могут достигать сотен гигабайт (из-за хранения сканов документов в BLOB-полях), это может потребовать апгрейда серверного оборудования. Системные требования SoftPro уже предписывают: «Servers: 8 GB RAM or higher... Disk Space: 7 GB» (для пустой базы), а реальные объемы значительно выше.12

**Сложность администрирования:** Настройка и поддержка репликации SQL Server — это задача для квалифицированного администратора баз данных (DBA). Это не то, что можно «установить и забыть» через простой инсталлятор. Репликация может ломаться при обрывах сети, переполнении логов или обновлении схемы БД. Если у клиента нет штатного DBA (что типично для компаний 10-99 сотрудников, как у «ꆜ»), поддержка такого решения ляжет на плечи Sphere.

**Лицензионные ограничения SQL:** Многие малые офисы используют **SQL Server Express Edition**, который бесплатен, но имеет существенные ограничения. В частности, SQL Express может выступать только как Subscriber в транзакционной репликации, но настройка Publisher на нем ограничена или невозможна без покупки полноценной лицензии SQL Server Standard, что стоит тысячи долларов. Это делает решение экономически неприемлемым для малого бизнеса.

## **R⬆4-S: Screen Scraping и RPA (Robotic Process Automation)**

### **Суть подхода**

Скрин-скрейпинг (Screen Scraping) или RPA (Robotic Process Automation) — это метод автоматизации, при котором программный робот имитирует действия человека-оператора. Скрипт запускает клиентское приложение TPS, авторизуется под служебной учетной записью, открывает нужные окна (экраны заказов, отчеты), копирует данные из полей ввода или таблиц и сохраняет их во внешнюю систему.

В контексте задачи «ꆜ» это могло бы выглядеть как бот, который каждую ночь запускает SoftPro, генерирует отчет «Новые заказы за день», сохраняет его в Excel/CSV, а затем парсит этот файл и отправляет в API Sphere. Технологически это может быть реализовано через инструменты UI Automation, Selenium (для веб-версий), AutoIt или специализированные платформы типа UiPath.

### **Оценка жизнеспособности**

**10/100**

### **Достоинства**

**Универсальность:** Теоретически этот метод работает с **любой** системой, которая имеет пользовательский интерфейс. Неважно, есть ли у системы API, доступна ли база данных, находится ли она в облаке или на локальном сервере. Если человек может увидеть данные на экране, робот может их считать. Это позволяет обойти ограничения закрытых облачных сред типа Citrix, где нет доступа ни к чему, кроме «картинки» экрана.

**Независимость от схемы БД:** Робот работает с бизнес-терминами («Номер заказа», «Имя покупателя»), представленными в интерфейсе, а не с именами таблиц и колонок в базе данных. Это избавляет от необходимости разбираться в сложной нормализованной схеме SQL.

### **Недостатки**

**Крайне низкая надежность:** Это самое «хрупкое» решение. Любое незначительное изменение интерфейса — перемещение кнопки, изменение шрифта, появление всплывающего окна с рекламой или предупреждением — приведет к сбою скрипта. Поддержка такого решения превращается в ад: каждое обновление TPS требует переписывания ботов.

**Юридические риски (Regulatory Compliance):** Это критический блокирующий фактор. Регулятор CFPB (Consumer Financial Protection Bureau) занял жесткую позицию в отношении скрин-скрейпинга. В документах, касающихся секции 1033 (Personal Financial Data Rights), CFPB прямо указывает: «Screen scraping poses risks to consumer privacy and data security... attempts by third parties to reach data... could well be limited by the CFPA's prohibition on unfair, deceptive, and abusive acts or practices».13 Использование скрин-скрейпинга для сбора NPI (данных о заемщиках) может быть расценено как «недобросовестная практика» (UDAAP), что грозит огромными штрафами. Кроме того, передача пароля от учетной записи третьей стороне (скрипту) нарушает принципы безопасности многих банков и финансовых институтов.

**Блокировка ресурсов:** RPA требует выделенной пользовательской сессии. Робот занимает компьютер (или виртуальную машину), двигает мышкой, открывает окна. Это мешает работе реальных пользователей и требует выделения отдельной рабочей станции под «робота», что увеличивает затраты.

**Масштабируемость:** Метод абсолютно не масштабируем. Если объем данных вырастет, роботу потребуется больше времени на «прокликивание» экранов, что физически ограничено скоростью работы интерфейса.

## **R⬆5-S: Использование промежуточного API-шлюза с локальным кэшированием (Smart Agent)**

### **Суть подхода**

Эта стратегия является эволюцией метода R⬆1, обогащенной современными практиками разработки распределенных систем. Она предполагает установку на сервер клиента «умного агента» (Smart Agent) — легковесного приложения (написанного, например, на Go, Rust или.NET Core).

Архитектура решения:

1. **Локальное хранилище:** Агент создает собственную локальную, зашифрованную базу данных (например, SQLite с SQLCipher или LocalDB).  
2. **Инкрементальная синхронизация:** Агент подключается к TPS (через SQL или API) и забирает только **изменения** (Delta), произошедшие с момента последней синхронизации. Используются техники Change Data Capture (CDC) или отслеживание по полям LastModifiedDate/RowVersion.  
3. **Кэширование и трансформация:** Полученные данные сохраняются в локальный кэш, где проходят очистку, валидацию и трансформацию в целевую модель данных Sphere.  
4. **Асинхронная отправка:** Агент отправляет пакеты данных в облако Sphere в фоновом режиме, используя надежные очереди сообщений.

### **Оценка жизнеспособности**

**88/100**

### **Достоинства**

**Оптимизация трафика и нагрузки:** Передача только дельты изменений («It's a very small amount of data - probably less than 10MB daily» — как верно заметил клиент) кардинально снижает нагрузку на сеть. Локальное кэширование позволяет минимизировать количество тяжелых запросов к основной базе TPS.

**Соответствие требованиям безопасности:** Локальная база данных агента может (и должна) быть зашифрована, что обеспечивает соответствие требованию 16 CFR § 314.4(c)(3) о защите данных «at rest».1 Агент может управлять ключами шифрования и ротировать их, не затрагивая основную базу TPS.

**Устойчивость (Resilience):** Локальный кэш позволяет пережить временные разрывы интернет-соединения. Агент будет накапливать данные у себя и отправит их, когда связь восстановится. Это критично для офисов с нестабильным интернетом.

**Предварительная валидация:** Агент выступает фильтром, не пропуская в облако Sphere «мусорные» или некорректные данные, что повышает общее качество данных в CRM.

### **Недостатки**

**Сложность реализации:** Реализация надежного механизма определения изменений (CDC) на уровне приложения — нетривиальная задача. В таблицах legacy-систем часто отсутствуют надежные метки времени изменения для всех связанных сущностей. Приходится изобретать сложные алгоритмы хеширования записей для сравнения.

**Риск рассинхронизации:** Существует риск (Data Drift), когда данные в кэше агента начинают отличаться от данных в реальной базе TPS из-за ошибок логики синхронизации или коллизий. Требуются механизмы периодической полной сверки (Reconciliation).

**Проблема обновления:** Агент устанавливается в инфраструктуре, которую разработчик не контролирует. Механизм автообновления агента должен быть пуленепробиваемым, чтобы не потребовалось выезжать в офис к каждому клиенту при выходе патча.

## **Сравнительный анализ стратегий**

В таблице ниже представлено сводное сравнение рассмотренных архитектурных подходов по ключевым критериям, важным для принятия решения.

| Критерий | R⬆1: Direct SQL | R⬆2: Action Lists | R⬆3: Replication | R⬆4: Screen Scraping | R⬆5: Smart Agent |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Скорость разработки** | Высокая | Средняя | Низкая | Средняя | Средняя |
| **Риск блокировок БД** | Высокий | Отсутствует | Отсутствует | Низкий | Средний (контролируемый) |
| **Полнота данных** | Полная | Ограниченная | Полная | Ограниченная (UI) | Полная |
| **Юридическая чистота** | Низкая (EULA) | Высокая | Высокая | Критическая (CFPB) | Средняя |
| **Сложность внедрения** | Низкая | Высокая (ручная) | Очень высокая | Высокая | Низкая (авто) |
| **Соответствие 16 CFR 314** | Требует доработки | Нативно | Нативно | Нарушает | Нативно (с шифрованием) |
| **Работа в Cloud/Hosted** | Нет | Да | Нет | Да | Нет |

## **Вердикт и стратегические рекомендации**

### **Синтез оптимального решения**

На основании проведенного анализа, очевидно, что идеального решения «серебряной пули» не существует из-за разнородности инфраструктуры клиентов. Стратегии **R⬆4 (Screen Scraping)** и **R⬆3 (Replication)** следует отбросить: первая — из-за критических юридических рисков и ненадежности, вторая — из-за экономической нецелесообразности и технической сложности для целевого сегмента малого и среднего бизнеса.

Наиболее перспективными являются стратегии **R⬆2 (Нативная автоматизация)** и **R⬆5 (Умный агент)**. Рекомендация для компании Sphere («ꆜ») заключается в реализации **Гибридной стратегии адаптивной интеграции**:

1. **Ядро решения (Core):** Разработать **Smart Agent (R⬆5)** как основной продукт.  
   * Агент должен устанавливаться как служба Windows.  
   * Он должен использовать локальную зашифрованную БД для буферизации.  
   * По умолчанию он должен использовать **безопасные методы чтения** (например, через существующие представления/Views или хранимые процедуры, если они доступны), но иметь режим **Direct SQL Read (R⬆1)** с использованием уровня изоляции транзакций SET TRANSACTION ISOLATION LEVEL SNAPSHOT. Это позволит читать данные без наложения блокировок на пишущие транзакции пользователей, решая главную проблему R⬆1.  
2. **Событийный триггер (Event-Driven Fallback):**  
   * Для критических событий (например, «Новый заказ») агент должен уметь принимать сигналы от TPS. Для этого агент должен поднимать локальный HTTP-сервер (webhook listener) на localhost.  
   * В TPS (Resware/SoftPro) настраивается **Action List/Trigger (R⬆2)**, который просто «дергает» этот локальный веб-хук, сообщая ID измененного заказа.  
   * Получив сигнал, агент точечно запрашивает данные по этому ID из SQL. Это устраняет необходимость в постоянном тяжелом поллинге всей базы.

### **Критические факторы успеха и предостережения**

Юридическая чистота (Compliance First):  
Разработка должна вестись по принципу Privacy by Design. Инсталлятор агента должен:

* Явно запрашивать согласие администратора на доступ к базе данных.  
* Генерировать уникальные ключи шифрования для каждой инсталляции и хранить их с использованием **Windows Data Protection API (DPAPI)**, что является индустриальным стандартом для защиты секретов в среде Windows. Это обеспечит соответствие ALTA Best Practices Pillar 3.

Работа с облачными версиями:  
Необходимо честно предупредить клиента «ꆜ», что предложенное решение «локальной установки» технически ограничено средами On-Premise (сервер в офисе) и IaaS (виртуальная машина в облаке, подконтрольная клиенту). Для клиентов, использующих SaaS-версии (SoftPro Hosted, Resware Cloud), прямой доступ к файловой системе и SQL-портам закрыт на уровне сетевой инфраструктуры провайдера.7 Для этого сегмента рынка потребуется отдельная ветка разработки, использующая исключительно официальные API (SoftPro 360 API, Resware API), что потребует других бюджетов и сроков. Попытка использовать «универсальный» SQL-коннектор для облачных версий обречена на провал.  
**Вывод:** Реализация гибридного агента (R⬆5 + элементы R⬆2) позволит Sphere создать конкурентное преимущество, предложив рынку быстрое, надежное и, главное, безопасное решение проблемы интеграции, избежав при этом юридических ловушек, связанных со скрин-скрейпингом и нарушением стандартов безопасности данных.

#### **Works cited**

1. 16 CFR Part 314 -- Standards for Safeguarding Customer Information - eCFR, accessed November 24, 2025, [https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314)  
2. 16 CFR 314.4 -- Elements. - eCFR, accessed November 24, 2025, [https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314/section-314.4](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314/section-314.4)  
3. Title Insurance and Settlement Company Best Practices, accessed November 24, 2025, [https://www.alta.org/policies-and-standards/best-practices/download?bestPracID=97&type=pdf](https://www.alta.org/policies-and-standards/best-practices/download?bestPracID=97&type=pdf)  
4. ALTA Best Practices 4.2 (2025) | Compliance Guide - Closinglock, accessed November 24, 2025, [https://www.closinglock.com/2025-alta-best-practices-compliance/](https://www.closinglock.com/2025-alta-best-practices-compliance/)  
5. 4 Security Benefits of a Single Communication Portal - Qualia Insight, accessed November 24, 2025, [https://blog.qualia.com/single-portal-security-benefits/](https://blog.qualia.com/single-portal-security-benefits/)  
6. MARCH 2025 AMERICAN LAND TITLE ASSOCIATION, accessed November 24, 2025, [https://www.alta.org/news-and-publications/titlenews-magazine/2025/march_2025.pdf](https://www.alta.org/news-and-publications/titlenews-magazine/2025/march_2025.pdf)  
7. SoftPro System Requirements – Hosted, accessed November 24, 2025, [https://www.softprocorp.com/softpro-system-requirements-hosted/](https://www.softprocorp.com/softpro-system-requirements-hosted/)  
8. Sending Action Events to Resware - Support Hub - Snapdocs, accessed November 24, 2025, [https://support.snapdocs.com/action-event-resware](https://support.snapdocs.com/action-event-resware)  
9. SoftPro - SoftPro Eclosings for Complete Transactions, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/eclosings/](https://www.softprocorp.com/real-estate-software-solutions/eclosings/)  
10. SoftPro Select - Real Estate Closing Software, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-select/](https://www.softprocorp.com/real-estate-software-solutions/softpro-select/)  
11. SoftPro 360 Integrations, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/](https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/)  
12. SoftPro System Requirements – Standard, accessed November 24, 2025, [https://www.softprocorp.com/softpro-system-requirements-standard/](https://www.softprocorp.com/softpro-system-requirements-standard/)  
13. Notice of Final Rulemaking - Required Rulemaking on Personal Financial Data Rights - files.consumerfinance.gov., accessed November 24, 2025, [https://files.consumerfinance.gov/f/documents/cfpb_personal-financial-data-rights-final-rule_2024-10.pdf](https://files.consumerfinance.gov/f/documents/cfpb_personal-financial-data-rights-final-rule_2024-10.pdf)


# 24.
# 24.1.
`S⌖` ≔ (SoftPro)

# 24.2.
`S⌖-TNT` ≔ (Технология `S⌖`: Task Notification Tool)

# 24.3.
`S⌖-S` ≔ (Автоматизации `S⌖` Select для отправки структурированных электронных писем с вложениями)

# 24.4.
`S⌖-360` ≔ (Разработка официального адаптера `S⌖` 360)

# 25.
# 25.1.
`R⌖` ≔ (Resware)

# 25.2.
`R⌖-AE` ≔ (Технология `R⌖`: Action Events)

# 25.3.
`R⌖-Rest` ≔ (Rest API `R⌖`)

# 25.4.
`R⌖-SOAP` ≔ (SOAP API `R⌖`)
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1. `᛭T`
`Sꕊ`[§1-§3] ≔ `S⌖-TNT`

# 2. `᛭T`
Найди максимум информации о `Sꕊ`.
В частности, меня интересует:
1) Официальная документация к `Sꕊ`.
2) Суть `Sꕊ`.

# 3.
1) В своём анализе используй авторитетные источники информации на английском языке.
2) Свой ответ дай на русском языке. 
3) Не пиши никогда «Хороший вопрос» и другой подобный мусор в начале ответа.
Мне подобное пиздобольство не нужно.
4) Обязательно используй свой режим «Deep Research».
Твой ответ без режима «Deep Research» — гарантированно неверный.
5) На остальные вопросы не отвечай.
6) Не пустословь.
~~~~~~