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
Сегодня 2025-11-24.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021992670149716146110

## 2.2. Title
Network Specialist – Set Up Port Forwarding Workaround on T-Mobile Home Internet (IPv6 + CGNAT)

## 2.3. Description
`PD` ≔ 
```text
#
I’m looking for a networking expert who can help me set up a reliable workaround for opening incoming ports on a T-Mobile Home Internet modem, which currently blocks inbound connections due to:
- IPv6-only network
- Carrier-Grade NAT (CGNAT)

#
T-Mobile confirmed they cannot open ports, but they advised that port forwarding can be achieved using third-party solutions such as:
- SSL VPN
- WireGuard

# Scope of Work
- Recommend the best method to bypass CGNAT and enable stable inbound connections
- Set up and configure a working solution (SSL VPN, WireGuard, or another viable method)
- Optionally advise if Google Cloud, or similar cloud services, can be used as a relay, tunnel, or reverse proxy workaround
- Configure everything securely and test that external devices can connect to the required ports
- Provide instructions so I can manage it afterward

# Requirements
- Strong experience with networking, NAT traversal, and IPv6
- Experience with VPNs (WireGuard, SSL VPN, or similar)
- Familiarity with cloud networking (Google Cloud, AWS, etc.) is a plus
- Ability to explain options clearly and implement the best solution

# Deliverables
- Successfully opened / forwarded ports to my local device despite T-Mobile restrictions
- Fully working configuration (VPN tunnel, cloud relay, or other method)
- Documentation of the setup

# Additional Info
I already confirmed with T-Mobile support that they cannot open ports on their network, so this will require a workaround solution, not simple port forwarding through the modem.
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Meriden

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Manufacturing & Construction

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Mar 27, 2022
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
39
### 5.3.4. Total spent (USD)
21K
### 5.3.5. Количество оплаченных часов в почасовых проектах
615
### 5.3.6. Средняя почасовая ставка (USD)
29.51

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
- T-Mobile currently blocks inbound connections
- T-Mobile confirmed they cannot open ports
~~~
```

# 7.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
set up a reliable workaround for opening incoming ports on a T-Mobile Home Internet modem
~~~
```

~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1. `᛭T`
1) Выяви все проблемы, которые беспокоят `ꆜ` в `P⁎`.
2) Проанализируй обоснованность каждой из выявленных проблем.

# 2. Источники информации
В своём анализе используй авторитетные источники информации на английском языке.

# 3. Требования к ответу
Свой ответ дай на русском языке. 
~~~~~~