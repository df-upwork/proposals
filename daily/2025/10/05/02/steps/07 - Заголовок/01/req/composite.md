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
Сегодня 2025-10-05.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021974167269608227151

## 2.2. Title
React/Next.js architect

## 2.3. Description
`PD` ≔ 
```text
I need someone with extensive experience in development and deployment of Next.js and React applications to do an architecture and code review with my team.

We have a purpose-build web publishing platform build by an experienced web team, but we've encountered some performance issues and we need an experienced person to look at it with fresh eyes, make some recommendations, and possibly help us improve performance, avoid technical pitfalls, and so on.

## Deliverables
- Engage with my technical team for probably a couple weeks
- Produce two things: 
    1) technical fixes that my team can apply (or just apply them with the team directly)
	2) written architecture recommendations for the future
```

## 2.4. Tags
React
Next.js
Cloudflare
Website Migration
Website Customization

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Mar 27, 2025
### 5.3.2. Hire rate (%)
0
### 5.3.3. Количество опубликованных проектов (jobs posted)
3
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
we've encountered some performance issues
~~~
```

# 7.
`N†` ≔†
```
Проблемы, подобные `P†` в приложениях Next.js
```


 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 2.1.
`Dᨀ` ≔ (мой ответ `ꆜ`)

## 2.2.
Содержание `Dᨀ`:
~~~markdown
In my experience, the primary causes of poor performance in Next.js applications are the following:
# 1. Inefficient data fetching and processing
## 1.1. 
Sequential requests (`fetch` waterfalls) instead of parallel ones.
## 1.2. 
Slow queries to the database/API.
## 1.3. 
Over-fetching.
## 1.4. 
Blocking operations on the server that affect Time to First Byte (TTFB).
# 2. Suboptimal rendering and caching strategy
## 2.1. 
Using dynamic rendering (rendering at request time) for content suitable for static rendering (rendering at build time or upon revalidation).
## 2.2. Inefficient use of server-side caching mechanisms in the App Router
### 2.2.1. 
Incorrect data cache configuration. 
This includes unnecessarily using the `cache: 'no-store'` option for `fetch` requests or failing to utilize `unstable_cache` for data that could be cached. 
This increases the load on data sources.
### 2.2.2. 
Suboptimal revalidation strategies for data cache and full route cache (time-based revalidation or on-demand revalidation), leading to the display of stale data or too frequent content regeneration.
### 2.2.3. 
Unintentional disabling of the full route cache due to the use of dynamic functions (e.g., `cookies()`, `headers()`), opting the route into dynamic rendering and preventing caching of the rendering result.
### 2.2.4. 
Failing to use React `cache` for non-`fetch` requests (e.g., via an ORM or direct database queries), resulting in the duplication of identical requests within a single render pass, as these requests (unlike `fetch` requests) are not automatically memoized.
# 3. Large JavaScript bundles and hydration issues
## 3.1. 
Importing unnecessary libraries.
## 3.2. 
Insufficiently granular component-level code splitting: failing to utilize lazy loading (with `next/dynamic` or `React.lazy`) for non-critical or large client components.
## 3.3. 
Slow hydration due to excessive size or complexity of client components, leading to increased Time to Interactive (TTI) and Total Blocking Time (TBT).
## 3.4. 
Using client components instead of server components for non-interactive parts of the interface, leading to an excessive JavaScript bundle size and increased hydration workload.
# 4. Unoptimized resources and third-party scripts
## 4.1. 
Failing to use `next/image` for automatic image optimization (e.g., serving modern formats like WebP/AVIF, responsive sizing, and lazy loading).
## 4.2. 
Render-blocking fonts and third-party scripts (analytics, ads).
# 5 Infrastructure configuration issues (Cloudflare)
## 5.1. 
Inefficient CDN caching rules.
## 5.2. 
Runtime environment limitations (e.g., Edge Runtime), such as resource constraints (CPU time, bundle size) and incompatibilities with third-party libraries that rely on unsupported Node.js APIs.
~~~

# 2. `᛭T`
Я хочу опубликовать `Dᨀ` в виде статьи на своём сайте и в виде документа PDF.
Для этих целей мне нужно озаглавить `Dᨀ`.
Твоя задача: предложить 10 вариантов заголовка (`T๏`) для `Dᨀ`.

# 3. Требования к `T๏`
## 3.1.
`T๏` должен быть на английском языке.
## 3.2.
Для каждого `T๏` укажи своё обоснование.
## 3.3.
Не пиши каждое слово с заглавной буквы. 
Вместо этого пиши нормальным образом, как обычное предложение.
## 3.4.
Не повторяй варианты §5.

# 4. Пожелания к `T๏`
## 4.1.
Желательно использовать профессиональный язык предметных областей `P⁎` и `Dᨀ`.

## 4.2.
Желательно указать характер проделанной мной работы, например:
- consultation 
- expert opinion
- guidance

## 4.3.
Попробуй использовать варианты §5 как основу для твоей работы.

# 5. Варианты `T๏`, которые мне пока нравятся больше всего
- Why your Next.js application is slow and how to identify the issues
- My checklist for <…>

~~~~~~