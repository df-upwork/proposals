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
Благодаря вашему подробному описанию проблемы я выделил 2 наиболее вероятные причины, которые могут вызывать эту проблему независимо друг от друга или в сочетании.
Я излагаю их в пунктах 1 и 2 ниже.
Причина «WordPress sessions», на которую вам указала поддержка LearnDash — гораздо менее вероятна.
Я разбираю её в пункте 3.

1) Причина #1: Некорректная конфигурация кэширования или промежуточных слоев (Proxy/CDN).
1.1) Суть:
Эта причина наиболее вероятно проявляется по сценарию 1.1.1.
Сценарий 1.1.2 является гораздо менее вероятным по причине 1.2.3.
1.1.1) Неправильная работа Page Caching и Redirect Caching
Это наиболее распространенный механизм.
Аутентификация в WordPress основана на cookies (имена начинаются с `wordpress_logged_in_`).
Системы Page Caching (e.g., на уровне веб-сервера Apache, Proxy, CDN или плагины кэширования) должны быть настроены так, чтобы пропускать запрос к WordPress (Bypass Cache) при наличии этих cookies.
Использование механизма Vary Cache (варьирование кэша) в данном случае некорректно.
Значение аутентификационных cookies уникально для каждой сессии пользователя.
Варьирование кэша по уникальному значению приведет к созданию отдельной записи в кэше для каждой сессии.
Это полностью нивелирует эффективность Page Caching (Cache Hit Rate).
Если конфигурация некорректна, система кэширования игнорирует эти cookies и обрабатывает запрос как анонимный.
Когда авторизованный пользователь запрашивает защищенный URL (e.g., курс или урок), система кэширования может вернуть ответ, ранее сохраненный для гостя (Cache HIT).
Если для этого URL был закэширован ответ перенаправления (HTTP 302 на страницу входа, который генерируется для гостей), пользователь немедленно перенаправляется обратно на страницу входа.
В этом сценарии запрос обслуживается системой кэширования.
PHP может не выполняться вовсе (если кэш обслуживается веб-сервером Apache, Proxy или CDN).
Альтернативно, выполнение PHP может прерываться на ранней стадии (e.g., через механизм Drop-in `advanced-cache.php` при использовании плагинов кэширования WordPress).

1.1.2) Неправильная работа Cookie Stripping
Промежуточный слой (e.g., CDN, Proxy, Load Balancer или конфигурация веб-сервера Apache) может быть некорректно настроен на удаление (Stripping) аутентификационных cookies перед тем, как запрос достигнет приложения WordPress.
В этом сценарии запрос достигает ядра WordPress.
Однако, поскольку аутентификационные cookies отсутствуют, функция `is_user_logged_in()` возвращает `false`.
Чтобы защитить контент, WordPress (часто через функцию `auth_redirect()`) или LearnDash немедленно инициирует перенаправление на страницу входа.

1.2) Обоснование:
1.2.1) Вы пишете, очистка кэша или вход через режим инкогнито/приватный браузер часто «исправляет» проблему временно.
1.2.2) Это указывает на то, что пользователь получает некорректное состояние (Stale State).
Это является сильным индикатором получения закэшированного перенаправления (Сценарий 1.1.1).
Действия на стороне клиента (Client-Side Actions) не могут исправить конфигурацию сервера, но они могут временно обойти проблему за счет изменения состояния запроса или локального кэша.
Это происходит через 2 механизма:

1.2.2.1) Взаимодействие с Browser Cache.
В Сценарии 1.1.1 система Server-Side Caching некорректно возвращает закэшированный ответ перенаправления (e.g., HTTP 302).
Если этот ответ содержит заголовки управления кэшем (e.g., `Cache-Control` или `Expires`), добавленные caching layer, браузер может сохранить его локально.
В этом случае браузер выполняет перенаправление локально, не обращаясь к серверу повторно.
Очистка кэша браузера или режим инкогнито заставляют браузер отбросить локально сохраненный ответ и отправить новый запрос на сервер.

