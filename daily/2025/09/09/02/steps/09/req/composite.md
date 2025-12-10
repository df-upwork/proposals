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
# 1.
`ꆜ` ≔ `Michael Klein`


# 2.
## 2.1.
`C᛭` ≔ `Unity Hospice and Palliative Care`

## 2.2.
⊤ 
```ini
Сайт `C᛭`: https://www.unityhospice.com
```

# 3.
⊤ 
```
`ꆜ` владеет `C᛭` и является его CEO
https://ktla.com/business/press-releases/ein-presswire/791464985/unity-hospice-and-palliative-care-with-over-30-years-experience-broadens-services-to-southern-wisconsin/
```

# 4.
Статья о `ꆜ`: https://voyagechicago.com/interview/meet-michael-klein-chaim-klein-eli-klein-ben-klein-unity-hospice-chicagoland/
Содержание:
~~~
Today we’d like to introduce you to Michael, Chaim, Eli, and Ben Klein.

Michael, Chaim, Eli, and Ben, can you briefly walk us through your story – how you started and how you got to where you are today.
Unity Hospice was created in November 1992 – in fact, we’re celebrating our 25th anniversary next month, which is tremendously rewarding on many levels.

At the time, I was partner at a major law firm here in Chicago. I am eternally grateful for my career experience in law, but my vision was to do something that truly made a difference for humanity. So, back in 1992 when my wife and I were expecting our fifth child, we decided to leave the partnership and make that vision a reality. I started Unity Hospice at my kitchen table – I still have that same kitchen table. I familiarized myself with the regulations, and took the necessary steps to start a hospice company, and hired my first employees – all things I’ve never done before.

Our very first office was in Skokie, Ill., the town in which our corporate office is located today. We started off with a few patients here and there. We later expanded to downtown Chicago so that we had the ability to serve a larger patient-base. Now, 25 years later, we have six offices that serve patients in Illinois, Indiana and Missouri. To see where we have grown and come to today is really pretty tremendous.

I still remember one of our very first patients…he was a veteran without a means to pay for his care. But that didn’t matter – he was sick. This patient was in need of a specialized type of care that only hospice can offer, and we were dedicated to serving him. That experience has laid the foundation of who we are as an organization today. We don’t turn anyone down because of an inability to pay…we put people before profit.

Has it been a smooth road?
To reflect back on our 25 years, I’m sure there have been struggles along the way – as with any business. But it’s the accomplishments that stick out to me more than the struggles. The growth we’ve experienced over the years is directly attributed to our team: our clinical team – without whom we would not be able to provide such a proficient level of care…our administrative & marketing teams who oversee the daily intricacies of customer service, intake and billing…our volunteers who give up their personal time and energy to visit with our patients. One of the nice things about Unity is that our staff comes to you; whether a patient is in a private home, a nursing home or other care facility, we will provide care in the place they call “home” so patients and families experience comfort, dignity and tranquility, wherever they are.

But perhaps the biggest accomplish to me, not only as an owner but as a father, is to see my kids continue the legacy of working at Unity. I couldn’t be more proud of that.

We’d love to hear more about your business.
Hospice care is an alternative to traditional healthcare as it focuses on the unique needs of people diagnosed with terminal illness.

Unity Hospice offers expert medical care, pain management and emotional and spiritual support as needed for our patients. Typically, hospice care is offered for patients with roughly 6 months or less to live. Some of our patients have benefitted from hospice for much less time than that, and some for longer. Everyone’s circumstance is different. Unity takes an individualized approach to each patient and family, and we generate a customized plan of care based on their specific needs.

Many people don’t realize that deciding which hospice to go with is your choice. You don’t have to use a hospice affiliated with your doctor or hospital, and you don’t have to use a specific hospice just because a health care provider recommended it. It is your right to choose the hospice that you truly want for your loved one. Many people choose Unity Hospice over other hospices because the experience Unity provides is unmatched. Unity was founded with a desire to care, and that care and warmth flows through all parts of Unity Hospice today.

What sets us apart? Many things…but one that I’m humbled by personally is we that we don’t just serve our patients and families. We also make it a priority to serve our communities. Over the years, Unity Hospice has provided free services and many charitable contributions. We routinely participate in disaster relief efforts, volunteer at food pantries, provide holiday meals & gifts to families in need, among many other things. It’s important to us that we are a citizen in the communities we serve.

Looking back on the 25 years of Unity Hospice, I would say that I’m most proud of the team members. Unity Hospice has become a family business in every sense of the word. My eldest son is the administrator of our Chicago office, while another son of mine serves as the company’s finance director. But in addition to that, every employee has become like a family member to me – the “Unity family”, we like to say. I feel honored to have the opportunity to provide a much-needed service to people in crisis situations…but I can’t have this opportunity by myself. And for that I have to thank my staff.

If you had to start over, what would you have done differently?
You know, I asked myself this question a very long time ago. And as it turns out, Unity Hospice is my “start over”. The way that I would have done things differently before is to pursue an opportunity that impacted people’s lives in a positive way. And I believe that Unity Hospice does just that – together we make a difference for patients, we make a difference in our communities, and yes, ultimately, we make the world a better place.

Contact Info:

Address: 600 W. Cermak Rd, Suite 3D
Chicago, IL 60616
Website: www.unityhospice.com
Phone: 312-427-6000
~~~
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1. `᛭T`
Найди мне:
1) email adress `ꆜ`
2) `ꆜ` в Facebook
3) `ꆜ` в LinkedIn

# 2.
1) В своём анализе используй авторитетные источники информации на английском языке.
2) Свой ответ дай на русском языке. 
3) Не пиши никогда «Хороший вопрос» и другой подобный мусор в начале ответа.
Мне подобное пиздобольство не нужно.
4) Обязательно используй свой режим «Deep Research».
Твой ответ без режима «Deep Research» — гарантированно неверный.
5) На остальные вопросы не отвечай.
6) Уже известную мне информацию не пересказывай.
7) Не пустословь.



~~~~~~