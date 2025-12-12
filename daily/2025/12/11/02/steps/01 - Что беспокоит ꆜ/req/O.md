# 0.
Сегодня 2025-12-11.

# 1.
## 1.1.
`UW` ≔Ⱳ https://en.wikipedia.org/wiki/Upwork

## 1.2.
`ꆜ` ≔ ⟨ a potential client on `UW` ⟩

# 2. `P⁎`
## 2.1.
`P⁎` ≔ ⟨ a potential project of `ꆜ`, published on `UW` ⟩

## 2.2.
ꘖ `P⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021998936685512149772'
Title = 'Azure CLI SSL Certificate Verification Expert Needed for Python 3.13 Proxy Issue'
Publication_Date = 'today'
``` 

## 2.3. 
ꘖ `P⁎` ∋ `PD` ≔ ⟪ Description ⟫ 
~~~markdown
#
I need an experienced freelancer to troubleshoot and resolve an SSL certificate verification error I'm encountering when using Azure CLI on my Windows machine (likely running in Git Bash or similar). 
#
The setup involves a custom Python 3.13 environment with Azure CLI installed via pip, and I'm behind a corporate proxy that performs SSL/TLS inspection. 
#
Despite following standard fixes, the issue persists, and I suspect it's related to strict certificate validation in Python 3.13.
# Problem Details:
## Command failing
`az login` (aliased to `python -m azure.cli`).
## Error message
"[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: CA cert does not include key usage extension (_ssl.c:1028)".
## Environment
Windows, Python 3.13, custom `.bashrc` with exports like:
```bash
export PATH=/c/Users/[username]/bin:$PATH
export SSL_CERT_FILE=/path/to/cacert.pem
export REQUESTS_CA_BUNDLE=$SSL_CERT_FILE (and similar for GIT, CURL, NODE).
```

# Attempts made:
- Appended the proxy's root CA certificate (exported from a working machine) to a custom `cacert.pem`.
- Set proxy vars (`HTTP_PROXY`, `HTTPS_PROXY`).

# 
The CA cert is from our internal network/proxy (e.g., Zscaler or similar), but it lacks required extensions like keyCertSign in Key Usage.
#
Works on another machine (possibly older Python or different config), but not here.

# Goal
##
Get `az login` working without disabling verification (insecure workaround). 
##
Prefer secure fixes like using system cert store, proper CA config, or Python tweaks.
~~~

# 4. ꘖ `ꆜ`
ꘖ `ꆜ` ∋
```toml
Location = 'New York, United States'

['Характеристики компании `ꆜ`']
'Сектор экономики' = 'Tech & IT'
'Количество сотрудников' = 'Individual client'

['Характеристики учётной записи `ꆜ` на `UW`']
'Member since' = 'Jun 12, 2020'
'Hire rate (%)' = 65
'Количество опубликованных проектов (jobs posted)' = 417
'Total spent (USD)' = '351K'
'Количество оплаченных часов в почасовых проектах' = 7599
'Средняя почасовая ставка (USD)' = 44.22
```

# 5. `P⠿`
## 
`PO⠿` ~ ⟨ другие проекты `ꆜ` на `UW` ⟩

##
`P⠿` ≔ ⠿{`P⁎`} ⋃ `PO⠿`

##
`Pᵢ` : `P⠿`

## `P1⁎`
###
`P1⁎` : `PO⠿`

###
ꘖ `P1⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021997044898041376943'
Publication_Date = '6 days ago'
Title = 'Azure Networking'
```

### 
ꘖ `P1⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
Need SME to troubleshoot azure firewall issues, route tables, vpn gateway etc.  
Strong preference for those who are azure network certified.  
Not too many people out there with that skillset.
~~~

## `P2⁎`
###
`P2⁎` : `PO⠿`

###
ꘖ `P2⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021996198048289262610'
Title = 'Azure Cosmos DB Developer – Define & Implement Schema for Cosmos DB (NoSQL) Blob Storage Integration'
Publication_Date = 'last week'
``` 

### 
ꘖ `P2⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
Must join call today 11am EST for this tutorial.  
No audio just mouse control.  
Lets connect before 11am call though.

We already have data being stored in Azure Blob Storage (JSON files). We now need to:

