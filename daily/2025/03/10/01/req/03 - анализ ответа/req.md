## 1.
Потенциальный клиент опубликовал на Upwork следующий проект:
### 1.1. Title
Juniper & Cisco Network Configuration Expert Needed

### 1.2. Description
We are seeking a skilled network expert with experience in Juniper and Cisco technologies to assist in configuring high availability (HA), getting our existing 4G failover to work on Juniper SRX300 HA pair, and a Cisco Catalyst switch stack.
The ideal candidate will have a strong background in network security and performance optimization. You will be responsible for providing JunOS and Cisco IOS configuration changes required to get the 4G WAN failover working, as well as appropriate config to setup LAG (or other) to enable multiple uplinks to our Cisco core switch stack.
4G WAN failover must use multiple probes, and adjust DNS forwarding as necessary.

### 1.3. Tags
Juniper
Network Administration
Network Equipment
Cisco IOS
Cisco Certified Network Professional
Cisco Router
Junos OS
JNCIA-Junos

## 10. Мой потенциальный ответ клиенту (редакция 7)
Я хочу ответить клиенту так:
~~~
HA on a Juniper SRX300 pair is done as follows:
1) Физически соединитm устройства:
1.1) Cоединить ge-0/0/1 (node0) с ge-1/0/1 (node1) для control link.
1.2) Cоединить ge-0/0/7 (node0) с ge-1/0/7 (node1) для fabric link.
1.3) Подключить 4G-модемы в соответствии с выбранной схемой HA:
1.3.1) Два отдельных USB-модема (по одному на каждую ноду), чтобы физически обеспечить 4G на обеих SRX.
1.3.2) Один 4G-модем с двумя физическими интерфейсами (редкий вариант).
1.3.3) Один внешний 4G-роутер с Ethernet-портом, подключаем его к reth-интерфейсу. 
Тогда 4G «общий» для обеих нод кластера.
1.3.4) Если имеется только один USB-модем и нет второго выхода, полноценный автоматический HA не получится: придётся вручную переключать модем на secondary или использовать внешний роутер.
1.4) Соединить несколько портов (для LAG) от каждого SRX300 к стеку Cisco Catalyst
2) Выполнить первоначальную настройку на обоих устройствах:
```
set system host-name srx300-node0
set system root-authentication plain-text-password
set system services ssh
```
3) Настроить интерфейсы на primary SRX300:
не нужен.
4) Настроить интерфейсы на secondary SRX300:
не нужен.
5) На primary SRX300 настроить chassis cluster:
5.1) Если SRX ещё работает в standalone-режиме, сначала включаем кластер:
```
set chassis cluster cluster-id 1 node 0 reboot
commit
request system reboot
```
Устройство перезагрузится, перейдёт в кластерный режим, и интерфейсы будут переименованы в формате `ge-0/0/x`, `ge-1/0/x`.
5.2)
```
set chassis cluster cluster-id 1 node 0
set chassis cluster reth-count 2
set chassis cluster redundancy-group 0 node 0 priority 200
set chassis cluster redundancy-group 0 node 1 priority 100
set chassis cluster redundancy-group 1 node 0 priority 200
set chassis cluster redundancy-group 1 node 1 priority 100
set chassis cluster redundancy-group 1 node 0 interface-monitor ge-0/0/2 weight 255
set chassis cluster redundancy-group 1 node 0 interface-monitor ge-0/0/0 weight 255
set chassis cluster redundancy-group 1 node 1 interface-monitor ge-1/0/2 weight 255
set chassis cluster redundancy-group 1 node 1 interface-monitor ge-1/0/0 weight 255
set chassis cluster control-link ge-0/0/1
set chassis cluster cluster-id 1 node 0 fabric-link ge-0/0/7
commit check
commit
request system reboot
```
6) После успешной перезагрузки primary SRX300, на secondary SRX300 (node1) настроить chassis cluster:
6.1) Если SRX ещё работает в standalone-режиме, сначала включаем кластер (аналогично пункту 5.1):
```
set chassis cluster cluster-id 1 node 1 reboot
commit
request system reboot
```
6.2)
```
set chassis cluster cluster-id 1 node 1
set chassis cluster control-link ge-1/0/1
set chassis cluster cluster-id 1 node 1 fabric-link ge-1/0/7
commit check
commit
request system reboot
```
7) Настроить redundant ethernet интерфейсы:
```
set interfaces reth0 redundant-ether-options redundancy-group 1
set interfaces reth0 aggregated-ether-options lacp active
set interfaces reth0 aggregated-ether-options minimum-links 1
set interfaces reth0 unit 0 family inet address 192.168.1.254/24

set interfaces reth1 redundant-ether-options redundancy-group 1
set interfaces reth1 aggregated-ether-options lacp active
set interfaces reth1 unit 0 family inet address 10.0.0.254/30
```
8) Привязать физические интерфейсы к redundant интерфейсам:
```
set interfaces ge-0/0/0 gigether-options redundant-parent reth0
set interfaces ge-1/0/0 gigether-options redundant-parent reth0
set interfaces ge-0/0/2 gigether-options redundant-parent reth1
set interfaces ge-1/0/2 gigether-options redundant-parent reth1
```
9) Настроить 4G-интерфейс на primary SRX300 (PPP):
```
set interfaces pp0 unit 0 family inet negotiate-address
set interfaces pp0 unit 0 ppp-options chap access-profile 4g-profile
set interfaces pp0 unit 0 ppp-options pap access-profile 4g-profile
set access profile 4g-profile authentication-order [ chap pap ]
set access profile 4g-profile client [username] secret [password]
```
10) Настроить резервный маршрут через 4G:
```
set routing-options static route 0.0.0.0/0 qualified-next-hop 10.0.0.253 preference 10
set routing-options static route 0.0.0.0/0 next-hop pp0.0 preference 20
```
11) Настроить `ip-monitoring` для проверки основного канала:
```
set services ip-monitoring enable

set services ip-monitoring policy MAIN-LINK test test1 probe-count 5
set services ip-monitoring policy MAIN-LINK test test1 test-interval 5
set services ip-monitoring policy MAIN-LINK test test1 target 8.8.8.8 
set services ip-monitoring policy MAIN-LINK test test1 source-interface reth1.0

set services ip-monitoring policy MAIN-LINK then preferred-route route 0.0.0.0/0 next-hop 10.0.0.253 qualified-next-hop pp0.0
set services ip-monitoring policy MAIN-LINK then failover-route route 0.0.0.0/0 next-hop pp0.0
```
12)
не нужен.

