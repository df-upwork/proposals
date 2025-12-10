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
1) По моему опыту, ваша проблема с высокой вероятностью вызвана причинами, описанными в пунктах 2 и 3 ниже.
Обе гипотезы хорошо объясняют наблюдаемые симптомы, и они могут присутствовать одновременно.
2) Превышение лимитов размера HTTP-заголовков на OCI LB
2.1) OCI Load Balancers имеют строгие ограничения на максимальный размер HTTP-заголовков ответа от бэкенда. 
SvelteKit при выполнении SSR генерирует обширные заголовки, в частности, заголовок `Link` для предварительной загрузки ресурсов (preload assets), а также большие `Set-Cookie`. 
Если размер заголовков превышает лимит OCI LB, балансировщик возвращает 502.
2.2) Эта гипотеза точно объясняет разницу между SSR (большие заголовки) и SPA-навигацией (маленькие заголовки API-ответов).
2.3) Эта гипотеза также объясняет, почему прямой доступ работает: Nginx и браузеры имеют более высокие лимиты, чем OCI LB.
2.4) OCI Load Balancers имеют фиксированный лимит на максимальный размер HTTP-заголовков ответа (Response Headers) от бэкенда.
Согласно документу поддержки Oracle (Doc ID 2603461.1), этот лимит составляет 8KB.
Превышение этого лимита приводит к ошибке 502, даже если бэкенд ответил 200 OK.
Документация OCI описывает настройку HTTP Header Rules в OCI LB Rule Sets, но она позволяет увеличить лимит только для заголовков запроса (Request Headers, превышение которого вызывает ошибку 400), и не влияет на лимит заголовков ответа.
Следовательно, для решения этой проблемы необходимо уменьшить размер заголовков, генерируемых SvelteKit во время SSR (e.g., оптимизация `Link` preload заголовков или `Set-Cookie`).
3) Несоответствие таймаутов Keep-Alive
3.1) Ошибка 502 может возникать из-за race condition при повторном использовании постоянных соединений (Keep-Alive).
OCI LB поддерживает пул соединений с бэкендом (Nginx).
Если Nginx закрывает соединение (по достижении своего `keepalive_timeout`) раньше, чем истекает LB-to-Backend Idle Timeout на балансировщике, LB может попытаться отправить новый запрос через уже закрытое соединение, что приводит к ошибке 502.
3.2) Это классическая причина intermittent ошибок 502, что прямо соответствует вашему описанию «often spits out a 502».
3.3) Проблема проявляется только через LB, так как при прямом доступе этот механизм управления соединениями не задействован.
3.4) Критически важно, чтобы таймаут Keep-Alive на бэкенде (Nginx `keepalive_timeout`) был больше, чем LB-to-Backend Idle Timeout на OCI LB.
Согласно документации OCI («Load Balancer Timeout Connection Settings»), OCI LB закрывает соединения с бэкендом, которые простаивают более 300 секунд (фиксированное значение LB-to-Backend Idle Timeout).
Если `keepalive_timeout` в Nginx меньше этого значения (e.g., стандартное значение 75s), это создает идеальные условия для возникновения проблемы.
Документация OCI рекомендует установить таймаут на бэкенде не менее 310 секунд для предотвращения ошибок 502.
Увеличение Listener Idle Timeout (который определяет время простоя во время фазы HTTP-запроса/ответа, а не между запросами), которое вы предприняли, не влияет на этот механизм.
3.5) Эта гипотеза хорошо объясняет, почему проблема возникает преимущественно при SSR (обновление страницы).
SSR-запросы часто происходят после периода бездействия пользователя.
Если время простоя превышает `keepalive_timeout` Nginx, но меньше LB-to-Backend Idle Timeout (300s), возникает описанное состояние гонки.
SPA-навигация, напротив, генерирует частые запросы, которые поддерживают соединение в активном состоянии и предотвращают достижение idle-таймаутов.
~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
1) In my experience, your issue is highly likely caused by the reasons described in points 2 and 3 below.
Both hypotheses explain the observed symptoms well, and they can be present simultaneously.
2) Exceeding HTTP header size limits on the OCI LB.
2.1) OCI Load Balancers have strict limits on the maximum size of response headers from the backend. When performing SSR, SvelteKit generates large headers, particularly the `Link` header for preload assets, as well as large `Set-Cookie` headers. If the header size exceeds the OCI LB limit, the load balancer returns a 502.
2.2) This hypothesis precisely explains the difference between SSR (large headers) and SPA navigation (small API response headers).
2.3) This hypothesis also explains why direct access works: Nginx and browsers have higher limits than the OCI LB.
2.4) OCI Load Balancers have a fixed limit on the maximum size of HTTP response headers (Response Headers) from the backend.
According to Oracle, this limit is 8KB: https://support.oracle.com/knowledge/Oracle%20Cloud/2603461_1.html
Exceeding this limit results in a 502 error, even if the backend responded with 200 OK.
The OCI documentation describes the configuration of HTTP Header Rules in OCI LB Rule Sets, but it allows increasing the limit only for request headers (Request Headers, exceeding which causes a 400 error), and does not affect the response headers limit.
Therefore, to solve this problem, it is necessary to reduce the size of the headers generated by SvelteKit during SSR (e.g., by optimizing `Link` preload headers or `Set-Cookie`).
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
Если время простоя превышает `keepalive_timeout` Nginx, но меньше LB-to-Backend Idle Timeout (300s), возникает описанное состояние гонки.
SPA-навигация, напротив, генерирует частые запросы, которые поддерживают соединение в активном состоянии и предотвращают достижение idle-таймаутов.
~~~

