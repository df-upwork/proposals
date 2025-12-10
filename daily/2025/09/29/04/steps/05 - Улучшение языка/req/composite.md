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
Сегодня 2025-09-29.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021971759158754297021

## 2.2. Title
Expert Nginx SME for Reverse Proxy Setup

## 2.3. Description
`PD` ≔ 
```text
I need expert level nginx SME for setting up a reverse proxy. Need to add a nginx as a reverse proxy for accessing a site in a restricted network. I am currently getting cookies error when trying to login to the site.

# Deliverables
- Set up Nginx as a reverse proxy
- Resolve cookies error during login
- Ensure secure access to restricted network site
```

## 2.4. Tags
NGINX
Linux System Administration
Apache Administration
Nginx
Linux
Ubuntu


## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
Individual client

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Nov 20, 2015
### 5.3.2. Hire rate (%)
49
### 5.3.3. Количество опубликованных проектов (jobs posted)
45
### 5.3.4. Total spent (USD)
9.7K
### 5.3.5. Количество оплаченных часов в почасовых проектах
245
### 5.3.6. Средняя почасовая ставка (USD)
32.73

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
I am currently getting cookies error when trying to login to the site
~~~
```

# 7.
## 7.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 7.2.
Содержание `Aᨀ`:
~~~markdown
0) In my experience, your cookie error is most likely caused by the reverse proxy server changing the interaction context between the client and the backend application.
Cookies set by the backend for the internal context (domain, path, protocol) become invalid for the client's browser.
I consider 5 hypotheses to be the most likely in your situation.
I outline them in points 1-5 below.
1) Hypothesis #1: Cookie `Domain` attribute mismatch.
1.1) The essence
The backend application sets a Cookie with a `Domain` attribute that matches its internal address (e.g., `internal.local`).
The client's browser, which connects via the external address (e.g., `proxy.com`), rejects this Cookie due to the domain mismatch.
1.2) Plausibility arguments
1.2.1) In the project description, you specified access to the website in a «restricted network».
This strongly implies the use of internal domain names that differ from external ones.
1.2.2) By default, Nginx does not modify the `Domain` attribute in the `Set-Cookie` header transmitted from the backend.
The `proxy_cookie_domain` directive is required to rewrite this attribute correctly.
2) Hypothesis #2: Issues with SSL/TLS termination and the `Secure` flag.
2.1) The essence
Nginx terminates SSL/TLS (accepts HTTPS from the client), but interacts with the backend over insecure HTTP.
The backend is not aware of the original secure connection and perceives the request as HTTP.
This leads to authentication errors because the backend generates incorrect absolute URLs for redirection (using `http://` instead of `https://`) or it refuses to establish a session, considering the transport to be insecure.
2.2) Plausibility arguments
2.2.1) Your phrase «Ensure secure access» implies the use of HTTPS.
SSL termination on the reverse proxy is a standard practice.
2.2.2) If Nginx does not forward information about the original protocol (e.g., via the `X-Forwarded-Proto: https` header), the backend considers the connection insecure.
This leads to incorrect redirect URL generation or causes the application to refuse the session.
Furthermore, if the backend mistakenly perceives the connection as insecure (HTTP), it will likely not set the `Secure` flag on cookies. 
This is problematic because modern browsers mandate the `Secure` flag for any cookie marked with `SameSite=None` (which is often required in reverse proxy scenarios).
3) Hypothesis #3: Incorrect `Host` header forwarding
3.1) The essence
Nginx forwards an incorrect `Host` header to the backend (e.g., the upstream server's name or its IP address instead of the external domain name used by the client).
The backend uses this value to generate absolute redirect URLs after login.
Additionally, this value is used as the target origin in Cross-Site Request Forgery (CSRF) protection.
3.2) Plausibility arguments
Many web frameworks compare the value of the `Host` header (target origin) with the values of the `Origin` and/or `Referer` headers (source origin) for CSRF protection.
A mismatch, caused by an incorrect `proxy_set_header Host` configuration, leads to this check failing (e.g., a 403 Forbidden error), resulting in authentication failure.
If the application uses the `Host` header to set the `Domain` attribute in the Cookie, this scenario is the root cause of Hypothesis #1.
4) Hypothesis #4: Cookie path mismatch (the `Path` attribute).
4.1) The essence
The backend application sets a cookie with a `Path` attribute matching its internal path (e.g., `/internal-app/`).
The client's browser accesses the application via the proxy using a different path (e.g., `/`).
The browser does not send the cookie in subsequent requests because the current request path does not match the cookie's `Path` attribute.
4.2) Plausibility arguments
4.2.1) Changing the URL structure is a common practice when publishing an internal application via a reverse proxy.
4.2.2) By default, Nginx does not modify the `Path` attribute in the `Set-Cookie` header.
The `proxy_cookie_path` directive is required to correct this.
5) Hypothesis #5: Cookie blocking due to the `SameSite` attribute.
5.1) The essence
When proxying results in a change of domain (site), the interaction context, from the browser's perspective, shifts from same-site to cross-site.
The browser prevents authentication cookies from being sent, as they do not meet the requirements for the cross-site context.
5.2) Plausibility arguments
Modern browsers apply the `SameSite=Lax` policy by default if the `SameSite` attribute is not explicitly set.
The `Lax` or `Strict` policies restrict cookies from being sent in cross-site requests (e.g., `POST` requests after a redirect).
Using cookies in a cross-site context requires explicitly setting `SameSite=None`; this must be accompanied by the `Secure` flag.
If the backend does not set these attributes correctly, or if they are not modified by Nginx (e.g., using the `proxy_cookie_flags` directive), authentication will fail.
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
5) Hypothesis #5: Cookie blocking due to the `SameSite` attribute.
5.1) The essence
When proxying results in a change of domain (site), the interaction context, from the browser's perspective, shifts from same-site to cross-site.
The browser prevents authentication cookies from being sent, as they do not meet the requirements for the cross-site context.
5.2) Plausibility arguments
Modern browsers apply the `SameSite=Lax` policy by default if the `SameSite` attribute is not explicitly set.
The `Lax` or `Strict` policies restrict cookies from being sent in cross-site requests (e.g., `POST` requests after a redirect).
Using cookies in a cross-site context requires explicitly setting `SameSite=None`; this must be accompanied by the `Secure` flag.
If the backend does not set these attributes correctly, or if they are not modified by Nginx (e.g., using the `proxy_cookie_flags` directive), authentication will fail.
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
Этот фрагмент должен состоять из законченных предложений (не оборванных кусков предложений).
~~~~~~