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
https://www.upwork.com/jobs/~021972320965691019923

## 2.2. Title
Microsoft D365 Business Central Reports

## 2.3. Description
`PD` ≔ 
```text
I need assistance in Microsoft D365 Business Central. 
I would like to generate both system generated reports such as invoices as well as custom reports using the "Century Gothic" font.  
This font is available in the desktop and online version of Word, but not in any of the reporting options I can see within Business Central.
```

## 2.4. Tags
Microsoft Dynamics 365
microsoft business central

# 5. Информация о `ꆜ`
## 5.1. Местоположение
Canada
Vancouver

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
10-99 people

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Feb 8, 2020
### 5.3.2. Hire rate (%)
75
### 5.3.3. Количество опубликованных проектов (jobs posted)
27 
### 5.3.4. Total spent (USD)
$38K
### 5.3.5. Количество оплаченных часов в почасовых проектах
605
### 5.3.6. Средняя почасовая ставка (USD)
58.58

# 6.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
I would like to generate both system generated reports such as invoices as well as custom reports using the "Century Gothic" font
~~~
```

# 7.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
This font is available in the desktop and online version of Word, but not in any of the reporting options I can see within Business Central.
~~~
```

# 8. Анализ способов решения `T⁎` 
## 8.1. Встраивание шрифта в макет Word (Word Layout Font Embedding)

### Описание
D365 BC поддерживает макеты Microsoft Word (.docx). В Word есть функция встраивания шрифтов непосредственно в файл (File → Options → Save → "Embed fonts in the file"). Теоретически, если шрифт успешно встроен, механизм рендеринга BC SaaS может использовать его при генерации PDF. Опыт экспертов сообщества (например, Erik Hougaard) показывает, что этот метод может быть успешным, если выполнен корректно.

### Достоинства
- **Стоимость:** Бесплатно. Не требует дополнительных лицензий или разработки.
- **Простота:** Реализуется стандартными средствами Word и загрузкой макета в BC (Custom Report Layouts).

### Недостатки
- **Зависимость от лицензии шрифта:** Успех критически зависит от прав на встраивание (Font Embeddability) конкретного файла "Century Gothic". 
Если лицензия запрещает встраивание, Word не внедрит шрифт.
- **Ограничение типа макета:** Применимо только к Word Layouts. 
Не работает для RDLC-макетов. Конвертация сложных RDLC в Word может быть трудоемкой.
- **Ненадежность:** Хотя метод часто работает, он не гарантирован на 100% и может зависеть от настроек в Word (например, необходимо отключить "Do not embed common system fonts").

### Оценка: 75/100

## 8.2. Сторонние ISV-решения для отчетности (Third-party Reporting Tools)

### Описание
Использование специализированных приложений из Microsoft AppSource (например, **ForNAV** или **Docentric**). Эти решения предоставляют собственные движки рендеринга, которые обходят ограничения платформы SaaS и автоматически внедряют пользовательские шрифты в PDF.

### Достоинства
- **Надежность:** Гарантированное и поддерживаемое вендором решение.
- **Улучшенные инструменты:** Часто предлагают более мощные и удобные дизайнеры отчетов.
- **Универсальность:** Работает для сложных отчетов, которые трудно реализовать стандартными средствами.

### Недостатки
- **Стоимость:** Требуется приобретение подписки/лицензий.
- **Внедрение и обучение:** Требуется время на изучение инструмента и конвертацию отчетов в новый формат.
- **Ограничения предпросмотра:** ⊤⟦ForNAV Knowledge Base⟧ (Предпросмотр в веб-клиенте BC может не отображать пользовательский шрифт; он виден только в финальном PDF).

### Оценка: 90/100

## 8.3. Внешний сервис рендеринга (External Rendering Engine)

### Описание
Разработка внешнего микросервиса (например, Azure Function). BC отправляет данные отчета (JSON/XML) в этот сервис. Сервис, используя сторонние библиотеки генерации PDF (например, PDFSharp, IronPDF), которые поддерживают полное внедрение шрифтов, генерирует документ с "Century Gothic" и возвращает его в BC.

### Достоинства
- **Полный контроль и гибкость:** Гарантирует использование любого шрифта и сложного форматирования, обходя все ограничения BC SaaS.
- **Качество вывода:** Генерируется высококачественный PDF с внедренным текстом (с возможностью поиска и копирования).

