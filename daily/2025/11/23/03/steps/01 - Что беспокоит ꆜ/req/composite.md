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
Сегодня 2025-11-23.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021992339547511628414

## 2.2. Title
Nutanix Systems Engineer for Backup Environment Deployment

## 2.3. Description
`PD` ≔ 
```text
#
We are seeking an experienced Nutanix Systems Engineer to assist with the deployment of a new 4-node Nutanix cluster, including validation of hardware, software, licensing, and compatibility with an existing production environment.

#
This engagement requires someone who understands Nutanix hardware PIDs, AOS/AHV licensing, Prism Central/Prism Leap, and the architectural caveats involved in building a new site that will operate in parallel to production as a backup/DR environment.

# Ideal Experience
- Strong background with Nutanix NX hardware platforms and related PIDs
- Deep understanding of AOS, AHV, Prism Central, and Prism Leap
- Experience with multi-site Nutanix deployments, DR runbooks, and cross-cluster replication
- Ability to validate switch, firewall, and networking requirements for Nutanix clusters
- Knowledge of licensing models (AOS Pro vs Ultimate, Prism Central, Leap, term SKUs, support SKUs)
- Experience guiding customers through new-site buildouts and DR/backup planning

# Key Responsibilities
- Review design, architecture, and BOM for the new 4-node Nutanix site
- Validate all hardware PIDs, NICs, uplinks, switch modules, and licensing against Nutanix compatibility requirements
- Confirm correct AOS Pro and Prism Leap licensing for replication, DR, and recovery workflows
- Ensure all necessary components (hardware, software, support SKUs, cabling, optics, power, etc.) are included and sized correctly
- Validate compatibility between new site and existing production site, including hypervisor, AOS versioning, network topology, and replication capabilities
- Act as a remote technical resource to support planning, documentation, and deployment readiness
- Identify any missing elements or risks in the deployment plan
- Provide best practices around Nutanix cluster setup, networking, node placement, and DR architecture
- Support configuration steps as needed (AHV, Prism, storage containers, networks, protection domains
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Irvine

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Jul 13, 2025
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
4
### 5.3.4. Total spent (USD)
2.8K
### 5.3.5. Количество оплаченных часов в почасовых проектах
39
### 5.3.6. Средняя почасовая ставка (USD)
58.07

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021960940130771944242

### 6.1.2. Title
VOIP Troubleshooting and Configuration Specialist Needed

### 6.1.3. Description
`P1D` ≔ 
```text
We are seeking an experienced professional to assist with troubleshooting a VOIP call behavior issue and configuring VOIP gateway routing logic. The ideal candidate will have hands-on experience with PRI PBX systems and a deep understanding of VOIP protocols. Your expertise will help resolve ongoing issues and optimize our VOIP infrastructure. If you're passionate about delivering high-quality VOIP solutions, we want to hear from you! Looking for a go-to engineer to work with if this project goes well.
```

### 6.1.4. Publication Date
3 months ago

### 6.1.5. Payment Terms (USD) 
#### 6.1.5.1. Expected by `ꆜ`  
250 (Fixed Price)
#### 6.1.5.2. Actual
неизвестно

### 6.1.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.1.7. Duration (expected by `ꆜ`)
неизвестно

### 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

### 6.2.1. URL
https://www.upwork.com/jobs/~021944524922209486421

### 6.2.3. Title
Cisco DWDM Remote Support – ONS 15454 & NCS 2000 Experience

### 6.2.3. Description
`P2D` ≔ 
```text
We’re looking for a reliable, experienced network engineer or optical transport tech who’s comfortable supporting Cisco DWDM platforms — specifically ONS 15454 (M6/M12 chassis) and/or Cisco NCS 2000.

This is a remote, as-needed role — you’d be helping us troubleshoot or guide us through issues that come up in the field. In some cases, it might just be helping us review CTC logs, verify card configs, or assist with a remote provisioning task. Other times, it could involve guiding an on-site tech who's hands-on with the hardware.

We don’t expect someone to be available 24/7, but we’re building a small bench of go-to experts for optical support. If you’re dependable and know your way around these systems, it could turn into regular work.

Please share any experience you have working with Cisco DWDM platforms such as the ONS 15454 and NCS 2000, as well as any related optical transport hardware or DWDM network architecture.
```

### 6.2.4. Publication Date
last quarter

### 6.2.5. Payment Terms  (USD) 
#### 6.2.5.1. Expected by `ꆜ`
30-50 Hourly
#### 6.2.5.2. Actual 
5 hrs @ $40.00/hr
Billed: $207.99

### 6.2.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.2.7. Duration (expected by `ꆜ`)
1-3 months

### 6.2.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.3. `P3⁎`

### 6.3.1. URL
https://www.upwork.com/jobs/~021956171617144318918

### 6.3.2. Title
Oracle DBA - Cleanup High Disk Space - Possibly Extend Disk Space

### 6.3.3. Description
`P3D` ≔ 
```text
We have a Cisco Prime server running on Linux/VMware with Oracle databases experiencing high disk utilization. I need an experienced engineer who can help assess and clean up the environment, and if cleanup is not sufficient, guide us through expanding the underlying storage.

Scope of Work:

Assess current disk usage and identify safe cleanup opportunities in Oracle.

Perform tablespace cleanup, defragmentation, and stats gathering where appropriate.

If cleanup is insufficient, plan and execute storage expansion, which may include:

Adding physical disks and expanding them in Linux

Extending VM storage in VMware and allocating it to the OS

Restart and validate databases once adequate space is available.

Ensure all changes are performed without impacting database integrity.
```

### 6.3.4. Publication Date

last quarter

### 6.3.5. Payment Terms (USD) 
#### 6.3.5.1. Expected by `ꆜ`  
45-70 Hourly
#### 6.3.5.2. Actual
20 hrs @ $50.00/hr
Billed: $1,051.24

### 6.3.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.3.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

### 6.3.8. Contractor Location (expected by `ꆜ`)
Not specified


# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 8.
## 8.1.
`С⁎` ≔ 
```
Компания `ꆜ`:
```

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
assist with the deployment of a new 4-node Nutanix cluster
~~~
```

# 10.
## 10.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Review design, architecture, and BOM for the new 4-node Nutanix site
~~~
```

## 10.2.
`T2⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Validate all hardware PIDs, NICs, uplinks, switch modules, and licensing against Nutanix compatibility requirements
~~~
```

## 10.3.
`T3⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Confirm correct AOS Pro and Prism Leap licensing for replication, DR, and recovery workflows
~~~
```

## 10.4.
`T4⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Ensure all necessary components (hardware, software, support SKUs, cabling, optics, power, etc.) are included and sized correctly
~~~
```

## 10.5.
`T5⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Validate compatibility between new site and existing production site, including hypervisor, AOS versioning, network topology, and replication capabilities
~~~
```

## 10.6.
`T6⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Act as a remote technical resource to support planning, documentation, and deployment readiness
~~~
```

## 10.7.
`T7⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Identify any missing elements or risks in the deployment plan
~~~
```

## 10.8.
`T8⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Provide best practices around Nutanix cluster setup, networking, node placement, and DR architecture
~~~
```

## 10.9.
`T9⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Support configuration steps as needed (AHV, Prism, storage containers, networks, protection domains
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