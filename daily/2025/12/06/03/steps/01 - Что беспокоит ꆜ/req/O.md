# 0.
Сегодня 2025-12-06.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021996977273470295441

## 2.2. Title
GCP DevOps help needed

## 2.3. Description
`PD` ≔ 
```text
#
We need help with multiple items in GCP but to get started below is the first item we need help with:

# Project Summary
Google Datastream to MongoDB Atlas via PSC

# Objective
Establish a private connection between Google Cloud Datastream and MongoDB Atlas using Private Service Connect (PSC) to avoid public internet traversal.

# The Blockers
Datastream fails to connect with Connection Refused or Timeout. 

# Symptom
The error logs show Datastream attempting to connect to Atlas Public IPs instead of the PSC Private IPs 

# Root Cause Diagnosis
Split-Horizon DNS Failure. Datastream is ignoring the Private DNS Zone in the peered VPC and falling back to Public DNS (which resolves the Atlas Wildcard to public IPs).

# Infrastructure State (What is Configured)
## 1. Network & Connectivity:

### VPC
datastream-net (Project: internal-resources-corp).

### PSC Endpoints
2 Endpoints created targeting the Atlas Service Attachment.

### Private Service Access (PSA):
- Peering created with servicenetworking.googleapis.com.
- Crucial Config: export-custom-routes and import-custom-routes are set to TRUE on the peering connection.
- Reserved Range: [range]/24 for the service link.

## 2. DNS Configuration (Cloud DNS):

### Zone
mongo-psc-isolated (Private Zone).

### Visibility
Attached to datastream-net network.

### Records
We explicitly mapped the Canonical Atlas Hostnames (found via hello command) to the local PSC IPs.

## 3. Firewalls:
### GCP Ingress
Allow 0.0.0.0/0 (Temporary "Sledgehammer" rule for debugging).

### GCP Egress
Allow UDP:53 (DNS) to 0.0.0.0/0.

### MongoDB Atlas Access List
[range]/24 is whitelisted.

# Verification Results 
We deployed a DNS Verifier VM inside the datastream-net VPC to validate the infrastructure.

## ✅ VM DNS Test
nslookup on the VM correctly resolves the Atlas hostnames to Private IPs 

## ✅ VM Connectivity Test
mongosh on the VM connects successfully to the cluster using the Private IPs.

## ❌ Datastream Test
Datastream Connection Profile test fails. 
Configuring a dummy hostname (...mongodb.net-RESET) proves it resolves to Public IPs, meaning Datastream is not utilizing the Custom Routes exported via Peering.
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Coraopolis

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
100-1,000

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Nov 10, 2019
### 5.3.2. Hire rate (%)
79
### 5.3.3. Количество опубликованных проектов (jobs posted)
28
### 5.3.4. Total spent (USD)
239K
### 5.3.5. Количество оплаченных часов в почасовых проектах
3464
### 5.3.6. Средняя почасовая ставка (USD)
59.92

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
Establish a private connection between Google Cloud Datastream and MongoDB Atlas using Private Service Connect (PSC) to avoid public internet traversal.
~~~
```

# 10.
`P†` ≔†
```
Проблема на пути к `T⁎`, о которой `ꆜ` пишет в `PD`:
~~~
```

# 11.
## 11.1.
`P1†` ≔ 
```		
Часть `P†`, описанная `PD` так:
~~~
The error logs show Datastream attempting to connect to Atlas Public IPs instead of the PSC Private IPs 
~~~
```

## 11.2.
`P2†` ≔ 
```		
Часть `P†`, описанная `PD` так:
~~~
Datastream is ignoring the Private DNS Zone in the peered VPC and falling back to Public DNS (which resolves the Atlas Wildcard to public IPs)
~~~
```

## 11.3.
`P3†` ≔ 
```		
Часть `P†`, описанная `PD` так:
~~~
Datastream Test: Datastream Connection Profile test fails. Configuring a dummy hostname (...mongodb.net-RESET) proves it resolves to Public IPs, meaning Datastream is not utilizing the Custom Routes exported via Peering.
~~~
```

 