13) Настроить DNS серверы для основного канала:
```
set system name-server 8.8.8.8
set system name-server 8.8.4.4
```
14) Настроить DNS forwarding с автоматическим переключением:
```
set system services dns forwarding server 8.8.8.8
set system services dns forwarding server 8.8.4.4

set event-options policy primary-down events chassiscluster_status_change
set event-options policy primary-down within 30
set event-options policy primary-down match "RG1: node0 lost the primary role"
set event-options policy primary-down then execute-commands commands "delete system services dns forwarding server 8.8.8.8"
set event-options policy primary-down then execute-commands commands "delete system services dns forwarding server 8.8.4.4"
set event-options policy primary-down then execute-commands commands "set system services dns forwarding server [the DNS server of the 4G provider]"
set event-options policy primary-down then execute-commands commands "commit"

set event-options policy primary-up events chassiscluster_status_change
set event-options policy primary-up within 30
set event-options policy primary-up match   "RG1: node0 gained the primary role"
set event-options policy primary-up then execute-commands commands "delete system services dns forwarding server [the DNS server of the 4G provider]"
set event-options policy primary-up then execute-commands commands "set system services dns forwarding server 8.8.8.8"
set event-options policy primary-up then execute-commands commands "set system services dns forwarding server 8.8.4.4"
set event-options policy primary-up then execute-commands commands "commit"
```
15) Настроить Link Aggregation на SRX300:
```
set interfaces ge-0/0/3 gigether-options redundant-parent reth0
set interfaces ge-1/0/3 gigether-options redundant-parent reth0
```
16) Настройка EtherChannel на Cisco Catalyst:
```
interface range GigabitEthernet1/0/1-2
 description Link to SRX300 HA Pair
 channel-group 1 mode active
 no shutdown

interface Port-channel1
 description LAG to SRX300 HA Pair
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 no shutdown
```
17) Проверить статус HA кластера:
```
show chassis cluster status
show chassis cluster interfaces
```
18) Проверить работу LAG:
```
show interfaces reth0 extensive
show lacp interfaces reth0
```
19) Протестировать failover:
19.1) Физически отключить основной WAN-канал
19.2) Проверить, переключилось ли соединение на 4G
19.3) Убедиться, что DNS forwarding корректно изменился
19.4) Подключить основной канал обратно и проверить возврат к нему
20) Протестировать HA:
20.1) Выключить primary устройство SRX300
20.2) Убедиться, что secondary устройство взяло на себя функции
20.3) Включить primary устройство и убедиться в корректном восстановлении кластера
21) Настроить security-зоны:
```
set security zones security-zone TRUST interfaces reth0.0 host-inbound-traffic system-services all
set security zones security-zone TRUST interfaces reth0.0 host-inbound-traffic protocols all
set security zones security-zone UNTRUST interfaces reth1.0 host-inbound-traffic system-services ping
set security zones security-zone UNTRUST interfaces reth1.0 host-inbound-traffic protocols bgp  # пример
set security zones security-zone UNTRUST interfaces pp0.0 host-inbound-traffic system-services ping
```
22) Настроить NAT и security-политики:
```
set security nat source rule-set RS1 from zone TRUST to zone UNTRUST
set security nat source rule-set RS1 rule R1 match source-address 192.168.1.0/24
set security nat source rule-set RS1 rule R1 then source-nat interface
set security policies from-zone TRUST to-zone UNTRUST policy ALLOW-ALL match source-address any
set security policies from-zone TRUST to-zone UNTRUST policy ALLOW-ALL match destination-address any
set security policies from-zone TRUST to-zone UNTRUST policy ALLOW-ALL match application any
set security policies from-zone TRUST to-zone UNTRUST policy ALLOW-ALL then permit
```
~~~

## 11. Твоя задача
Есть ли в моём ответе фактические ошибки?
Есть ли в моём ответе логические ошибки?
Упустил ли я в ответе нечто важное?