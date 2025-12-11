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

# 17. `≔⊥`
~~~code
A ≔⊥ (B, C)
~~~
обозначает, что я вижу противоречие между `B` и `C` и обозначаю это противоречие как `A`.
Альтернативная запись:
```code
A ≔ (B, C ⊢ ⊥)
```

# 18. `≔⌖`
~~~code
A ≔⌖ ⟦§P⟧ 
```
B
```
~~~
означает, что я обозначаю как `A` утверждение `B`, высказанное раннее в пункте §P.
~~~~~~

# 3. `O.md`
~~~~~~markdown
# 0.
Сегодня 2025-12-11.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021998936685512149772

## 2.2. Title
Azure CLI SSL Certificate Verification Expert Needed for Python 3.13 Proxy Issue

## 2.3. Description
`PD` ≔ 
```text
I need an experienced freelancer to troubleshoot and resolve an SSL certificate verification error I'm encountering when using Azure CLI on my Windows machine (likely running in Git Bash or similar). The setup involves a custom Python 3.13 environment with Azure CLI installed via pip, and I'm behind a corporate proxy that performs SSL/TLS inspection. Despite following standard fixes, the issue persists, and I suspect it's related to strict certificate validation in Python 3.13.
Problem Details:

Command failing: az login (aliased to python -m azure.cli).
Error message: "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: CA cert does not include key usage extension (_ssl.c:1028)".
Environment: Windows, Python 3.13, custom .bashrc with exports like:
export PATH=/c/Users/[username]/bin:$PATH
export SSL_CERT_FILE=/path/to/cacert.pem
export REQUESTS_CA_BUNDLE=$SSL_CERT_FILE (and similar for GIT, CURL, NODE).

Attempts made:
Appended the proxy's root CA certificate (exported from a working machine) to a custom cacert.pem.
Set proxy vars (HTTP_PROXY, HTTPS_PROXY).
The CA cert is from our internal network/proxy (e.g., Zscaler or similar), but it lacks required extensions like keyCertSign in Key Usage.
Works on another machine (possibly older Python or different config), but not here.

Goal: Get az login working without disabling verification (insecure workaround). Prefer secure fixes like using system cert store, proper CA config, or Python tweaks.
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
New York

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Tech & IT

### 5.2.2. Количество сотрудников
Individual client

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Jun 12, 2020
### 5.3.2. Hire rate (%)
65
### 5.3.3. Количество опубликованных проектов (jobs posted)
417
### 5.3.4. Total spent (USD)
351K
### 5.3.5. Количество оплаченных часов в почасовых проектах
7599
### 5.3.6. Средняя почасовая ставка (USD)
44.22

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021997044898041376943

### 6.1.2. Title
Azure Networking

### 6.1.3. Description
`P1D` ≔ 
```text
Need SME to troubleshoot azure firewall issues, route tables, vpn gateway etc.  Strong preference for those who are azure network certified.  Not too many people out there with that skillset.
```

### 6.1.4. Publication Date
6 days ago

## 6.2. `P2⁎`

### 6.2.1. URL
https://www.upwork.com/jobs/~021996198048289262610

### 6.2.3. Title
Azure Cosmos DB Developer – Define & Implement Schema for Cosmos DB (NoSQL) Blob Storage Integration

### 6.2.3. Description
`P2D` ≔ 
```text
Must join call today 11am EST for this tutorial.  No audio just mouse control.  Lets connect before 11am call though.

We already have data being stored in Azure Blob Storage (JSON files). We now need to:

