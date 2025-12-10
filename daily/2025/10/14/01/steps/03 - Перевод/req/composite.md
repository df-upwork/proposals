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
Сегодня 2025-10-14.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021977396223927955174

## 2.2. Title
Automation Engineer

## 2.3. Description
`PD` ≔ 
```text
I have a successful Charter business in Chicago and I have a problem with reservations. 
There are three ways people can make reservations and book our Charters. 
Two are booking platforms that are nationwide. 
One is called to get my boat and the other one is called boatsetter. 
The third way they could book is directly on my booking site which I use an app called Greenstone.
Now all of these apps allow you to move the booking once you get it to either a Google calendar or possibly calendy so that all your bookings are in one place and you can see if you have double booked or have openings. 
The biggest problem is is that none of these three ways allow you to send your calendar back to them to block out time slots on each of the platforms. 
So you have to do that manually so if you get a booking and get my boat, you have to go into Green Stone and boatsetter and block out that time. 
If you get a booking on Greenstone, you have to go to get my boat and boat setter and block out that time. 
All this has to be done manually and it is very time-consuming. 
The apps don’t allow the other apps to talk to each other and none of them will upload Google calendar dates to block out certain times. 
No one in the charter industry has been able to figure out a way to automate this and as a result, many Charters get double booked and it creates a real bad customer service issue. 
In the new world of AI, there must be a way to solve this problem. 
Can you as an expert in advanced automation tell me how I could possibly solve this issue and maybe even build an app or a platform to be able to resell it as a subscription to the thousands of Charter wrote operators in the United States.
```

## 2.4. Tags
Automation
Business Process Automation
Dashboard
Google Workspace
AI Bot
ChatGPT
API Integration
Browser Automation
Web Scraping
API
Selenium
Zapier
Make.com
Google Sheets Automation
CRM Automation
Chatbot Development

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
Dec 15, 2024
### 5.3.2. Hire rate (%)
0
### 5.3.3. Количество опубликованных проектов (jobs posted)
1
### 5.3.4. Total spent (USD)
0
### 5.3.5. Количество оплаченных часов в почасовых проектах
0
### 5.3.6. Средняя почасовая ставка (USD)
0


 
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
Ваши заблуждения:
1) «none of these three ways allow you to send your calendar back to them to block out time slots»
1.1) На официальном сайте Greenstone явно указана «Google Calendar integration»: https://www.greenstoneapp.com/dashboard 
Также утверждается, что их календари помогают поддерживать синхронизацию «without double bookings».
Это подразумевает наличие двусторонней синхронизации.
1.2) GetMyBoat поддерживает импорт Google Calendar: https://www.youtube.com/watch?v=qWgG4U1l3WU
2) «No one in the charter industry has been able to figure out a way to automate this»
Технология для решения этой задачи давно существует и широко используется не только в чартерном бизнесе, но и в смежных отраслях (гостеприимство, аренда). 
Она называется «Channel Manager».
Пример реализации для чартерного бизнеса: https://web.viewyacht.com/post/charter-channel-manager-api
~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
Технология для решения этой задачи давно существует и широко используется не только в чартерном бизнесе, но и в смежных отраслях (гостеприимство, аренда). 
Она называется «Channel Manager».
Пример реализации для чартерного бизнеса: https://web.viewyacht.com/post/charter-channel-manager-api
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

## 6.11.
Все числительные должны писаться цифрами (а не прописью).

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