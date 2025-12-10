# 0.
Сегодня 2025-11-09.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021986836608333931187

## 2.2. Title
Data Consultant for Database Migration and Integration

## 2.3. Description
`PD` ≔ 
```text
Fountain House is a national mental health nonprofit that founded the clubhouse model for people with serious mental illness.

We are seeking an experienced Microsoft data and technology consultant to migrate a legacy Microsoft Access database to Azure Data Factory.   
The project involves using Elastic Queries and Azure Data Factory to create a secure, scalable, and analytics-ready data environment.

There is related work including connecting to our EHR system, which SQL based and will require building a data dictionary and number specialized views.

# Deliverables
- Migrate legacy Access database to Azure SQL
- Integrate Azure SQL with Eccovia using Elastic Queries
- Enable advanced analytics capabilities
- Create a complete data dictionary with SQL views
- See attached document for detailed scope of work
```

# 3.
## 3.1.
`PD2` ≔ («attached document», который `ꆜ` упоминает в `PD`)

## 3.2. Содержание `PD2` 
```markdown
# What We Need Done:
We need an experienced data consultant to migrate a legacy Microsoft Access database
into Azure SQL and integrate it with our Eccovia system using Elastic Queries and Azure
Data Factory. 
The project involves reviewing the existing Eccovia SQL database,
enabling advanced analytics, and creating a comprehensive data dictionary with all
necessary SQL views. 
The goal is to deliver a secure, scalable, and analytics-ready data
environment for ongoing reporting and insights.

# Current Environment Overview
## SharePoint & Power Apps (Legacy)
- System created for remote service capture (Wellness, Education, Employment, etc.).
- Data entry through Power Apps → SharePoint lists → linked into Access database.

## Access Database
- Houses linked SharePoint tables, analytic sets, service-based tables, “gold” tables for
dashboards, and supporting dictionaries.
- Still contains historical/legacy data with structures that differ from EHR (Ecovia).

## FH Analytics Environment
- Primary repository for manual weekly exports ClientTrack EHR
- Deduplication by type, day, and member.
- Normalizing housing, demographic, and employment data.
- Coding free-text entries (e.g., diagnoses).
- Assigning and maintaining unique IDs.
- Produces initial cleaned analytic sets for reporting.

## Eccovia (ClientTrack EHR)
- Current system of record for service-level data.
- Manual data extraction via Data Explorer queries on a weekly basis.
- All live data capture is now in Eccovia (Power Apps UIs are dormant).

# Challenges & Pain Points
- Manual processes: Weekly extraction and cleaning consume several hours.
- Legacy vs. current data structures: Access/SharePoint schema misaligned with Eccovia.
- Identifier mismatches: Legacy used CGUIDs; Eccovia issues Client IDs, often reassigning
new IDs to returning members.
- Vendor concerns: Eccovia was initially open to Elastic Query access, but later became
hesitant; viewer-level access was proposed as a compromise.
- Data autonomy: Fountain House emphasizes that its data must remain fully accessible


# Migration Strategy Discussion
- Removes reliance on manual exports and enables real-time integration with Power BI.
- Normalization standards include deduplication, data coding, and fuzzy matching (e.g., name
+ DOB).
- Two strategies are under consideration: Start Fresh or Migrate Legacy Historical Data Sets.
- Elastic Query into Azure SQL for access from Eccovia into Azure SQL via meta tables.

# Rough Scope of Work
## 1. Discovery and Planning
- Assess existing Access and Eccovia environments, dependencies, and integration points.
- Review data governance, data quality, and readiness for migration.
- Produce a detailed migration and integration roadmap.

## 2. Pre-Migration Preparation and Schema Work
- Inventory and evaluate existing Access databases and linked sources.
- Conduct initial migration tests using SSMA or equivalent tools.
- Resolve schema issues, normalize data types, and convert Access queries/macros to SQL
views or stored procedures.

## 3. Data Load and Pipeline Development
- Design and implement pipelines using Azure Data Factory, SSMA, or other tools for efficient
data loading.
- Configure and test data loads, validate results, and document the process.
- Optimize for scalability, performance, and maintainability.

## 4. Elastic Query Configuration and Eccovia Integration
- Configure Elastic Queries in Azure SQL to connect directly with the Eccovia SQL database.
- Conduct a structured review of the Eccovia SQL database, including schema and
relationships.
- Implement secure external data sources, credentials, and virtual tables for cross-database
joins.
- Design and document data mappings, transformations, and refresh strategies.

## 5. Data Architecture and Analytics Enablement
- Develop a comprehensive data dictionary defining key tables, relationships, and metrics
across the integrated environment.
- Create SQL views and stored procedures that align with analytical and reporting needs.
- Enable advanced analytics through standardized schemas and performance tuning.
- Collaborate with internal analytics teams to ensure datasets are analysis ready.

## 6. Validation, Documentation, and Handoff
- Validate data accuracy and performance.
- Produce full documentation of architecture, data flows, and query logic.
- Conduct knowledge transfer sessions with internal teams.

## 7. Project Management and Coordination
- Manage project schedule, communication, and milestones.
- Provide regular updates and ensure deliverables meet standards and expectations.

# Expected Outcomes
- Fully migrated and normalized the Azure SQL environment.
- Established Elastic Query integration with Eccovia.
- Comprehensive data dictionary and defined SQL views supporting analytics.
- Documentation and knowledge transfer to Fountain House IT and analytics teams.
```


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
Nov 3, 2025
### 5.3.2. Hire rate (%)
0
### 5.3.3. Количество опубликованных проектов (jobs posted)
1
### 5.3.4. Total spent (USD)
0
### 5.3.5. Количество оплаченных часов в почасовых проектах
0

# 6.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
migrate a legacy Microsoft Access database to Azure Data Factory
~~~
```

 