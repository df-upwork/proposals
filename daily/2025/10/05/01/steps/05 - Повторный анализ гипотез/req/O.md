# 0.
Сегодня 2025-10-05.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021974194499637969231

## 2.2. Title
AWS Networking Engineer Needed for Client VPN Connectivity Issues for Urgent Issue

## 2.3. Description
`PD` ≔ 
```text
## Description
We are seeking a highly skilled AWS Networking Engineer to help us diagnose and fix connectivity issues with our AWS Client VPN setup.  
We have an urgent situation and need to resolve for our company (NITROcrete LLC).  
This occured after an End of Life for an Akami product we were using.

## Our current environment:
- Single VPC (no on-premises connectivity)
- AWS Client VPN endpoint configured with mutual certificate authentication
- Client access via AWS VPN Client and OpenVPN
- VPN transit secured with IPSec via Akamai

## The problem:
We are unable to connect successfully to the VPN using the AWS VPN Client. 
We’ve attempted to configure the Client VPN endpoint but are experiencing persistent DNS resolution failures upon login.

## Scope of Work:
- Diagnose why our AWS VPN Client cannot establish a successful connection
- Review the current Client VPN endpoint setup and associated configuration (CIDR block, routing, DNS, network ACLs, security groups)
- Identify root cause of DNS resolution failures
- Provide clear next steps and a recommended solution path
- Assist with implementing the fix so the VPN is functional

## Deliverables:
- Problem Diagnosis — identify why connections are failing and document the cause.
- Resolution — guide us through the changes needed, and assist in applying them, so our AWS Client VPN endpoint works reliably.

## Required Skills:
- Strong hands-on experience with AWS VPC networking (subnets, route tables, security groups, NACLs)
- Deep understanding of AWS Client VPN endpoints and mutual TLS authentication
- Experience troubleshooting with AWS VPN Client and OpenVPN
- Familiarity with DNS resolution in AWS environments (Route 53, DHCP options sets)
- Ability to explain findings clearly and document changes

## Engagement Model:
- Short-term engagement (diagnosis + fix)
- Immediate availability preferred
```

## 2.4. Tags
VPN
Network Administration
Network Security
System Administration
Linux System Administration

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Engineering & Architecture

