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
߷⠿ ≔ ⠿~ (приложеные к этому запросу файлы)
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
Сегодня 2025-10-01.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021973162834964667109

## 2.2. Title
Urgent: WordPress/LearnDash Developer Needed to Fix Login Redirection Issue

## 2.3. Description
`PD` ≔ 
```text
Users are being redirected back to the login page when trying to access courses or lessons, even though they are already logged in.

This creates daily frustration for users and a massive support burden for our staff.

We’ve tried numerous solutions with different developers, and even LearnDash support has pointed out it’s likely tied to WordPress sessions, cookies, or permalink handling. 
Our current developer has been investigating, but we need someone who can come in quickly, isolate the root cause, and implement a permanent fix.

# What’s Happening:
- Users log in successfully, but when they click into a course/lesson, they are redirected back to the login page.
- Clearing cache or logging in via an incognito/private browser often “fixes” the issue temporarily.
- We’ve tested staging, but staging doesn’t replicate live user sessions (problem only shows with real user activity).

# Environment Details:
- Platform: WordPress &#43; LearnDash LMS
- Hosting: cPanel/WHM (Apache, PHP-FPM, MariaDB), with Google Cloud storage integration in progress

# Logs we have:
- Custom MU plugin logging logins, cookies, and referrers
- login-audit.log tracking user logins in real time
- Apache/domlogs

# What We’ve Already Tried:
- Clearing and resetting server/session caches
- Restarting Apache/PHP-FPM
- Flushing OPcache, deleting /tmp session files
- Creating custom logging MU plugin to track login/session cookies
- Testing staging (problem does not reproduce there — only live with active users)

# What We Need From You:
- Diagnose and fix the root cause of the login redirection issue
- Audit session/cookie handling (WordPress core &#43; LearnDash &#43; any custom plugins)
- Ensure the fix works across all courses and lessons without having to manually update permalinks
- Provide a clear report of the root cause and implemented solution so we can maintain it long term

# Bonus Points if You Can:
- Suggest and implement hardening for session handling, caching, and redirects
- Audit our LearnDash &#43; WordPress setup for other performance or stability issues
- Set up better logging so future issues can be quickly diagnosed

# Requirements:
- Proven experience with WordPress core session/auth systems
- Deep knowledge of LearnDash (courses, lessons, redirects, logins)
- Strong debugging skills (server logs, PHP logs, WordPress hooks/filters)
- Able to start immediately and work directly on our live system during peak hours (with our oversight)

# Deliverables
1. Permanent fix to the login redirection issue
2. Documentation of root cause + steps taken
3. Recommendations for long-term maintenance
```

## 2.4. Tags
WordPress core debugging (authentication, sessions, redirects)
LearnDash LMS deep experience (courses, lessons, login/session flows)
PHP (advanced debugging and plugin development)
Apache/Nginx server configuration (cPanel/WHM environments
Cookie/session handling in WordPress
MySQL query troubleshooting
BuddyBoss
Redis, Memcached, Opcache
sign-on (SSO
Google Cloud Storage

## 2.5. Questions
### 2.5.1.
Have you fixed login redirection/session loop issues in WordPress or LearnDash before? 
If yes, please describe the root cause and solution.

### 2.5.2.
How would you approach debugging this issue without disrupting live students?

### 2.5.3.
What’s your process for isolating a plugin conflict vs. WordPress core issue?

### 2.5.4.
Do you have experience with multi-server environments or caching conflicts

### 2.5.5.
How quickly could you start and provide an initial root cause analysis?

# 5. Информация о `ꆜ`
## 5.1. Местоположение

United States
Lake Mary

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
10-99

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Oct 11, 2017
### 5.3.2. Hire rate (%)
81
### 5.3.3. Количество опубликованных проектов (jobs posted)
77
### 5.3.4. Total spent (USD)
$162K
### 5.3.5. Количество оплаченных часов в почасовых проектах
11996
### 5.3.6. Средняя почасовая ставка (USD)
12.95

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
Users are being redirected back to the login page when trying to access courses or lessons, even though they are already logged in.
~~~
```


 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1
## 1.1.
`Cᛘ⠿` ≔ ⠿~ (Возможные причины `P†`)

## 1.2.
`Cᛘᵢ` : `Cᛘ⠿`

## 1.3.
? `Cᛘᵢ`

## 1.4.
`Pⰳ(Cᛘᵢ)` ≔ (Правдоподобность гипотезы `Cᛘᵢ`)

# 2. `᛭T`
Действуй пошагово
## 2.1.
Найди `Cᛘ⠿`.
## 2.2.
Проанализируй `Cᛘ⠿`.
Для этого для каждого  `Cᛘᵢ` выяви:
### 2.2.1.
Доводы за `Pⰳ(Cᛘᵢ)`.
### 2.2.2.
Доводы против `Pⰳ(Cᛘᵢ)`.
## 2.3.
Оцени `Pⰳ(Cᛘᵢ)` по шкале от 0 до 100:
- 0 означает, что ты полностью уверен, что `Cᛘᵢ` ложна.
- 100 означает, что ты полностью уверен, что `Cᛘᵢ` истинна.
## 2.4.
Выскажи свой вердикт.

# 3. Требования к источникам информации / Общие
## 3.1.
В своём анализе используй авторитетные источники информации на английском языке.

# 4. Требования к источникам информации / При анализе юридических вопросов
## 4.1.
В своём анализе используй официальные юридические источники информации.

## 4.2.
В своём ответе сошлись на конкретные пункты конкретных нормативных актов, с конкретными цитатами из них.
Цитаты давай как в оригинальном варианте (как они записаны в нормативном акте), так и в своём переводе.

# 5. Требования к процессу анализа
## 5.1.
Не решай задачи, не относящиеся к `᛭T`.
## 5.2.
Обязательно используй свой режим «Deep Research».
Твой ответ без режима «Deep Research» — гарантированно неверный.

# 6. Требования к ответу
## 6.1.
Уже известную мне информацию не пересказывай.

## 6.2.
Свой ответ дай на русском языке. 


~~~~~~