1.2.2.2) Временный обход Server-Side Cache.
Режим инкогнито или очистка cookies требуют повторного входа в систему.
Процесс входа (Login Process) изменяет характеристики сессии.
E.g., ответ `wp-login.php` содержит заголовок `Set-Cookie`.
Некоторые системы кэширования могут интерпретировать это как сигнал для временного отключения кэша для этой сессии (e.g., механизм Hit-for-Pass).
Также запрос, следующий сразу после входа, может содержать специфический заголовок `Referer`.
Эти факторы могут позволить первому запросу после входа успешно достичь WordPress, минуя некорректный закэшированный ответ.
Однако при последующих запросах, когда эти условия больше не выполняются, проблема возвращается.

1.2.3) Симптом 1.2.1 делает Сценарий 1.1.2 гораздо менее вероятным, чем Сценарий 1.1.1.
Если бы конфигурация инфраструктуры была однородной, постоянное правило удаления cookies применялось бы к каждому запросу, и действия на стороне клиента не приводили бы к временному решению.
Однако в неоднородной среде с несколькими серверами (e.g., за балансировщиком нагрузки), где конфигурация может быть неидентичной, возможно, что только часть узлов некорректно удаляет cookies.
В таком случае начало новой сессии может направить пользователя на корректно работающий узел, что создаст видимость временного исправления проблемы.

2) Причина #2: Неправильная работа Object Caching.
2.1) Суть:
В тегах проекта вы указали Redis и Memcached.
Если ваша система использует эти технологии для Object Caching, критически важные данные для аутентификации (Authentication) кэшируются в памяти.
WordPress использует Session Tokens (хранящиеся в `wp_usermeta`) для отслеживания состояния входа пользователя.
При высокой нагрузке состояние этих токенов в Object Cache может перестать соответствовать актуальному состоянию базы данных MariaDB (Inconsistent State).
Когда пользователь переходит на защищенную страницу, WordPress выполняет Authentication Check с помощью функции `wp_validate_auth_cookie()`.
При наличии Persistent Object Cache эта функция использует его как первичный источник данных (Primary Data Source) для получения Session Tokens (e.g., через `get_user_meta()`).
Если WordPress читает некорректный (устаревший или поврежденный) Session Token из кэша (Cache HIT), проверка завершается неудачей.
В результате WordPress считает пользователя неаутентифицированным (функция `is_user_logged_in()` возвращает `false`) и инициирует перенаправление на страницу входа.
Это может происходить по двум сценариям.

2.1.1) Stale Cache
Когда Session Tokens обновляются в базе данных (e.g., при входе, выходе или автоматическом продлении сессии), соответствующие данные в Object Cache должны быть инвалидированы (Invalidated) или обновлены.
Если механизм инвалидации работает некорректно (e.g., из-за ошибки в конфигурации, конфликта плагинов или проблем с репликацией базы данных), последующие запросы могут получить устаревшие данные (Stale Data) из кэша.
Использование устаревшего токена приводит к сбою Authentication.

2.1.2) Race Condition
При высокой нагрузке и параллельных запросах (e.g., AJAX) может возникнуть Race Condition при обновлении Session Tokens в кэше.
Хотя базовые операции (e.g., GET, SET) в Redis и Memcached являются атомарными (atomic), Race Condition возникает на уровне прикладной логики (Application Logic) в цикле Read-Modify-Write.
Этот цикл (приложение читает массив токенов из кэша, изменяет его в PHP и записывает обратно) не является атомарным.
Если несколько процессов одновременно изменяют этот массив, это может привести к потере обновления (Lost Update) и несогласованности состояния (Inconsistent State) в кэше.
Чтение некорректного состояния Session Tokens приводит к сбою Authentication.

2.2) Обоснование:
2.2.1) Сочетание высокой активности пользователей (которая есть на production, но нет на staging) и использования внешнего Object Cache создает условия для возникновения Stale Cache и Race Condition.
2.2.2) Этот механизм объясняет, почему пользователи перенаправляются, «even though they are already logged in».
Authentication cookie присутствует в браузере, но Authentication Check завершается неудачей из-за временной несогласованности Session Tokens в Object Cache во время конкретного запроса.

