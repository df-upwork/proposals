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
```
▶ A
```
означает, что в описываемой мной ситуации я использую `A`.



~~~~~~

# 3. `O.md`
~~~~~~markdown
# 0.
Сегодня 2025-09-11.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/Shopify-Developer-Image-upload-convert_~021965280210785048329

## 2.2. Title
Shopify Developer - Image upload / convert


## 2.3. Description
`PD` ≔ 
```text
I am looking to develop a 1-page 1-product website that allows a user to upload an image, BUT the most essential part is: we need to convert the uploaded image into a watercolor effect of the original upload photo.

I have the photoshop actions I’d like to occur, but can obviously not use PS for a real time e-commerce conversion of a normal photo upload to the water color effect.

Please respond with your plan for the project as well an estimated timeline based on the scope.
```

## 2.4. Attachments
### 2.4.1. 
`source.jpg`
### 2.4.2. 
`target.png`


# 3. Информация о `ꆜ`
## 3.1. Местоположение

United States
Ocean City

## 3.2. Характеристики компании
### 3.2.1. Сектор экономики
неизвестно

### 3.2.2. Количество сотрудников
неизвестно

## 3.3. Характеристики учётной записи на `UW`
### 3.3.1. Member since
Nov 10, 2020
### 3.3.2. Hire rate (%)
100
### 3.3.3. Количество опубликованных проектов (jobs posted)
44
### 3.3.4. Total spent (USD)
$165K
### 3.3.5. Количество оплаченных часов в почасовых проектах
6250
### 3.3.6. Средняя почасовая ставка (USD)
$23.85

# 4. Другие проекты `ꆜ` на `UW`
## 4.1. `P1⁎`

## 4.1.1. URL
https://www.upwork.com/jobs/~021961209762859434349

## 4.1.3. Title
Photoshop Automation Template

## 4.1.4. Description
`P1D` ≔ 
```text
Need assistance in mass converting standard images into water color digital paintings using Photoshop actions. The conversion from a standard photo to water color is complete. Step 2 in the process is downsizing the rendering, putting it into a framed background, and saving the output image. I neeed to select from 5 different background options that will be our standard going forward. Must be able to start immediately. Ty!
```

## 4.2. `P2⁎`

## 4.2.1. URL
https://www.upwork.com/jobs/~021960906095505385383

## 4.2.2. Title
Cold Calling Business Manager

## 4.2.3. Description
`P2D` ≔ 
```text
I am looking for a VERY SPECIAL manager, who will bring on-board and oversee a team of 5-20 telemarketers who will cold call, text, and email realtors. The nature of the email is a gift for their client after they sell their home. All leads will be generated. I I just need someone to manage a team of incredibly skilled cold-callers and ensure hiring, training, metrics, payroll are being met.

Willing to pay for a centralized office for all team members to work together.

Must be able to work eastern standard time

Familiarization with cold calling tech and initial set up is a BIG bonus.

Base salary + commission!

LOOKING FOR A UNIQUE UNICORN. HIGH EXPECTATIONS. HIGH REWARD.

MUST SPEAK CLEAR ENGLISH WITH NO NOTICABLE ACCENT.

THANK YOU & GOD BLESS!!
```

## 4.3. `P3⁎`

## 4.3.1. URL
https://www.upwork.com/jobs/~021965623373957601033

## 4.3.2. Title
Figma Designer + create content


## 4.3.3. Description
`P3D` ≔ 
```text
Must be able to start immediately
Need to be able to start asap.

1 page website
1 product
4 variants
Inspiration:
https://www.limeandlou.com/

Home page video
Upload image (sticky) follows you on page
Explain process
Step 1 upload image
Step 2 input address (text box)
Step 3 select 1 of 4 frame color
Step 4 checkout

Realtor package - bundle and and save
4 options
(3 pack) (5 pack) (10 pack) (20 pack)

Broker - bundle and save
4 options
25, 50, 75, 100

Reviews

4 icons - Locally Made, High-End Quality, Eco Friendly, Free Shipping
```

# 5.
## 5.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`}