Design and define the optimal schema/structure for storing processed/output data in Azure Cosmos DB (Cosmos TV module).
Decide partitioning strategy, indexing policy, container structure, and relationships (embedding vs referencing) for best performance and cost.
Create the actual Cosmos DB database, containers, and implement the schema in a real Azure environment.
Write sample code (preferably C#/.NET 6+) to insert/read data respecting the new schema.
Ensure smooth integration between existing Blob Storage data pipeline and the new Cosmos DB layer.
~~~

## `P3⁎`
###
`P3⁎` : `PO⠿`

###
ꘖ `P3⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021996002015865609380'
Title = 'Azure Policy Expert Needed to Modify and Exempt Policies for AKS Deployments'
Publication_Date = 'STUB'
``` 

### 
ꘖ `P3⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
Modify our existing Azure policies that are currently blocking AKS (Azure Kubernetes Service) deployments. The policies enforce standards like naming conventions, image restrictions, high-privileged roles, and DNS integrations, but they conflict with AKS's managed resources (e.g., random VMSS names, Microsoft-provided images).

Your tasks:

Review our current policy definitions (provided via shared access or code snippets).

Update policy rules to inherently exclude AKS-specific resource types (e.g., using "notEquals" on type in the "if" block for definitions like Microsoft.ContainerService/managedClusters or Microsoft.Compute/virtualMachineScaleSets).

Implement targeted exemptions using resourceSelectors (e.g., by resourceType for temporary waivers scoped to resource groups).

Ensure modifications align with best practices for least privilege, compliance (e.g., CIS benchmarks), and our multi-tenant environment.
~~~

## `P4⁎`
###
`P4⁎` : `PO⠿`

###
ꘖ `P4⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021995911249699121827'
Title = 'Azure DevOps Pipeline Setup for On-Prem SQL DACPAC Deployment (CI/CD Automation)'
Publication_Date = 'last week'
``` 

### 
ꘖ `P4⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
Currently building a CI/CD pipeline in Azure DevOps for deploying SQL Server DACPACs to on-prem environments (UAT and Prod). 
The pipeline needs to handle building .sqlproj files, generating DACPAC artifacts, and deploying them using the `SqlDacpacDeploymentOnMachineGroup@0` task with secure Windows authentication. 
We have a basic YAML pipeline working for DEV/UAT, but need help refining it for production: adding approvals/gates, integrating Key Vault for credentials (avoid hardcoded), handling cross-database references, ensuring deployment order (e.g., Nexus before Synapse), and scripting agent reinstalls/PowerShell for proxy persistence. The goal is fully automated, repeatable deploys with least-privilege security. Experience with restricted on-prem setups (no internet, domain accounts) is a plus.
~~~

## `P5⁎`
###
`P5⁎` : `PO⠿`

###
ꘖ `P5⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021995894758345910947'
Title = 'Azure AI Document Intelligence SME for Data Extraction Platform'
Publication_Date = 'last week'
``` 

### 
ꘖ `P5⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
Building a scalable Azure-based platform for financial document processing (e.g., ingestion, classification, extraction, validation, and GO/NIGO rules).  Collaborate on optimizing the data pipeline, improving AI model accuracy (custom neural models via Document Intelligence), implementing feedback loops for continuous training, and ensuring scalability for thousands of docs/day.

Azure Document Intelligence (Form Recognizer) – custom models, programmatic training/API integration.

Azure data services: Blob Storage, Cosmos DB (partitioning/indexing), Data Factory/Functions for pipelines.

Python backend development for AI/ETL workflows.

AI/ML for document OCR, extraction, and accuracy optimization (e.g., pre-processing, feedback loops).

Experience with financial/document-heavy domains (e.g., banking, transfer agency).

Event-driven architecture (Event Grid, queues, retries).
Strong debugging skills (JSON diffs, API versioning).

Collaborative prototyping in agile teams.
~~~

## `P6⁎`
###
`P6⁎` : `PO⠿`

###
ꘖ `P6⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021991876712436376190'
Title = 'Azure Expert Needed to Reset VMSS Admin Password and Troubleshoot Access Issues'
Publication_Date = '3 weeks ago'
``` 

### 
ꘖ `P6⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
I'm facing challenges resetting the local admin password for an Azure Virtual Machine Scale Set (VMSS) instance. I need an experienced Azure specialist to guide me through the process or implement the fix remotely (via screen share or direct access if possible). The setup involves:

Azure VMSS with Windows instances (using Bastion for secure RDP access).
Resetting the admin password using PowerShell or Azure CLI in Cloud Shell.
Handling multiple Azure subscriptions and ensuring the correct one is selected.
Applying the VMAccessAgent extension to update the password across instances.
Troubleshooting errors like "Resource group not found" or extension failures.
Verifying access post-reset and providing best practices to avoid future issues.
~~~

## `P7⁎`
###
`P7⁎` : `PO⠿`

###
ꘖ `P7⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021989699095682937282'
Title = 'AWS Architecture Diagram for Self-Hosted Active Directory on EC2'
Publication_Date = '4 weeks ago'
``` 

### 
ꘖ `P7⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
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
~~~

## `P8⁎`
###
`P8⁎` : `PO⠿`

###
ꘖ `P8⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021985766303100858858'
Title = 'Fix Real-Time Speaker Diarization Issue in Audio Streaming App Using AssemblyAI'
Publication_Date = 'last month'
``` 

### 
ꘖ `P8⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
We're building an AI meeting analysis app that uses AssemblyAI for real-time transcription and xAI's Grok API for analysis. The app processes audio in small chunks (2-5 seconds) for low latency, but we're facing issues with speaker diarization: labels reset across chunks (e.g., Speaker B in one chunk becomes Speaker A in the next), leading to instability in multi-speaker meetings (3-5 speakers). The code is Python-based with PyAudio for capture, and AssemblyAI for transcription (streaming mode).
I need an experienced developer to:

Review the current code (shared via GitHub: https://github.com/visionrd-ai/ai-meeting-analyzer/tree/feat/dual-api) and identify why diarization is unstable (e.g., context loss, audio quality).
Implement fixes for 85%+ accuracy in noisy/overlapping audio, such as overlapping chunks (0.5-1s), pre-processing (noise reduction, normalization), and persistent label remapping (e.g., map temp labels to User1/User2).
Test on 3-5 speaker samples (provide clips if needed) with less than 5s end-to-end latency.
Suggest optimizations for mobile/browser (e.g., React Native compatibility) if possible.
Provide updated code, test results (error rates), and explanation of changes.

Experience with AssemblyAI, real-time audio processing, and diarization is essential.
~~~

## `P9⁎`
###
`P9⁎` : `PO⠿`

###
ꘖ `P9⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021976763199104265958'
Title = 'Audit Script for Security Group Usage in Azure and Microsoft 365'
Publication_Date = '2 months ago'
``` 

### 
ꘖ `P9⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
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
~~~

## `P10⁎`
###
`P10⁎` : `PO⠿`

###
ꘖ `P10⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021970849920727383409'
Title = 'Troubleshoot On-Prem SQL Server 2022 Entra ID (Azure AD) Authentication for Service Principal'
Publication_Date = '3 months ago'
``` 

### 
ꘖ `P10⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
Experienced SQL Server DBA needed ASAP to fix Entra ID authentication error on on-premises SQL 2022 instance. 
Error: "Command 'CREATE USER FROM EXTERNAL PROVIDER' not supported as Azure Active Directory is not configured." 
Goal: Enable SPN logins via Azure Arc. Quick turnaround
~~~

## `P11⁎`
###
`P11⁎` : `PO⠿`

###
ꘖ `P11⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021958886974371840651'
Title = 'Azure AKS and PostgreSQL Access Configuration'
Publication_Date = 'last quarter'
``` 

### 
ꘖ `P11⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
Looking for an experience Azure Kubernetes Service (AKS) and PostgreSQL expert to assist with configuring and granting access to our PostgreSQL database integrated with our AKS environment. 
This role involves working with our inBranch Backend architecture deployed on Microsoft Azure
~~~

## `P12⁎`
###
`P12⁎` : `PO⠿`

###
ꘖ `P12⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021945073415357127853'
Title = 'Azure Kubernetes SME'
Publication_Date = 'last quarter'
``` 

### 
ꘖ `P12⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
Need Azure Kubernetes SME and need to review code and enable disk encryption.  
Gitlab and Teffaform are the two tools used.
~~~

## `P13⁎`
###
`P13⁎` : `PO⠿`

###
ꘖ `P13⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021949510797914266486'
Title = 'VS Code Migration Tutorial Creator for SQL Database Projects (From Visual Studio Workflow)'
Publication_Date = 'last quarter'
``` 

### 
ꘖ `P13⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
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
~~~

## `P14⁎`
###
`P14⁎` : `PO⠿`

###
ꘖ `P14⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021943386746220758613'
Title = 'Azure Sentinel filter Windows log data sent to Sentinel'
Publication_Date = 'last quarter'
``` 

### 
ꘖ `P14⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
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
~~~

## `P15⁎`
###
`P15⁎` : `PO⠿`

###
ꘖ `P15⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021921178157218030852'
Title = 'Azure Kubernetes connection issues'
Publication_Date = '2 quarters ago'
``` 

### 
ꘖ `P15⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
We have  connection issues.  
We have 2 clusters and aks-02 which responds for my command but not aks-01 fails.No errors in diagnose. Having connection issues.  
I feel like we are missing few standards to deploy AKS.
~~~

## `P16⁎`
###
`P16⁎` : `PO⠿`

###
ꘖ `P16⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021979132360843737909'
Title = 'Windows WSL2 Expert Needed: Find Alternatives to Ubuntu When Blocked by Group Policy'
Publication_Date = '2 months ago'
``` 

### 
ꘖ `P16⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
I need help implementing alternatives to installing Ubuntu in WSL2 on Windows, as group policy blocks it. Based on these options:

Install a different WSL2 distro like Debian (via PowerShell or manual .appx sideload).
Install WSL2 without a distro and manually import Debian tar file.
Use alternatives like Multipass for Debian VM, VirtualBox/VMware for full Linux VMs, or Azure VM if all else fails.

You'll set this up on my Windows machine (remote access via TeamViewer or similar), test the chosen method, and provide step-by-step documentation. Ensure it bypasses policy restrictions where possible without exemption.
~~~

## `P17⁎`
###
`P17⁎` : `PO⠿`

###
ꘖ `P17⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021930600114871209360'
Title = 'Migrate NPS to new server'
Publication_Date = '2 quarters ago'
``` 

### 
ꘖ `P17⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
We need to migrate the NPS service used for VPN1 and VPN2.  VPN2 can be tested first before cutting over the primary VPN, i.e. VPN1.
~~~

## `P18⁎`
###
`P18⁎` : `PO⠿`

###
ꘖ `P18⁎` ∋
```toml
URL = 'https://www.upwork.com/jobs/~021956086820766368034'
Title = 'Azure Security Specialist for CMK Implementation and Key Backup'
Publication_Date = 'last quarter'
``` 

### 
ꘖ `P18⁎` ∋ ⟨ Description ⟩ ≔
~~~markdown
I need an Azure SME to enable Customer-Managed Keys (CMK) for Transparent Data Encryption (TDE) on our Azure SQL development databases and configure secure key backups in Azure Key Vault.
~~~

# 6. `С⁎`
## 6.1.
`С⁎` ≔ ⟨ компания `ꆜ` ⟩

## 6.4.
⊤ (Все `Pᵢ` касаются `С⁎`)

# 7. `T⁎`
`T⁎` ≔ ⟪ задача `ꆜ` в рамках `P⁎` ⟫ ⌖ ⟦`PD`⟧
~~~markdown
Get `az login` working without disabling verification (insecure workaround)
~~~

# 8. `P†`
## `P†`
`P†` ≔† ⟪ проблема `ꆜ` в рамках `P⁎` ⟫ ⌖ ⟦`PD`⟧
~~~markdown
an SSL certificate verification error I'm encountering when using Azure CLI on my Windows machine
~~~

## `P1†`
`P1†` ≔† ⟪ подпроблема `P1†` ⟫ ⌖ ⟦`PD`⟧
~~~markdown
Command failing: `az login` (aliased to python -m azure.cli).
Error message: "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: CA cert does not include key usage extension (_ssl.c:1028)".
~~~

 