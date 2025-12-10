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
 