## 5.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 5.3.
`Pi` : `Ps`

# 6.
## 6.1.
⊤ (Все `Pi` касаются одного и того же большого проекта `ꆜ`)

# 7.
`T⁎` ≔†
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
we need to convert the uploaded image into a watercolor effect of the original upload photo.
~~~
```

# 8.
## 8.1.
`I1` ≔ 
```
Предоставленный `ꆜ` файл `source.jpg` (§2.4.1)).
`ꆜ` приводит его в `PD` как пример «the uploaded image»
```

## 8.2.
`I2` ≔ 
```
Предоставленный `ꆜ` файл `target.png` (§2.4.2)).
`ꆜ` приводит его в `PD` как пример «a watercolor effect of `I1`»
```

# 9
`PAᨀ` ≔
```
«the photoshop actions», о которых `ꆜ` говорит в `PD`.
``` 

# 10.
`PA?` ≔?
```
Действительно ли некие `PAᨀ` могут преобразовать `I1` в `I2`?
``` 
 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1.
`H`[§1-§4] ≔ `PA?`

## 1.2.
`Ps`[§1-§4] ≔ ⠿~(доводы за `H`)

## 1.3.
`Pi`[§1-§4] : `Ps`

## 1.4.
`Cs`[§1-§4] ≔ ⠿~(доводы против `H`)

## 1.5.
`Ci`[§1-§4] : `Cs`

## 1.6.
`As`[§1-§4] ≔ (`Ps` ⋃ `Cs`)

 ## 1.7.
`Ai`[§1-§4] : `As`

## 1.8.
`AiS`[§1-§4] ≔ («Score» для `Ai`: целое число от 0 до 100, отражающее значимость `Ai`)

## 1.9.
`V`[§1-§4] ≔ ⠿(твоё итоговое, обоснованное, объективное мнение о `H`)

## 1.10.
`HS`[§1-§4] ≔ («Score» для `H`: целое число от 0 до 100, отражающее твою оценку `H`)

## 1.11.
`R`[§1-§4] ≔ (итоговый отчёт)

## 1.12.
`Ts`[§1-§4] ≔ (`As` ⋃ ⠿{`V`})

## 1.13.
`Ti`[§1-§4] : `Ts`

# 2. `᛭T`
Действуй последовательно, по следующим шагам:
2.1. Определи и систематизируй `Cs`.
2.2. Определи и систематизируй `Ps`.
2.3. Совместно проанализируй `Cs` и `Ps`. 
Для каждого `Ai` определи `AiS`. 
2.4. На основе этого анализа составь `V` и определи `HS`.
2.5. Предоставь `R` в соответствии с требованиями §3

# 3. Требования к формату `R`
## 3.1. 
`Rs` ≔
```markdown
# 1. Pros
## 1.1. <`Ai` Title>
**Score**: **`AiS`**
`Ai`

## 1.2. <`Ai` Title>
**Score**: **`AiS`**
`Ai`

<…>

# 2. Cons
## 2.1. <`Ai` Title>
**Score**: **`AiS`**
`Ai`

## 2.2. <`Ai` Title>
**Score**: **`AiS`**
`Ai`

<…>

# 3. Verdict
**Score**: **`HS`**
`V`
```

## 3.2. 
`R` должен быть документом Markdown структуры `Rs`.

## 3.3.
Не заключай `R` внутрь backticks.  
Другими словами, в твоём ответе `R` должен отображаться как rendered Markdown, а не как сырая разметка Markdown.

## 3.4.
### 3.4.1
Каждый абзац `Ti` должен содержать ровно одно предложение.
### 3.4.2
Между абзацами `Ti` не должно оставаться пустых строк.

# 4. Требования к источникам информации
В своём анализе используй авторитетные источники информации на английском языке.

# 5. Дополнительные требования
1) Уже известную мне информацию не пересказывай.
2) Свой ответ дай на русском языке. 
3) Обязательно используй свой режим «Deep Research».
Твой ответ без режима «Deep Research» — гарантированно неверный.

~~~~~~