3) Причина #3: Проблемы с нативными PHP-сессиями (PHP Native Sessions).
3.1) Суть:
Эта причина гораздо менее вероятна (обоснование в пункте 3.2), но её следует рассмотреть, так как есть признаки использования PHP Native Sessions (`$_SESSION`) в вашей системе.
Хотя WordPress Core не использует `$_SESSION` для Authentication, некоторые плагины (e.g., BuddyBoss, указанный в тегах) могут их активировать.
Ваши действия по удалению файлов в `/tmp` (deleting /tmp session files) также предполагают их использование.
Если `$_SESSION` активны, это создает Concurrency Challenges при высокой нагрузке (которая есть на production, но нет на staging).
Конкретные проблемы зависят от конфигурации PHP `session.save_handler` и проявляются в двух основных сценариях:
3.1.1) Session Locking.
Если используется стандартный обработчик (`session.save_handler = files`), параллельные запросы (e.g., AJAX) блокируют друг друга при вызове `session_start()`.
Это приводит к Resource Contention и значительным задержкам.
3.1.2) Race Conditions.
Если используется внешний обработчик (e.g., Redis или Memcached, указанные в тегах) с отключенной или неэффективной блокировкой, параллельные запросы могут повреждать данные сессии (Data Corruption).

3.2) Обоснование низкой вероятности.
Эти сценарии вряд ли являются прямой причиной цикла перенаправлений из-за несоответствия симптомов (Symptom Mismatch).
3.2.1) Session Locking (пункт 3.1.1) приводит к Performance Bottlenecks.
Симптомы обычно включают ошибки сервера (e.g., HTTP `504 Gateway Timeout` или HTTP `500 Internal Server Error`), а не чистое перенаправление (HTTP `302`) на страницу входа.
3.2.2) Race Conditions (пункт 3.1.2) вызывают Data Corruption в `$_SESSION`.
Это может повлиять на логику плагинов (LearnDash/BuddyBoss), но не влияет на стандартный механизм Authentication WordPress Core.
WordPress Core Authentication основан на cookies и Session Tokens, а не на `$_SESSION`.
3.2.3) В целом, эти механизмы способствуют общей нестабильности системы под нагрузкой, а не конкретно этой проблеме с циклом входа.

4) «How would you approach debugging this issue without disrupting live students?»
4.1) Passive Diagnostics
Цель этапа  — идентифицировать слой, генерирующий перенаправление (CDN, Proxy, Apache или WordPress/PHP), без внесения изменений в код или конфигурацию Production.

4.1.1) Анализ конфигурации и HTTP Headers (Диагностика Причины #1).
4.1.1.1) Проанализировать конфигурацию всех слоев Page Caching (CDN, Proxy, модули Apache, плагины WordPress) на предмет правил обработки аутентификационных cookies.
4.2.2.2) Проанализировать HTTP Response Headers (e.g., `X-Cache`, `Cache-Control`, `Age`) для запросов к защищенным URL.
Наличие заголовков, указывающих на Cache HIT в ответе HTTP 302, подтвердит Сценарий 1.1.1.

4.1.2) Анализ Object Cache (Диагностика Причины #2).
4.1.2.1) Проанализировать конфигурацию интеграции Redis/Memcached.
4.1.2.2) Проанализировать операции кэша (GET/SET/DELETE), связанные с Session Tokens, во время тестовых попыток входа, используя инструменты Real-Time Monitoring (e.g., `redis-cli monitor`).
Это позволяет наблюдать за потенциальными несоответствиями (Stale Cache или Race Conditions) без сброса глобального кэша, который привел бы к принудительному выходу из системы всех студентов.

4.1.3) Анализ существующих логов.
Провести корреляционный анализ Apache `domlogs`, `login-audit.log` и логов вашего MU plugin для выявления паттернов перенаправлений.

4.2) Conditional Debugging
 Если пассивная диагностика не дала окончательного ответа — перейти к активным методам отладки.