# 5. `᛭T`
Переведи `F` на `L_TARGET`, с учётом:
- контекста `D`
- `D2`: уже переведённой части `D`
- `᛭O`

# 6. Правила перевода
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
### 6.3.3.
Не форматируй веб-ссылки посредством Markdown, если они не отформатированы так в оригинале. 
Например, не пиши так:
```
[https://www.eca.web.tr/eca-nita-esnek-uclu-eviye-bataryasi-beyaz-102118110-308](https://www.eca.web.tr/eca-nita-esnek-uclu-eviye-bataryasi-beyaz-102118110-308)
```
если в оригинале скобок `[]()` нет.

## 6.4.
Форматируй перевод в точности как оригинал. 
В частности:
*) каждый абзац должен содержать ровно одно предложение
*) между абзацами не должно оставаться пустых строк.
*) кавычки используй те же, что и в оригинале: «» и ``.

## 6.5.
Не используй сокращения типа «don't». Все подобные фразы пиши полностью: «do not».

## 6.6.
Не используй жаргон.
Вместо этого используй официальные термины.
### 6.6.1.
В частности, фразы в кавычках используй только в том случае, когда они являются точными цитатами.
Не используй фразы в кавычках для применения жаргонных фраз.
Например, следующий фрагмент текста недопустим, потому что там используется жаргонная фраза «пролетел»: 
```
Например, код, который пушит данные о покупке, подключён асинхронно и загружается с небольшой задержкой, а триггер уже «пролетел».
```

## 6.7.
При обсуждении программного обеспечения используй точные официальные термины на английском языке: именно в том виде, как они указаны в официальной англоязычной документации к этому программному обеспечению.

## 6.8.
Не используй «you need» и другие подобные обращённые к клиенту фразы, перекладывающие действия на него.
Помни: я пишу клиенту или потенциальному клиенту.
Делать в любом случае буду я, а не клиент.
Вместо «you need» используй 2 альтернативы:
### 6.8.1.
Нейтральные фразы типа «it is necessary».
### 6.8.2.
Глаголы в неопределённой форме.
Например, во фрагменте ниже использованы подобные глаголы «set up», «create»:
```
1.2) Set up the transfer of login events from WordPress to Power BI using Fabric / OneLake.
1.2.1) Set up a «Data Pipeline» from the WordPress database table that stores login events (see point 1.1) to Fabric / OneLake.
1.2.2) Set up a connection from Power BI to Fabric / OneLake to pass login events.
1.3) Create the data model in Power BI.
```
Обрати внимание, в этом фрагменте не говорится, кто именно будет выполнять описанные действия: ответственность не перекладывается на клиента, в отличие от «you need».

## 6.9.
Никогда не переводи понятие «сайт» / «веб-сайт» как «site». 
Вместо этого используй форму «website»: это является более профессиональным.

## 6.10.
Никогда не переводи понятие «пункт нумерованного списка» как «item».
Всегда переводи это как «point».

## 6.11.
Вместо «for example» используй «e.g.».
При этом не забывай, что в начале предложения эта фраза должна начинатся с заглавной буквы: «E.g.»
~~~~~~