### 5.2.2. Количество сотрудников
10-99 people

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Nov 20, 2023
### 5.3.2. Hire rate (%)
0
### 5.3.3. Количество опубликованных проектов (jobs posted)
1
### 5.3.4. Total spent (USD)
0
### 5.3.5. Количество оплаченных часов в почасовых проектах
0
### 5.3.6. Средняя почасовая ставка (USD)
0

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
persistent DNS resolution failures upon login
~~~
```

# 7.
## 7.1.
`Aᨀ` ≔ (мой потенциальный ответ `ꆜ`)

## 7.2.
Содержание `Aᨀ`:
~~~markdown
The most likely causes of your issue:
1) Incorrect configuration of the DNS servers.
1.1) The clients do not receive the correct IP addresses of the DNS resolvers upon connection.
Perhaps, old, inaccessible Akamai DNS servers are specified.
It is necessary to explicitly specify the correct IP addresses of the DNS servers in the «Client VPN endpoint» (`E`) configuration to resolve internal names in the VPC.
This can be:
1.1.1) The IP address of the Route 53 Resolver (`R`), which is the `<VPC_CIDR_BASE> + 2` of the primary IPv4 CIDR block of the VPC.
1.1.2) The IP addresses of Custom DNS servers (e.g., Active Directory Domain Controllers on EC2 instances or `R` Inbound Endpoints).
1.2) If the field is left empty, the DNS configuration is not passed to the client, and it attempts to use its local DNS settings.
The subsequent behavior depends on the tunneling mode of `E` (split-tunnel or full-tunnel).
1.2.1) If split-tunnel mode is enabled, the client will be able to use local DNS servers to resolve public names, but will not be able to resolve internal names in the VPC.
In this mode, AWS VPN Client on Windows does not set Windows Filtering Platform (`WFP`) rules to block local DNS traffic.
1.2.2) If full-tunnel mode is used, all client traffic is directed into the VPN tunnel through the default route (`0.0.0.0/0`).
This route intercepts traffic, including DNS queries, to local and public DNS servers.
Additionally, when using the AWS VPN Client on Windows in full-tunnel mode, `WFP` rules are applied.
These rules force all DNS traffic into the tunnel and block access to local DNS servers to prevent DNS leaks.
If the DNS servers are not specified in the `E` configuration or are unavailable through the tunnel, this leads to a complete failure of DNS resolution.
2) Lack of required authorization rules.
https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html
3) Traffic filtering by Security Groups (`SG`).
3.1) When `E` is associated with subnets, traffic is subject to an `SG`.
If Custom DNS servers are used (e.g., on EC2 instances or a `R` Inbound Endpoint), this `SG` must allow Outbound traffic on port 53 (UDP/TCP) to these servers.
Traffic to `R` is not filtered by `SG`.
3.2) If Custom DNS servers located inside the VPC (e.g., an EC2 instance or a `R` Inbound Endpoint) are used, it is necessary to check their own `SG`.
This `SG` must allow Inbound traffic on port 53 (UDP/TCP).
The Source for this Inbound rule must be the `SG` associated with `E`.
3.3) The network traffic flow has changed after the migration from Akamai.
New rules might not have been added or existing rules may be blocking traffic from the Client VPN network interfaces.
4) Incorrect configuration of Routes.
Routing issues depend on whether the split-tunnel mode is enabled on `E`.
4.1) split-tunnel mode is enabled.
The `E` route table must contain a route to the network where the DNS servers are located.
In this mode, only the routes defined in the `E` route table are added to the client device's route table.
If a route to the DNS servers (e.g., `AmazonProvidedDNS` or Custom DNS) is missing from this table, it will not be added to the client device.
As a result, DNS queries cannot be routed through the VPN tunnel.
Since the client's local network usually does not have routes to the internal IP addresses of the VPC, the queries will fail (time out).
4.2) split-tunnel mode is disabled (full-tunnel).
All client traffic, including DNS requests, is routed into the VPN tunnel via the default route (`0.0.0.0/0`).
In this case, a failure can occur if the traffic cannot reach the DNS servers after entering the VPC.
The traffic enters the subnets associated with `E`.
It is necessary to check the VPC Route Tables of these associated subnets.
These tables must contain the correct routes to the DNS servers being used.
E.g., if Custom DNS servers in a remote network are used (connected via VPC Peering or a Transit Gateway), the corresponding routes are required in the VPC Route Table.
Also, if public name resolution over the internet is required, the VPC Route Table must contain a route to a NAT Gateway or an Internet Gateway.
The absence of these routes at the VPC level will lead to the loss of DNS packets.
5) Traffic blocking by Network Access Control Lists (NACLs).
`E` is associated with specific subnets in the VPC.
Traffic passing through these subnets is filtered by Network Access Control Lists (NACLs).
However, traffic to `R` is not filtered by NACLs.
Therefore, NACLs configuration is required only when using custom DNS servers (e.g., located on EC2 instances or a `R` Inbound Endpoint).
In this case, it is necessary to consider that NACLs are stateless (they do not track connection state).
Unlike `SG`s, NACLs require explicit rules for both outbound and return traffic at the Subnet level.
It is necessary to check the NACLs for the subnets associated with `E` (the source subnets), and the NACL for the Subnet where the Custom DNS servers are located (the destination Subnet), if they are different.
Outbound NACL rules for the source subnets must allow traffic on port 53 (UDP/TCP) to the target subnet.
Inbound NACL rules for the source subnets must allow return traffic from the target Subnet to the ephemeral ports (typically the range `1024-65535`).
Inbound NACL rules for the target Subnet must allow traffic on port 53 (UDP/TCP) from the source subnets.
Outbound NACL rules for the target Subnet must allow return traffic to the ephemeral ports (`1024-65535`) to the source subnets.
The absence of any of these rules will result in DNS failures when using Custom DNS servers.
~~~

# 8.
`Hⰳ(i)?` ≔? 
```
Утверждение, что причина под номером `i` из `Aᨀ` является причиной `P†` в конкретном случае `P⁎`
```