4.2.1) Расширенное логирование (Enhanced Logging).
Модифицировать MU plugin для детального логирования процесса Authentication (e.g., результат `wp_validate_auth_cookie()`) и состояния cookies.
Это логирование будет активироваться только при наличии специального отладочного cookie или для конкретного тестового `user_id`.
4.2.2) Контролируемый обход кэша (Controlled Cache Bypass).
Временно настроить правила для принудительного обхода Page Cache только для тестовых запросов.
Использовать фильтр `wp_using_ext_object_cache`, чтобы временно отключить Object Cache только для моей тестовой сессии.

4.3) Staging Reproduction
Поскольку проблема зависит от нагрузки — провести Load Testing на Staging среде.
Используя инструменты (e.g., Apache JMeter или k6), симулировать параллельные аутентифицированные сессии для искусственного создания Race Conditions (Причина 2.1.2).
Это позволит безопасно воспроизвести проблему и протестировать исправления перед развертыванием на Production.

5) «What’s your process for isolating a plugin conflict vs. WordPress core issue?»
5.1) Общий принцип: Systematic Isolation.
Cистематически упрощать Runtime Environment до минимальной конфигурации (Vanilla WordPress).
Это позволяет определить, вызван ли сбой кодом сторонних компонентов (плагины или тема) или базовой платформой (WordPress Core или инфраструктура).

5.2) Процедура изоляции на Production.
5.2.1) Создание Clean Environment.
Использовать технику Conditional Deactivation.
Это реализуется через Must-Use Plugin (`mu-plugin`) или специализированные инструменты (e.g., плагин «Health Check & Troubleshooting»).
Этот метод создает Clean Environment (деактивирует плагины и переключает тему на стандартную, e.g., Twenty Twenty-Five) только для моей сессии администратора (Admin Session).
Другие пользователи продолжают работу с сайтом без изменений.

5.2.2) Baseline Check.
Попытаться воспроизвести проблему в изолированном Clean Environment (пункт 5.2.1).
5.2.2.1) Если проблема воспроизводится — это указывает на проблему в WordPress Core, Must-Use Plugins (включая ваш Custom MU plugin для логирования) или конфигурации инфраструктуры (Server Configuration, Caching Layers).
В этом случае перейти к анализу инфраструктуры и WordPress Core (пункт 5.2.4).
5.3.2.2) Если проблема не воспроизводится - это подтверждает Plugin Conflict или Theme Conflict.
В этом случае перейти к изоляции конфликтующего компонента (пункт 5.2.3).

5.2.3) Изоляция конфликтующего компонента.
5.2.3.1) Сохраняя изолированную сессию,активировать компоненты.
5.2.3.2) Сначала активировать текущую Theme.
Если проблема возвращается — источник конфликта находится в теме.
5.2.3.3) Если нет — активировать критически важные плагины (LearnDash, BuddyBoss).
Затем использовать Binary Search Method: активировать половину оставшихся плагинов и проверить воспроизведение проблемы.
Повторять процесс, сужая поиск до идентификации конкретного плагина или комбинации плагинов, вызывающих конфликт.