Design and define the optimal schema/structure for storing processed/output data in Azure Cosmos DB (Cosmos TV module).
Decide partitioning strategy, indexing policy, container structure, and relationships (embedding vs referencing) for best performance and cost.
Create the actual Cosmos DB database, containers, and implement the schema in a real Azure environment.
Write sample code (preferably C#/.NET 6+) to insert/read data respecting the new schema.
Ensure smooth integration between existing Blob Storage data pipeline and the new Cosmos DB layer.
```

### 6.2.4. Publication Date
last week

## 6.3. `P3⁎`

### 6.3.1. URL
Azure Policy Expert Needed to Modify and Exempt Policies for AKS Deployments

### 6.3.2. Title
https://www.upwork.com/jobs/~021996002015865609380

### 6.3.3. Description
`P3D` ≔ 
```text
Modify our existing Azure policies that are currently blocking AKS (Azure Kubernetes Service) deployments. The policies enforce standards like naming conventions, image restrictions, high-privileged roles, and DNS integrations, but they conflict with AKS's managed resources (e.g., random VMSS names, Microsoft-provided images).

Your tasks:

Review our current policy definitions (provided via shared access or code snippets).

Update policy rules to inherently exclude AKS-specific resource types (e.g., using "notEquals" on type in the "if" block for definitions like Microsoft.ContainerService/managedClusters or Microsoft.Compute/virtualMachineScaleSets).

Implement targeted exemptions using resourceSelectors (e.g., by resourceType for temporary waivers scoped to resource groups).

Ensure modifications align with best practices for least privilege, compliance (e.g., CIS benchmarks), and our multi-tenant environment.
```

### 6.3.4. Publication Date
last week

## 6.4. `P4⁎`

### 6.4.1. URL
https://www.upwork.com/jobs/~021995911249699121827

### 6.4.2. Title
Azure DevOps Pipeline Setup for On-Prem SQL DACPAC Deployment (CI/CD Automation)

### 6.4.3. Description
`P4D` ≔ 
```text
Currently building a CI/CD pipeline in Azure DevOps for deploying SQL Server DACPACs to on-prem environments (UAT and Prod). The pipeline needs to handle building .sqlproj files, generating DACPAC artifacts, and deploying them using the SqlDacpacDeploymentOnMachineGroup@0 task with secure Windows authentication. We have a basic YAML pipeline working for DEV/UAT, but need help refining it for production: adding approvals/gates, integrating Key Vault for credentials (avoid hardcoded), handling cross-database references, ensuring deployment order (e.g., Nexus before Synapse), and scripting agent reinstalls/PowerShell for proxy persistence. The goal is fully automated, repeatable deploys with least-privilege security. Experience with restricted on-prem setups (no internet, domain accounts) is a plus.
```

### 6.4.4. Publication Date
last week

## 6.5. `P5⁎`

### 6.5.1. URL
https://www.upwork.com/jobs/~021995894758345910947

### 6.5.2. Title
Azure AI Document Intelligence SME for Data Extraction Platform

### 6.5.3. Description
`P5D` ≔ 
```text
Building a scalable Azure-based platform for financial document processing (e.g., ingestion, classification, extraction, validation, and GO/NIGO rules).  Collaborate on optimizing the data pipeline, improving AI model accuracy (custom neural models via Document Intelligence), implementing feedback loops for continuous training, and ensuring scalability for thousands of docs/day.

Azure Document Intelligence (Form Recognizer) – custom models, programmatic training/API integration.

Azure data services: Blob Storage, Cosmos DB (partitioning/indexing), Data Factory/Functions for pipelines.

Python backend development for AI/ETL workflows.

AI/ML for document OCR, extraction, and accuracy optimization (e.g., pre-processing, feedback loops).

Experience with financial/document-heavy domains (e.g., banking, transfer agency).

Event-driven architecture (Event Grid, queues, retries).
Strong debugging skills (JSON diffs, API versioning).

Collaborative prototyping in agile teams.
```

### 6.5.4. Publication Date
last week

## 6.6. `P6⁎`

### 6.6.1. URL
https://www.upwork.com/jobs/~021991876712436376190

### 6.6.2. Title
Azure Expert Needed to Reset VMSS Admin Password and Troubleshoot Access Issues

### 6.6.3. Description
`P6D` ≔ 
```text
I'm facing challenges resetting the local admin password for an Azure Virtual Machine Scale Set (VMSS) instance. I need an experienced Azure specialist to guide me through the process or implement the fix remotely (via screen share or direct access if possible). The setup involves:

Azure VMSS with Windows instances (using Bastion for secure RDP access).
Resetting the admin password using PowerShell or Azure CLI in Cloud Shell.
Handling multiple Azure subscriptions and ensuring the correct one is selected.
Applying the VMAccessAgent extension to update the password across instances.
Troubleshooting errors like "Resource group not found" or extension failures.
Verifying access post-reset and providing best practices to avoid future issues.
```

### 6.6.4. Publication Date
3 weeks ago

## 6.7. `P7⁎`

### 6.7.1. URL
https://www.upwork.com/jobs/~021989699095682937282

### 6.7.2. Title
AWS Architecture Diagram for Self-Hosted Active Directory on EC2

### 6.7.3. Description
`P7D` ≔ 
```text
I'm looking for an AWS expert with Active Directory experience to create a high-level architecture diagram for a self-hosted AD setup in AWS. This is for an enterprise migration project extending an on-prem domain (bcbsfl.com) to AWS EC2.
Diagram Requirements:

Overall Structure: Left-to-right flow (on-prem to AWS).
On-Prem Side: GW Data Center with 2 DCs (DC1/DC2).
Connection: Direct Connect/Site-to-Site VPN to AWS Transit Gateway.
AWS Side: Multi-account setup:
gw-core-network: Transit Gateway (hub), Direct Connect.
gw-core-sharedservices: 2 EC2 DCs (AZ-a/b, private subnets, no agents, Tier 0), BlueCat Edge (DNS audit/policy).
gw-core-audit: CloudTrail logs.
gw-core-security: CrowdStrike/InSM JIT.
gw-core-master: Billing/Control Tower (no workloads).
App Landing Zones (e.g., lb-dev-ccaas, cwbz-pega-dev): Domain-joined EC2 VMs (InSM, GPO, SSM), OpenShift/Linux (Centrify/SSSD, no AD).

Flows:
AD replication (on-prem ⇄ AWS DCs).
Domain join (VM → DNS query → BlueCat → DC → Join success).
DNS resolution (VM → BlueCat → DC IP).
InSM JIT (CrowdStrike → DCs/VMs).

Visual Style: Use AWS icons (VPC, subnet, EC2, Transit Gateway, etc.). High-level – no CIDR/IPs, no security groups/NACLs. Group by accounts with boxes.
Tools: Draw.io
```

### 6.7.4. Publication Date
4 weeks ago

## 6.8. `P8⁎`

### 6.8.1. URL
https://www.upwork.com/jobs/~021985766303100858858

### 6.8.2. Title
Fix Real-Time Speaker Diarization Issue in Audio Streaming App Using AssemblyAI

### 6.8.3. Description
`P8D` ≔ 
```text
We're building an AI meeting analysis app that uses AssemblyAI for real-time transcription and xAI's Grok API for analysis. The app processes audio in small chunks (2-5 seconds) for low latency, but we're facing issues with speaker diarization: labels reset across chunks (e.g., Speaker B in one chunk becomes Speaker A in the next), leading to instability in multi-speaker meetings (3-5 speakers). The code is Python-based with PyAudio for capture, and AssemblyAI for transcription (streaming mode).
I need an experienced developer to:

Review the current code (shared via GitHub: https://github.com/visionrd-ai/ai-meeting-analyzer/tree/feat/dual-api) and identify why diarization is unstable (e.g., context loss, audio quality).
Implement fixes for 85%+ accuracy in noisy/overlapping audio, such as overlapping chunks (0.5-1s), pre-processing (noise reduction, normalization), and persistent label remapping (e.g., map temp labels to User1/User2).
Test on 3-5 speaker samples (provide clips if needed) with less than 5s end-to-end latency.
Suggest optimizations for mobile/browser (e.g., React Native compatibility) if possible.
Provide updated code, test results (error rates), and explanation of changes.

Experience with AssemblyAI, real-time audio processing, and diarization is essential.
```

### 6.8.4. Publication Date
last month

## 6.9. `P9⁎`

### 6.9.1. URL
https://www.upwork.com/jobs/~021976763199104265958

### 6.9.2. Title
Audit Script for Security Group Usage in Azure and Microsoft 365

### 6.9.3. Description
`P9D` ≔ 
```text
I need to understand what hybrid security groups (syncing AD to AAD) are actively used for access control, permissions, or roles across Azure resources and Microsoft 365 services. Deleting a group that's still referenced could break authentication, resource access, or integrations, leading to outages or security issues.

Develop PowerShell script that audits a specified security group's usage. It checks for assignments  references in key Azure and M365 areas.

The script takes a group name or Object ID as input and performs a comprehensive scan across the following services (grouped by category for clarity):

Identity and Access (Entra ID/Azure AD): Checks for role assignments (e.g., admin roles like Global Admin) and directory-level usage.
Azure Resources (RBAC and Specific Services): Scans subscriptions for RBAC role assignments; also inspects Key Vault (access policies), Sentinel (workspace permissions), Virtual Desktop (host pools), Backup (vaults), Policy (assignments), SQL (servers/databases), and Storage (accounts).
Microsoft 365 Collaboration Tools:

Teams: Verifies if the group backs a Team or is used in channels/memberships.
SharePoint Online: Flags site permissions (note: this is partial and may need site-specific iteration for full coverage).
OneDrive: Suggests checks for delegated access (via SharePoint audits).
Planner/Project: Looks for associated plans.
Exchange Online: Examines group links and memberships.


Security and Compliance: Audits Purview/Copilot references (e.g., audit logs) and Graph API (app role assignments/consents).
Device Management: Checks Intune role assignments.
```

### 6.9.4. Publication Date
2 months ago

## 6.10. `P10⁎`

### 6.10.1. URL
https://www.upwork.com/jobs/~021970849920727383409

### 6.10.2. Title
Troubleshoot On-Prem SQL Server 2022 Entra ID (Azure AD) Authentication for Service Principal

### 6.10.3. Description
`P10D` ≔ 
```text
Experienced SQL Server DBA needed ASAP to fix Entra ID authentication error on on-premises SQL 2022 instance. Error: "Command 'CREATE USER FROM EXTERNAL PROVIDER' not supported as Azure Active Directory is not configured." Goal: Enable SPN logins via Azure Arc. Quick turnaround
```

### 6.10.4. Publication Date
3 months ago

## 6.11. `P11⁎`

### 6.11.1. URL
https://www.upwork.com/jobs/~021958886974371840651

### 6.11.2. Title
Azure AKS and PostgreSQL Access Configuration


### 6.11.3. Description
`P11D` ≔ 
```text
Looking for an experience Azure Kubernetes Service (AKS) and PostgreSQL expert to assist with configuring and granting access to our PostgreSQL database integrated with our AKS environment. This role involves working with our inBranch Backend architecture deployed on Microsoft Azure
```

### 6.11.4. Publication Date
last quarter

## 6.12. `P12⁎`

### 6.12.1. URL
https://www.upwork.com/jobs/~021945073415357127853

### 6.12.2. Title
Azure Kubernetes SME

### 6.12.3. Description
`P12D` ≔ 
```text
Need Azure Kubernetes SME and need to review code and enable disk encryption.  Gitlab and Teffaform are the two tools used.
```

### 6.12.4. Publication Date
last quarter

## 6.13. `P13⁎`

### 6.13.1. URL
https://www.upwork.com/jobs/~021949510797914266486

### 6.13.2. Title
VS Code Migration Tutorial Creator for SQL Database Projects (From Visual Studio Workflow)


### 6.13.3. Description
`P13D` ≔ 
```text
Need a skilled technical writer/developer experienced in VS Code, SQL Server database projects, and Azure DevOps to create a comprehensive tutorial for migrating workflows from Visual Studio (VS) to VS Code. We are transitioning actuarial and modeling users (e.g., students and experts) to VS Code to avoid licensing costs and streamline processes like publishing DAC packs, handling PowerShell scripts for table scripting, and populating data in repositories (e.g., model point files).

Key Tasks:

Review existing VS documentation (provided) and adapt it into a step-by-step VS Code tutorial, covering:

Environment setup (installing VS Code extensions like Database Projects, PowerShell, SQL tools).

Publishing databases to SQL Server (e.g., handling .sqlproj files, build/publish profiles, permissions flags in XML).

Running PowerShell scripts (e.g., script tables.ps1) post-publish for merge statements and data updates.

Troubleshooting common issues (e.g., data not populating, order dependencies in builds, empty tables).

Branching strategies in Git/Azure DevOps for safe testing (e.g., dev branches for new tables like comp grade LTC).

Make the tutorial user-friendly for non-developers (e.g., actuaries): Include screenshots, code snippets, and explanations of why steps are needed (e.g., avoiding Git data governance pitfalls).

Incorporate best practices for migration, such as validating with a guinea pig user (deep VS expert) for feedback.

Suggest brief extensions for automation insights (e.g., flagging DAC pack dependencies), but focus primarily on the core tutorial.

Deliver a draft in Markdown/PDF format for review, with revisions based on team feedback.

Required Skills:

Expertise in VS Code, Visual Studio, SQL Server (DAC packs, stored procedures like SP generate merge), PowerShell scripting, and Git/Azure DevOps.

Familiarity with database workflows (e.g., table creation/population, merge statements); actuarial/modeling knowledge is a plus.
```

### 6.13.4. Publication Date
last quarter

## 6.14. `P14⁎`

### 6.14.1. URL
https://www.upwork.com/jobs/~021943386746220758613

### 6.14.2. Title
Azure Sentinel filter Windows log data sent to Sentinel


### 6.14.3. Description
`P14D` ≔ 
```text
I need to find ways we can reduce the noice on azure sentinel and save costs.  Its way too high.  I also need below task completed:

Validate Current DCR:

Access the Azure portal Microsoft Sentinel Configuration Data connectors Windows Security Events via AMA.

Confirm the DCR "Microsoft-Security-Event-CustomXPath-DCR" is linked to McBank-Sentinel-Workspace.

Review the current XPath query to ensure it matches the assumed configuration.

Test the New XPath Query:

Create a test DCR (e.g., "Test-Microsoft-Security-Event-CustomXPath-DCR") with the new XPath query.

Apply it to a subset of servers (e.g., a single file server hosting shares accessed by robocopy_sa).

Use a KQL query to verify Event ID 5145 exclusion for robocopy_sa:

SecurityEvent
| where EventID == 5145 and Account == "MCBANK\robocopy_sa"
| summarize count() by TimeGenerated

Expected result: No events after applying the test DCR.

Update the Production DCR:

Navigate to Azure portal Monitor Data Collection Rules Microsoft-Security-Event-CustomXPath-DCR.

Edit the DCR and replace the XPath query with the new one provided above.

Save and deploy the updated DCR to all enrolled machines.
```

### 6.14.4. Publication Date
last quarter


## 6.15. `P15⁎`

### 6.15.1. URL
https://www.upwork.com/jobs/~021921178157218030852

### 6.15.2. Title
Azure Kubernetes connection issues

### 6.15.3. Description
`P15D` ≔ 
```text
We have  connection issues.  We have 2 clusters and aks-02 which responds for my command but not aks-01 fails.No errors in diagnose. Having connection issues.  I feel like we are missing few standards to deploy AKS.
```

### 6.15.4. Publication Date
2 quarters ago


## 6.16. `P16⁎`

### 6.16.1. URL
https://www.upwork.com/jobs/~021979132360843737909

### 6.16.2. Title
Windows WSL2 Expert Needed: Find Alternatives to Ubuntu When Blocked by Group Policy

### 6.16.3. Description
`P16D` ≔ 
```text
I need help implementing alternatives to installing Ubuntu in WSL2 on Windows, as group policy blocks it. Based on these options:

Install a different WSL2 distro like Debian (via PowerShell or manual .appx sideload).
Install WSL2 without a distro and manually import Debian tar file.
Use alternatives like Multipass for Debian VM, VirtualBox/VMware for full Linux VMs, or Azure VM if all else fails.

You'll set this up on my Windows machine (remote access via TeamViewer or similar), test the chosen method, and provide step-by-step documentation. Ensure it bypasses policy restrictions where possible without exemption.
```

### 6.16.4. Publication Date
2 months ago


## 6.17. `P17⁎`

### 6.17.1. URL
https://www.upwork.com/jobs/~021930600114871209360

### 6.17.2. Title
Migrate NPS to new server

### 6.17.3. Description
`P17D` ≔ 
```text
We need to migrate the NPS service used for VPN1 and VPN2.  VPN2 can be tested first before cutting over the primary VPN, i.e. VPN1.
```

### 6.17.4. Publication Date
2 quarters ago

## 6.18. `P18⁎`

### 6.18.1. URL
https://www.upwork.com/jobs/~021956086820766368034

### 6.18.2. Title
Azure Security Specialist for CMK Implementation and Key Backup

### 6.18.3. Description
`P18D` ≔ 
```text
I need an Azure SME to enable Customer-Managed Keys (CMK) for Transparent Data Encryption (TDE) on our Azure SQL development databases and configure secure key backups in Azure Key Vault.
```

### 6.18.4. Publication Date
last quarter

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`, `P7⁎`, `P8⁎`, `P9⁎`, `P10⁎`, `P11⁎`, `P12⁎`, `P13⁎`, `P14⁎`, `P15⁎`, `P16⁎`, `P17⁎`, `P18⁎`}

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

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
an SSL certificate verification error I'm encountering when using Azure CLI on my Windows machine
~~~
```

# 10.
`P1†` ≔† 
```		
Подпроблема (часть `P†`):
~~~
Command failing: az login (aliased to python -m azure.cli).
Error message: "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: CA cert does not include key usage extension (_ssl.c:1028)".
~~~
```

# 11.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
Get az login working without disabling verification (insecure workaround)
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