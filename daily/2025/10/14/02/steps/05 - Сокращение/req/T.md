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
The MCL, which defines category colors, is stored only in the Default Data File of an Outlook profile.
Preservation of the MCL and colors is guaranteed only if the PST file was the Default Data File on the old computer and is configured as the Default Data File on the new computer.
2.3) Disadvantages
The method is applicable only if the source data is stored in a PST file.
It is not applicable if the contacts are stored in an OST file (used by Exchange, Microsoft 365, and Outlook.com accounts, or by IMAP accounts for server-synchronized data and «This computer only» folders).
All data contained in the file is transferred (e.g., mail, calendar), not just the contacts.
If the PST file was not the Default Data File in the source profile, it does not contain the MCL.
If the PST file is connected as a secondary data store (not the Default Data File) in the new profile, the MCL from the PST file is ignored.
In these scenarios, the category colors will not be transferred automatically and must be migrated separately using specialized methods (e.g., specialized third-party tools or programmatic methods), similar to the process described in method 3.
3) Folder-Level Copy
3.1) Essence
This method involves connecting the source contact data to the Outlook profile on the new computer and using the «Copy Folder» function to transfer the «Contacts» folder into the destination data store.
To be connected on the new computer, the source contacts must reside in a PST file.
The procedure varies depending on whether the source data is currently in a PST or an OST file.
3.1.1) Scenario A (Source data in PST, e.g., POP account)
The PST file is copied from the old computer.
It is then connected to the new Outlook profile as an additional data store («File» → «Open & Export» → «Open Outlook Data File»).
Finally, the «Contacts» folder is copied from this connected PST file to the target folder in the new profile using the «Copy Folder» function.
3.1.2) Scenario B (Source data in OST, e.g., IMAP «This computer only» folders)
The contacts must first be transferred to a temporary PST file on the source computer.
This OST to PST transfer can be performed using 2 high-fidelity methods.
3.1.2.1) Copy Folder
Create a new PST file within the original Outlook profile and copy the «Contacts» folder directly from the OST storage to this new PST file using the «Copy Folder» function.
3.1.2.2) Export Wizard
Use the standard Outlook «Import/Export Wizard» («File» → «Open & Export» → «Import/Export» → «Export to a file») to export the «Contacts» folder to a new PST file.
When exporting specifically to an «Outlook Data File (.pst)» (unlike CSV or Excel formats), the wizard preserves custom fields and groups.
The resulting temporary PST file is then transferred to the new computer.
It is connected to the new profile, and the contacts are copied into the destination data store using the «Copy Folder» function.
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
`𐒌†` ≔† 
```
В текущем тексте Aᨀ` слишком места занимает описание способа 3.
```

# 3. `᛭T`
Нужно ли вообще предлагать `ꆜ` способ 3, или же достаточно способов 1 и 21?
Предложи конкретные правки к `Aᨀ` для устранения `𐒌†`.

# 4. Источники информации
## 4.1.
Используй авторитетные источники информации на английском языке, относящиеся к предметной области `P⁎` и `𐒌†`.

## 4.2.
В первую очередь используй официальные источники.

# 5. Порядок работы
## 5.1.
Обязательно используй свой режим «Deep Research».
Твой ответ без режима «Deep Research» — гарантированно неверный.

## 5.2.
В первую очередь используй официальные источники.

# 6. Правила ответа / Общие
## 6.1.
Отвечай на русском языке.
Исключением являются точные официальные термины: смотри пункт 6.2 ниже.

## 6.2.
При обсуждении программного обеспечения используй точные официальные термины на английском языке: именно в том виде, как они указаны в официальной англоязычной документации к этому программному обеспечению.

## 6.3.
Не используй выделение жирным (`**`) и курсив (`*`).

## 6.4.
Названия файлов заключай в backticks.
Например: `header.php`.

## 6.5.
Названия элементов интерфейса заключай в угловые кавычки (`«»`).

## 6.6.
Для путей в интерфейсе используй `→`.
Например: «Current User» → «Personal».

## 6.7.
Не используй жаргон.
Вместо этого используй официальные термины.

### 6.7.1.
В частности, фразы в кавычках используй только в том случае, когда они являются точными цитатами.
Не используй фразы в кавычках для применения жаргонных фраз.
Например, следующий фрагмент текста недопустим, потому что там используется жаргонная фраза «пролетел»: 
```
Например, код, который пушит данные о покупке, подключён асинхронно и загружается с небольшой задержкой, а триггер уже «пролетел».
```

## 6.8.
Не используй самовольно «you need» и другие подобные обращённые к `ꆜ` фразы, перекладывающие действия на него, если в исходном тексте явно не сказано подобное (типа «вы должны»).
Помни: я пишу `ꆜ`.
Делать в любом случае буду я, а не `ꆜ`.
Именно за то, что описываемую работу делать буду я, `ꆜ` мне будет платить.
Моя задача — показать мою компетенцию и предложить `ꆜ` решение его проблемы, а не переложить решение проблемы на `ꆜ`.

## 6.9.
Мой вопрос не пересказывай.

## 6.10.
Уже сформулированную мной информацию не пересказывай.

## 6.11.
Писать свою версию `Aᨀ` не нужно: просто укажи конкретные точечные правки по пунктам.

## 6.12.
До и после списка правок ничего не пиши.

## 6.13.
Нумерация замечаний должна быть сквозной.

## 6.14.
Форматируй текст своих правок в точности как оригинал (`Aᨀ`). 
В частности:
*) каждый абзац должен содержать ровно одно предложение
*) между абзацами не должно оставаться пустых строк.
*) кавычки используй те же, что и в оригинале: «» и ``.

## 6.15.
Все числительные должны писаться цифрами (а не прописью).

# 7. Правила ответа / Для правок на английском языке
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