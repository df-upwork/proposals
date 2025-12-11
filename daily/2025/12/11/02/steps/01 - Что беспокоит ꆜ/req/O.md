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
STUB

### 6.9.2. Title
STUB

### 6.9.3. Description
`P9D` ≔ 
```text
STUB
```

### 6.9.4. Publication Date
STUB

## 6.10. `P10⁎`

### 6.10.1. URL
STUB

### 6.10.2. Title
STUB

### 6.10.3. Description
`P10D` ≔ 
```text
STUB
```

### 6.10.4. Publication Date
STUB

## 6.11. `P11⁎`

### 6.11.1. URL
STUB

### 6.11.2. Title
STUB

### 6.11.3. Description
`P11D` ≔ 
```text
STUB
```

### 6.11.4. Publication Date
STUB

## 6.12. `P12⁎`

### 6.12.1. URL
STUB

### 6.12.2. Title
STUB

### 6.12.3. Description
`P12D` ≔ 
```text
STUB
```

### 6.12.4. Publication Date
STUB

## 6.13. `P13⁎`

### 6.13.1. URL
STUB

### 6.13.2. Title
STUB

### 6.13.3. Description
`P13D` ≔ 
```text
STUB
```

### 6.13.4. Publication Date
STUB

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`, `P7⁎`, `P8⁎`, `P9⁎`, `P10⁎`, `P11⁎`, `P12⁎`, `P13⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 8.
## 8.1.
`С⁎` ≔ 
```
Компания `ꆜ`:
~~~
STUB
~~~
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
STUB
~~~
```

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
STUB
~~~
```

# 10.
## 10.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
STUB
~~~
```

## 10.2.
`T2⁎` ≔ 
```		
Подзадача из `PD`:
~~~
STUB
~~~
```

## 10.3.
`T3⁎` ≔ 
```		
Подзадача из `PD`:
~~~
STUB
~~~
```

## 10.4.
`T4⁎` ≔ 
```		
Подзадача из `PD`:
~~~
STUB
~~~
```

## 10.5.
`T5⁎` ≔ 
```		
Подзадача из `PD`:
~~~
STUB
~~~
```

## 10.6.
`T6⁎` ≔ 
```		
Подзадача из `PD`:
~~~
STUB
~~~
```

# 11.
## 11.1.
`Q1⁎` ≔ (Вопрос `ꆜ` §2.5.1)

## 11.2.
`Q2⁎` ≔ (Вопрос `ꆜ` §2.5.2)

## 11.3.
`Q3⁎` ≔ (Вопрос `ꆜ` §2.5.3)

## 11.4.
`Q4⁎` ≔ (Вопрос `ꆜ` §2.5.4)

## 11.5.
`Q5⁎` ≔ (Вопрос `ꆜ` §2.5.5)
 