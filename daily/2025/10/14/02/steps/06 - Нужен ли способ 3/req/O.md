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
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
transfer approximately 2,200 contacts from Classic Outlook on Windows 10 (old computer) to Classic Outlook on Windows 11 (new computer)
~~~
```

# 7.
## 7.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 7.2.
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
3) Folder-Level Transfer (via PST)
3.1) Essence
This method involves transferring the contacts via a temporary Outlook Data File (.pst).
It is used when contacts are stored locally but methods 1 and 2 are not applicable (e.g., data in an OST file from an IMAP account, «This computer only» folders) or when merging contacts into an existing profile is required.
The process requires 2 main steps.
3.1.1) Step 1: Consolidate data into a PST file
If the source data is in an OST file, it must first be transferred to a PST file on the old computer.
This can be achieved using the «Copy Folder» function or the Outlook «Import/Export Wizard» (exporting specifically to an «Outlook Data File (.pst)»).
Contrary to common belief, exporting to a PST file (unlike CSV) preserves all custom fields and groups.
If the data is already in a PST file, this file is used directly.
3.1.2) Step 2: Transfer to the new computer
The PST file is moved to the new computer and connected to the new Outlook profile.
The «Contacts» folder is then transferred from this PST file to the destination data store using the «Copy Folder» function.
3.2) Advantages
This method ensures high-fidelity data copying, including custom fields and contact groups.
It allows for the integration of old contacts into a new profile without replacing it entirely.
It is a viable method for migrating data stored in OST files.
3.3) Disadvantages
This method is more complex than methods 1 and 2, requiring multiple steps and management of data files.
The Master Category List (MCL), which stores category colors, is not transferred automatically.
While category names remain assigned to the contacts, their colors will be lost in the new profile.
Preserving the original colors requires a separate, specialized migration of the MCL (e.g., using programmatic methods or third-party tools), as Outlook lacks a built-in feature for this.
~~~
 
# 8.
`H?` ≔?
```
Нужно ли вообще предлагать `ꆜ` способ 3, или же достаточно способов 1 и 2?
```  