5.2.4) Дифференциация WordPress Core и инфраструктуры.
5.2.4.1) Проверить целостность файлов WordPress Core (File Integrity Check) на предмет модификаций.
5.2.4.2) Проанализировать конфигурацию инфраструктуры (Apache, PHP-FPM, Redis/Memcached, правила Caching), так как это наиболее вероятные причины для Production-Only проблем (как описано в пунктах 1-3).
5.3.4.3) Если предыдущие шаги не выявляют причину — рассмотреть вероятность ошибки в WordPress Core.
В этом случае провести глубокую отладку (Deep Debugging) с использованием Xdebug для анализа Authentication Flow и искать известные проблемы (Known Issues) в WordPress Trac.
```
~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
Thanks to your detailed description of the problem, I have identified the 2 most likely causes, which can cause this problem independently or in combination.
I outline them in points 1 and 2 below.
The «WordPress sessions» cause, to which LearnDash support pointed you, is far less likely.
I discuss it in point 3.
1) Cause #1: Incorrect configuration of caching or intermediary layers (Proxy/CDN).
1.1) Essence:
This cause most likely manifests under scenario 1.1.1.
Scenario 1.1.2 is much less likely for the reason in point 1.2.3.
1.1.1) Incorrect operation of Page Caching and Redirect Caching
This is the most common mechanism.
WordPress authentication is based on cookies (names start with `wordpress_logged_in_`).
Page Caching systems (e.g., at the web server level, such as Apache, Proxy, CDN, or caching plugins) must be configured to Bypass Cache when these cookies are present.
Using the Vary Cache mechanism is incorrect in this case.
The value of authentication cookies is unique for each user session.
Varying the cache based on a unique value will create a separate cache entry for each session.
This completely negates the effectiveness of Page Caching (Cache Hit Rate).
If the configuration is incorrect, the caching system ignores these cookies and processes the request as an anonymous one.
When an authorized user requests a protected URL (e.g., a course or a lesson), the caching system may return a response previously saved for a guest (Cache HIT).
If a redirection response (an HTTP 302 to the login page, which is generated for guests) has been cached for this URL, the user is immediately redirected back to the login page.
In this scenario, the request is served by the caching system.
PHP may not execute at all (if the cache is served by the Apache web server, a Proxy, or a CDN).
Alternatively, PHP execution may be interrupted at an early stage (e.g., via the `advanced-cache.php` Drop-in mechanism when using WordPress caching plugins).
1.1.2) Improper Cookie Stripping
An intermediate layer (e.g., a CDN, Proxy, Load Balancer, or the Apache web server configuration) may be incorrectly configured to strip authentication cookies before the request reaches the WordPress application.
In this scenario, the request reaches the WordPress core.
However, since the authentication cookies are absent, the `is_user_logged_in()` function returns `false`.
To protect the content, WordPress (often via the `auth_redirect()` function) or LearnDash immediately initiates a redirection to the login page.
1.2) Rationale:
1.2.1) You write that clearing the cache or logging in via an incognito/private browser often «fixes» the issue temporarily.
1.2.2) This indicates that the user is receiving a stale state.
This is a strong indicator of receiving a cached redirect (Scenario 1.1.1).
Client-side actions cannot fix the server configuration, but they can temporarily bypass the issue by changing the state of the request or the local cache.
This occurs through 2 mechanisms:
1.2.2.1) Interaction with Browser Cache.
In Scenario 1.1.1, the Server-Side Caching system incorrectly returns a cached redirect response (e.g., HTTP 302).
If this response contains cache control headers (e.g., `Cache-Control` or `Expires`) added by the caching layer, the browser may store it locally.
In this case, the browser performs the redirection locally without contacting the server again.
Clearing the browser cache or using incognito mode forces the browser to discard the locally stored response and send a new request to the server.
1.2.2.2) Temporary bypass of Server-Side Cache.
Incognito mode or clearing cookies require re-login.
The login process changes the session characteristics.
E.g., the `wp-login.php` response contains the `Set-Cookie` header.
Some caching systems may interpret this as a signal to temporarily disable the cache for this session (e.g., the Hit-for-Pass mechanism).
Also, the request immediately following login may contain a specific `Referer` header.
These factors may allow the first request after login to successfully reach WordPress, bypassing the incorrect cached response.
However, on subsequent requests, when these conditions are no longer met, the problem returns.
1.2.3) Symptom 1.2.1 makes Scenario 1.1.2 much less likely than Scenario 1.1.1.
If the infrastructure configuration were homogeneous, a persistent cookie stripping rule would be applied to every request, and client-side actions would not result in a temporary solution.
However, in a non-homogeneous environment with multiple servers (e.g., behind a load balancer), where the configuration might not be identical, it is possible that only some of the nodes incorrectly strip cookies.
In such a case, starting a new session might direct the user to a correctly functioning node, which would create the appearance of a temporary fix for the problem.
2) Cause #2: Incorrect operation of Object Caching.
2.1) Essence:
In the project tags, you have specified Redis and Memcached.
If your system uses these technologies for Object Caching, critical data for authentication are cached in memory.
WordPress uses Session Tokens (stored in `wp_usermeta`) to track the user's login state.
Under high load, the state of these tokens in the Object Cache can become inconsistent with the current state of the MariaDB database.
When a user navigates to a protected page, WordPress performs an Authentication Check using the `wp_validate_auth_cookie()` function.
With a Persistent Object Cache, this function uses it as the primary data source to retrieve Session Tokens (e.g., via `get_user_meta()`).
If WordPress reads an incorrect (stale or corrupted) Session Token from the cache (Cache HIT), the authentication check fails.
As a result, WordPress considers the user unauthenticated (the `is_user_logged_in()` function returns `false`) and initiates a redirection to the login page.
This can occur in two scenarios.
2.1.1) Stale Cache
When Session Tokens are updated in the database (e.g., upon login, logout, or automatic session extension), the corresponding data in the Object Cache must be invalidated or updated.
If the invalidation mechanism works incorrectly (e.g., due to a configuration error, a plugin conflict, or database replication issues), subsequent requests may receive stale data from the cache.
Using a stale token leads to an Authentication failure.
2.1.2) Race Condition
Under high load and concurrent requests (e.g., AJAX), a Race Condition can occur when updating Session Tokens in the cache.
Although the basic operations (e.g., GET, SET) in Redis and Memcached are atomic, the Race Condition occurs at the Application Logic level in the Read-Modify-Write cycle.
This cycle (the application reads the token array from the cache, modifies it in PHP, and writes it back) is not atomic.
If multiple processes simultaneously modify this array, it can lead to a Lost Update and an Inconsistent State in the cache.
Reading the incorrect state of Session Tokens leads to an Authentication failure.
2.2) Rationale:
2.2.1) The combination of high user activity (which is present on production but not on staging) and the use of an external Object Cache creates the conditions for Stale Cache and Race Condition.
2.2.2) This mechanism explains why users are redirected, «even though they are already logged in».
The Authentication cookie is present in the browser, but the Authentication Check fails due to a temporary inconsistency of the Session Tokens in the Object Cache during a specific request.
3) Cause #3: Problems with PHP Native Sessions.
3.1) Essence:
This cause is far less likely (rationale in point 3.2), but it should be considered, as there are signs of the use of PHP Native Sessions (`$_SESSION`) in your system.
Although WordPress Core does not use `$_SESSION` for Authentication, some plugins (e.g., BuddyBoss, mentioned in the tags) can activate them.
Your actions of deleting `/tmp` session files also suggest their use.
If `$_SESSION` are active, this creates Concurrency Challenges under high load (which exists on production but not on staging).
Specific problems depend on the PHP `session.save_handler` configuration and manifest in 2 main scenarios:
3.1.1) Session Locking.
If the standard handler (`session.save_handler = files`) is used, parallel requests (e.g., AJAX) block each other when calling `session_start()`.
This leads to Resource Contention and significant delays.
3.1.2) Race Conditions.
If an external handler (e.g., Redis or Memcached, mentioned in the tags) is used with disabled or ineffective locking, parallel requests can corrupt session data (Data Corruption).
3.2) Rationale for low probability.
These scenarios are unlikely to be the direct cause of the redirection loop due to a symptom mismatch.
3.2.1) Session Locking (point 3.1.1) leads to Performance Bottlenecks.
Symptoms typically include server errors (e.g., HTTP `504 Gateway Timeout` or HTTP `500 Internal Server Error`), rather than a pure redirect (HTTP `302`) to the login page.

~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
5.2.4) Дифференциация WordPress Core и инфраструктуры.
5.2.4.1) Проверить целостность файлов WordPress Core (File Integrity Check) на предмет модификаций.
5.2.4.2) Проанализировать конфигурацию инфраструктуры (Apache, PHP-FPM, Redis/Memcached, правила Caching), так как это наиболее вероятные причины для Production-Only проблем (как описано в пунктах 1-3).
5.3.4.3) Если предыдущие шаги не выявляют причину — рассмотреть вероятность ошибки в WordPress Core.
В этом случае провести глубокую отладку (Deep Debugging) с использованием Xdebug для анализа Authentication Flow и искать известные проблемы (Known Issues) в WordPress Trac.
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