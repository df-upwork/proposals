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


# 7.
## 7.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 7.2.
Содержание `Aᨀ`:
~~~markdown
1) In my experience, your issue is highly likely caused by the reasons described in points 2 and 3 below.
Both hypotheses explain the observed symptoms well, and they can occur simultaneously.
2) Exceeding HTTP header size limits on the OCI LB.
2.1) OCI Load Balancers have strict limits on the maximum size of response headers from the backend. When performing SSR, SvelteKit generates large headers, particularly the `Link` header for preload assets and large `Set-Cookie` headers. 
If the header size exceeds the OCI LB limit, the load balancer returns a 502.
2.2) This hypothesis precisely explains the difference between SSR (large headers) and SPA navigation (small API response headers).
2.3) This hypothesis also explains why direct access works: Nginx and browsers have higher limits than the OCI LB.
2.4) The fixed limit for the maximum size of HTTP response headers from the backend is 8KB, according to Oracle: https://support.oracle.com/knowledge/Oracle%20Cloud/2603461_1.html
Exceeding this limit results in a 502 error, even if the backend responds with 200 OK.
The OCI documentation describes the configuration of HTTP Header Rules in OCI LB Rule Sets. 
However, these rules only allow increasing the limit for request headers (exceeding this limit causes a 400 error); they cannot be used to adjust the response header limit.
Therefore, solving this problem requires reducing the size of the headers generated by SvelteKit during SSR (e.g., by optimizing `Link` preload headers or `Set-Cookie`).
3) `Keep-Alive` timeouts mismatch.
3.1) A 502 error can occur due to a race condition when reusing persistent connections (`Keep-Alive`).
The OCI LB maintains a connection pool with the backend (Nginx).
If Nginx closes a persistent connection (due to its `keepalive_timeout`) while the OCI LB still considers that connection active (because the LB-to-Backend Idle Timeout has not yet expired), a race condition occurs. 
The LB may attempt to reuse the closed connection, resulting in a 502 error.
3.2) This is a classic cause of intermittent 502 errors, which directly corresponds to your description «often spits out a 502».
3.3) The problem occurs only through the LB because this connection management mechanism is not involved when accessing the backend directly.
3.4) The `Keep-Alive` timeout on the backend (Nginx `keepalive_timeout`) must be greater than the LB-to-Backend Idle Timeout on the OCI LB.
According to the OCI documentation («Load Balancer Timeout Connection Settings»), the OCI LB closes connections to the backend that have been idle for more than 300 seconds (a fixed value for the LB-to-Backend Idle Timeout).
If the `keepalive_timeout` in Nginx is less than this value (e.g., the default value of 75s), this creates ideal conditions for the problem to occur.
The OCI documentation recommends setting the timeout on the backend to at least 310 seconds to prevent 502 errors.
Increasing the Listener Idle Timeout (which defines the idle time during the HTTP request/response phase, not between requests), which you have already tried, does not affect this mechanism.
3.5) This hypothesis effectively explains why the problem occurs predominantly during SSR (page refresh).
SSR requests often occur after a period of user inactivity.
If the idle time exceeds the Nginx `keepalive_timeout` but is less than the LB-to-Backend Idle Timeout (300s), the described race condition occurs.
SPA navigation, in contrast, generates frequent requests that keep the connection active and prevent the idle timeouts from being reached.
---
My GitHub profile: https://github.com/dmitrii-fediuk
~~~
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1.
`Fᨀ` ≔ (фрагмент `Aᨀ`)

## 1.2.
Содержание `Fᨀ`:
~~~markdown
3) `Keep-Alive` timeouts mismatch.
3.1) A 502 error can occur due to a race condition when reusing persistent connections (`Keep-Alive`).
The OCI LB maintains a connection pool with the backend (Nginx).
If Nginx closes a persistent connection (due to its `keepalive_timeout`) while the OCI LB still considers that connection active (because the LB-to-Backend Idle Timeout has not yet expired), a race condition occurs. 
The LB may attempt to reuse the closed connection, resulting in a 502 error.
3.2) This is a classic cause of intermittent 502 errors, which directly corresponds to your description «often spits out a 502».
3.3) The problem occurs only through the LB because this connection management mechanism is not involved when accessing the backend directly.
3.4) The `Keep-Alive` timeout on the backend (Nginx `keepalive_timeout`) must be greater than the LB-to-Backend Idle Timeout on the OCI LB.
According to the OCI documentation («Load Balancer Timeout Connection Settings»), the OCI LB closes connections to the backend that have been idle for more than 300 seconds (a fixed value for the LB-to-Backend Idle Timeout).
If the `keepalive_timeout` in Nginx is less than this value (e.g., the default value of 75s), this creates ideal conditions for the problem to occur.
The OCI documentation recommends setting the timeout on the backend to at least 310 seconds to prevent 502 errors.
Increasing the Listener Idle Timeout (which defines the idle time during the HTTP request/response phase, not between requests), which you have already tried, does not affect this mechanism.
3.5) This hypothesis effectively explains why the problem occurs predominantly during SSR (page refresh).
SSR requests often occur after a period of user inactivity.
If the idle time exceeds the Nginx `keepalive_timeout` but is less than the LB-to-Backend Idle Timeout (300s), the described race condition occurs.
SPA navigation, in contrast, generates frequent requests that keep the connection active and prevent the idle timeouts from being reached.
~~~ 

# 2. `᛭T`
Проанализируй `Fᨀ`:
## 2.1.
1) Есть ли там языковые ошибки?
2) Можно ли улучшить формулировки написанного там?

# 3. Требования к твоему ответу
## 3.1.
Отвечай на русском языке.
## 3.2.
Мой вопрос не пересказывай.
## 3.3.
Уже сформулированную мной информацию не пересказывай.
## 3.4.
Писать свою версию `Fᨀ` не нужно: просто укажи свои замечания по пунктам.
## 3.5.
До и после списка замечаний ничего не пиши.
## 3.6.
Нумерация замечаний должна быть сквозной.
## 3.7.
К угловым кавычкам `«»` не придирайся.
## 3.8
К числительным, записанным цифрами вместо прописи, не придирайся. 
Наоборот: у меня все числительные должны писаться цифрами.
## 3.9.
К backticks для аббревиатур не придирайся.
Пример: «the Notary Law (hereinafter `N`)».
## 3.10.
Для каждого замечания указывай твоё предложение по его устранению: конкретный фрагамент текста.
~~~~~~