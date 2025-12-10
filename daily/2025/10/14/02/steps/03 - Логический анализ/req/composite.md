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
https://www.upwork.com/jobs/~021977444611620908774

## 2.2. Title
Transfer Outlook Contacts (Keep Custom Fields, Categories & Groups Intact)

## 2.3. Description
`PD` ≔ 
```text
I need an Outlook expert to transfer approximately 2,200 contacts from Classic Outlook on Windows 10 (old computer) to Classic Outlook on Windows 11 (new computer).

This must include preserving:
- All custom fields (user-defined data)
- Contact categories and color codes
- Contact groups/mailing lists

A standard export/import (CSV or PST) will not work, since it loses my custom fields. 
I need someone experienced with advanced Outlook data migration, field mapping, or folder-level transfers who can ensure the data appears and functions exactly the same on the new system.

# Details:
- Source: Classic Outlook (Windows 10)
- Destination: Classic Outlook (Windows 11)
- Approximately 2,200 contacts
- Several user-defined custom fields and group categories

# Additional Note:
I’m a general Outlook user (not highly technical), so I need someone who can clearly explain what’s needed and handle most of the setup or transfer steps independently. 
Remote assistance via screen share or remote desktop is fine if required.

# Please include in your proposal:
- A summary of your Outlook data migration experience
- How do you plan to preserve custom fields and categories
- Estimated time to complete the job

#Skills & Expertise:
- Microsoft Outlook (Classic/Desktop)
- Outlook PST/OST file management
- Contact migration and field mapping
- Custom fields & category preservation
- Windows 10 → Windows 11 migration
- Data backup & verification

# Deliverables
A complete and verified Outlook Contacts migration to the new computer — identical in structure, fields, and categories to the original.
```

## 2.4. Tags
Microsoft Outlook
Desktop Application

# 5. Информация о `ꆜ`
## 5.1. Местоположение

USA
Hudson

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Jun 24, 2024
### 5.3.2. Hire rate (%)
75
### 5.3.3. Количество опубликованных проектов (jobs posted)
4
### 5.3.4. Total spent (USD)
1.2K
### 5.3.5. Количество оплаченных часов в почасовых проектах
2
### 5.3.6. Средняя почасовая ставка (USD)
359.28

# 6.
`T⁎` ≔†
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
transfer approximately 2,200 contacts from Classic Outlook on Windows 10 (old computer) to Classic Outlook on Windows 11 (new computer)
~~~
```


 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 1.2.
Содержание `Aᨀ`:
~~~markdown
Correct methods for solving your task:
1) Synchronization via a server (Exchange / Microsoft 365)
1.1) Essence
If you use a Microsoft Exchange, Microsoft 365, or Outlook.com account, then all data (contacts, custom fields, groups) is stored on the server.
The server also stores the Master Category List (MCL), which defines the names and colors of the categories.
For the migration, it is sufficient to set up the same account in Classic Outlook on the new computer, and the data will synchronize automatically.
1.2) Advantages
This is the simplest and most transparent method.
Intervention is minimal and is limited to the account setup.
Complete and accurate preservation of all data is guaranteed, including custom fields, groups, and category colors.
1.3) Disadvantages
This method is applicable only to Exchange, Microsoft 365, or Outlook.com accounts.
It is not applicable to POP accounts.
It is not applicable to IMAP accounts, as the IMAP protocol does not support the synchronization of contacts and categories.
2) Direct copying of the PST file (for local data)
2.1) Essence
If the contacts are stored locally in an Outlook Data File (.pst) (e.g., with a POP account or as a dedicated local data file alongside IMAP/Exchange), this method is applicable.
The method involves copying the entire PST file from the old computer to the new one while the Outlook application is closed.
On the new computer, Outlook is configured to use this copied file (either as the primary data store or connected as an additional data file).
2.2) Advantages
This is the most reliable method for local data, as the entire database is copied.
Preservation of custom fields and contact groups is guaranteed.
The MCL and colors are also preserved, as they are stored in the main PST file.
2.3) Disadvantages
The method is applicable only if the source data is stored in a PST file.
It is not applicable if the contacts are stored in an OST file (used by Exchange, Microsoft 365, and Outlook.com accounts, or by IMAP accounts for server-synchronized data and «This computer only» folders).
All data contained in the file is transferred (e.g., mail, calendar), not just the contacts.
3) Folder-Level Copy
3.1) Essence
This method involves accessing the source contact data in the Outlook profile on the new computer and using the «Copy Folder» function to transfer the «Contacts» folder to a new data store.
The source data must be accessible in a PST file.
If the contacts are already in a PST file (POP account), this file is connected to the new Outlook profile as an additional data store («File» → «Open & Export» → «Open Outlook Data File»).
If the contacts are in an OST file (e.g., local folders «This computer only» with IMAP), they must first be transferred to a PST file on the source computer.
Crucially, the standard Outlook «Import/Export Wizard» must not be used for this transfer, as it will discard custom fields.
Instead, a new PST file is created within the original Outlook profile on the old computer.
The «Contacts» folder is then copied directly from the OST storage to this new PST file using the «Copy Folder» function.
This resulting PST file is then connected to the new Outlook profile on the new computer.
3.2) Advantages
This method ensures high-fidelity data copying, including custom fields and contact groups.
It allows for the integration of old contacts into a new profile without replacing it entirely.
The method bypasses the unreliable Import/Export Wizard by performing a direct copy of the database objects.
3.3) Disadvantages
This method requires careful management of multiple data files in the Outlook interface.
In an IMAP scenario (data in an OST), this method depends on the prior conversion of the OST to a PST.
The MCL, which stores the definitions of category colors, is not transferred automatically because it resides in the primary data store, not within the copied «Contacts» folder.
While category names remain assigned to the contacts, their corresponding colors will be missing in the new profile.
Applying the «Upgrade to Color Categories» function restores the category names to the new profile's MCL, but it assigns new, random colors.
The original color codes will be lost using this built-in function.
To preserve the original colors with this method, the MCL must be migrated separately using specialized third-party tools or programmatic methods (e.g., PowerShell scripts), as Outlook does not offer a built-in feature for exporting/importing the MCL.
~~~

# 2.
# 2.1.
`Fⰳ(§p)` ≔ (Пункт `§p` из `Aᨀ`)

# 2.2.
`Fⰳ(§a-§b)` ≔ (Фрагмент `Aᨀ` с пункта `§a` по пункт `§b` включительно)

# 3.
`Fᨀ` ≔ `Fⰳ(1-3)`

# 4. `᛭T`
Проанализируй `Fᨀ`:
1) Есть ли там логические ошибки?
2) Есть ли там фактические ошибки?

# 5. Требования к твоему ответу
## 5.1.
Отвечай на русском языке.
## 5.2.
Мой вопрос не пересказывай.
## 5.3.
Уже сформулированную мной информацию не пересказывай.
## 5.4.
Писать свою версию `Fᨀ` не нужно: просто укажи свои замечания по пунктам.
## 5.5.
До и после списка замечаний ничего не пиши.
## 5.6.
Нумерация замечаний должна быть сквозной.
## 5.7.
Для каждого своего замечания указывай свою степень уверенности в нём по шкале от 0 до 100:
- 0 означает, что твоё замечание безосновательно (ошибочно).
- 100 означает, что ты полностью уверен в правоте своего замечания.

# 6. К чему не надо придираться
## 6.1.
Если большая часть `Fᨀ` — на русском языке, то не придирайся к смешению в `Fᨀ` русского и английского языков.
Это смешение — временное и будет устранено позже.
~~~~~~