### Недостатки
- **Высокая сложность разработки:** Требует значительных компетенций в AL, Azure и языке микросервиса (например, C#).
- **Усложнение архитектуры:** Увеличивает накладные расходы на поддержку и инфраструктуру Azure.
- **Задержки:** Сетевое взаимодействие замедляет генерацию отчета.

### Оценка: 65/100 

# 9.
`H1?` ≔?
```
Лицензия на шрифт «Century Gothic» разрешает его встраивание в документ Word (способ §8.1)
```

# 10.
## 10.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 10.2.
Содержание `Aᨀ`:
~~~markdown
1) The online version of Business Central (`BC`) does not support the «Century Gothic» (`CG`) font: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-fonts#document-fonts
2) Your task has 3 good solutions.
I describe them in points 3-5 below.
3) Solution 1: A font can be embedded into a Word report layout.
3.1) Step-by-step instructions.
3.1.1) In `BC`, navigate to the «Report Layout Selection» (`RLS`) page and locate the required report.
3.1.2) Note: This method only works with Word layouts; if the report currently uses an RDLC layout, this method cannot be applied directly.
3.1.3) Choose the «Custom Layouts» action (often found under the «Process» or «Actions» menu) to open the «Custom Report Layouts» page.
3.1.4) Create a new custom Word layout (`L`) based on an existing layout, as built-in layouts cannot be modified.
3.1.5) Choose the «New» action.
3.1.6) In the dialog, ensure the «Insert Word Layout» toggle is activated and choose «OK» to create a copy of the built-in Word layout.
3.1.7) Select the newly created layout `L` and choose the «Layout» → «Export Layout» action to save it as a `.docx` file (`F`).
3.1.8) Open `F` in Microsoft Word (`W`).
3.1.9) Apply `CG` to the necessary text fields and content controls.
3.1.10) In `W`, navigate to «File» → «Options» → «Save».
3.1.11) In the section «Preserve fidelity when sharing this document», configure the following settings.
3.1.12) The «Embed fonts in the file» option must be activated.
3.1.13) To optimize the file size, it is highly recommended to activate the «Embed only the characters used in the document (best for reducing file size)» option.
3.1.14) Crucially, the «Do not embed common system fonts» option must be deactivated.
This is necessary because the `BC` SaaS server-side component often fails to correctly render custom fonts if this option is activated.
3.1.15) Save `F`.
3.1.16) Return to the «Custom Report Layouts» page in `BC`.
3.1.17) Select `L` and choose the «Layout» → «Import Layout» action to upload the modified file `F`.
3.1.18) Return to the `RLS` page.
3.1.19) For the report, set the «Selected Layout» field to «Custom Layout».
3.1.20) In the «Custom Layout Description» field, select the layout `L`.
3.2) Technical rationale
3.2.1) The mechanism underlying this method is related to the PDF file generation process on the `BC` server.
3.2.2) When the system generates a PDF from a Word layout, it uses a server-side component (the Aspose library).
3.2.3) If the font is not embedded in the `.docx` file, this component reads the font name, tries to find it in the list of fonts installed on the server, does not find it, and replaces it with a default fallback font (specifically Calibri, according to Microsoft documentation), which leads to your problem.
3.2.4) When the embedding option is activated, complete information about the font's glyphs and metrics is saved directly inside the `.docx` file.
When this file is processed by the server-side component, it can extract the font data from the document itself and use it to correctly render the text in the PDF, without requiring the font to be installed in the server's operating system.
3.3) For the implementation of Method #1, it is important that the font's «Font Embeddability» property has the value «Editable» or «Installable».
I have checked — for `CG` this is indeed the case (it is «Installable»): see the attached file `Century Gothic.png`.
4) Solution 2: Using a third-party extension for advanced reporting (ForNAV)
https://appsource.microsoft.com/en-us/product/dynamics-365-business-central/pubid.fornav%7Caid.customizable_report_pack%7Cpappid.83326d6d-11f8-49fd-981a-6f266a7c8d81
ForNAV is a comprehensive reporting solution in `BC` that includes its own report designer, a converter for standard reports, and an advanced rendering engine.
A key feature of ForNAV is its built-in and officially supported capability to work with custom fonts.
Unlike the standard approach utilizing Microsoft Word's embedding feature, font embedding in ForNAV is a core, documented feature of the extension itself.
The ForNAV Designer automatically detects that a custom font installed on the developer's computer is used in the layout and embeds its data directly into the report layout file when saving.
ForNAV's native rendering service, which processes these layouts in the BC environment, is specifically designed to work correctly with such embedded fonts.
This ensures a stable and predictable result, completely eliminating the uncertainty and risks associated with the native Microsoft rendering component.
5) Solution 3: Development of an external microservice (e.g., Azure Function)
`BC` sends the report data (JSON/XML) to this service.
The service, using third-party PDF generation libraries (e.g., PDFSharp, IronPDF) that support full font embedding, generates the document with CG and returns it to BC.
This method guarantees the use of any font and complex formatting, bypassing all BC limitations.
A high-quality PDF is generated with embedded text (with search and copy capabilities).
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
4) Solution 2: Using a third-party extension for advanced reporting (ForNAV)
https://appsource.microsoft.com/en-us/product/dynamics-365-business-central/pubid.fornav%7Caid.customizable_report_pack%7Cpappid.83326d6d-11f8-49fd-981a-6f266a7c8d81
ForNAV is a comprehensive reporting solution in `BC` that includes its own report designer, a converter for standard reports, and an advanced rendering engine.
A key feature of ForNAV is its built-in and officially supported capability to work with custom fonts.
Unlike the standard approach utilizing Microsoft Word's embedding feature, font embedding in ForNAV is a core, documented feature of the extension itself.
The ForNAV Designer automatically detects that a custom font installed on the developer's computer is used in the layout and embeds its data directly into the report layout file when saving.
ForNAV's native rendering service, which processes these layouts in the BC environment, is specifically designed to work correctly with such embedded fonts.
This ensures a stable and predictable result, completely eliminating the uncertainty and risks associated with the native Microsoft rendering component.
5) Solution 3: Development of an external microservice (e.g., Azure Function)
`BC` sends the report data (JSON/XML) to this service.
The service, using third-party PDF generation libraries (e.g., PDFSharp, IronPDF) that support full font embedding, generates the document with CG and returns it to BC.
This method guarantees the use of any font and complex formatting, bypassing all BC limitations.
A high-quality PDF is generated with embedded text (with search and copy capabilities).
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