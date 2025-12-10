# Инструкция по настройке High Availability для пары Juniper SRX300 с резервированием через 4G WAN

## 1. Подготовка оборудования

1.1. Убедиться в наличии всего необходимого оборудования:
   - Два маршрутизатора Juniper SRX300
   - 4G модем (USB или внешний)
   - Кабели для соединения устройств
   - Стек коммутаторов Cisco Catalyst

1.2. Физически соединить устройства:
   - Соединить порты для кластеризации (например, ge-0/0/1) между двумя SRX300
   - Подключить основной WAN-канал к обоим устройствам SRX300
   - Подключить 4G модем к primary SRX300
   - Соединить несколько портов (для LAG) от каждого SRX300 к стеку Cisco Catalyst

## 2. Базовая настройка SRX300

2.1. Выполнить первоначальную настройку на обоих устройствах:

```
set system host-name srx300-node0
set system root-authentication plain-text-password
set system services ssh
set system services web-management http interface ge-0/0/0.0
```

2.2. Настроить интерфейсы на primary SRX300:

```
set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.1/24
set interfaces ge-0/0/2 unit 0 family inet address 10.0.0.1/30 # Основной WAN
set interfaces lt-0/0/0 unit 0 family inet address 169.254.0.1/30 # Интерфейс для HA
```

2.3. Настроить интерфейсы на secondary SRX300:

```
set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.2/24
set interfaces ge-0/0/2 unit 0 family inet address 10.0.0.2/30 # Основной WAN
set interfaces lt-0/0/0 unit 0 family inet address 169.254.0.2/30 # Интерфейс для HA
```

## 3. Настройка High Availability (HA)

3.1. На primary SRX300 настроить chassis cluster:

```
set chassis cluster cluster-id 1 node 0
set chassis cluster reth-count 3
set chassis cluster redundancy-group 0 node 0 priority 200
set chassis cluster redundancy-group 0 node 1 priority 100
set chassis cluster redundancy-group 1 node 0 priority 200
set chassis cluster redundancy-group 1 node 1 priority 100
set chassis cluster redundancy-group 1 interface-monitor ge-0/0/2 weight 255
set chassis cluster redundancy-group 1 preempt
set chassis cluster control-ports fpc 0 port 0
set chassis cluster control-ports fpc 1 port 0
```

3.2. На secondary SRX300 настроить chassis cluster:

```
set chassis cluster cluster-id 1 node 1
set chassis cluster control-ports fpc 0 port 0
set chassis cluster control-ports fpc 1 port 0
```

3.3. Настроить redundant ethernet интерфейсы:

```
set interfaces reth0 redundant-ether-options redundancy-group 1
set interfaces reth0 unit 0 family inet address 192.168.1.254/24
set interfaces reth1 redundant-ether-options redundancy-group 1
set interfaces reth1 unit 0 family inet address 10.0.0.254/30
```

3.4. Привязать физические интерфейсы к redundant интерфейсам:

```
set interfaces ge-0/0/0 gigether-options redundant-parent reth0
set interfaces ge-1/0/0 gigether-options redundant-parent reth0
set interfaces ge-0/0/2 gigether-options redundant-parent reth1
set interfaces ge-1/0/2 gigether-options redundant-parent reth1
```

## 4. Настройка 4G WAN интерфейса и failover

4.1. Настроить 4G интерфейс на primary SRX300:

```
set interfaces dl0 unit 0 family inet negotiate-address
set interfaces dl0 dialer-options pool dialer-pool-4g
set interfaces pp0 unit 0 ppp-options chap access-profile 4g-profile
set interfaces pp0 unit 0 ppp-options pap access-profile 4g-profile
set interfaces pp0 unit 0 family inet negotiate-address
set access profile 4g-profile authentication-username [имя_пользователя]
set access profile 4g-profile authentication-password [пароль]
```

4.2. Настроить резервный маршрут через 4G:

```
set routing-options static route 0.0.0.0/0 qualified-next-hop 10.0.0.254 preference 10
set routing-options static route 0.0.0.0/0 qualified-next-hop pp0.0 preference 20
```

## 5. Настройка multiple probes для мониторинга соединения

5.1. Настроить RPM (Real-time Performance Monitoring) для проверки основного канала:

```
set services rpm probe primary-isp test google server 8.8.8.8
set services rpm probe primary-isp test google probe-count 5
set services rpm probe primary-isp test google probe-interval 1
set services rpm probe primary-isp test google test-interval 10
set services rpm probe primary-isp test google thresholds successive-loss 3
set services rpm probe primary-isp test google thresholds total-loss 5

set services rpm probe primary-isp test cloudflare server 1.1.1.1
set services rpm probe primary-isp test cloudflare probe-count 5
set services rpm probe primary-isp test cloudflare probe-interval 1
set services rpm probe primary-isp test cloudflare test-interval 10
set services rpm probe primary-isp test cloudflare thresholds successive-loss 3
set services rpm probe primary-isp test cloudflare thresholds total-loss 5
```

5.2. Настроить Event Options для реагирования на результаты проверок:

```
set event-options policy primary-down events rpm-test-failed
set event-options policy primary-down attributes-match rpm-test-owner primary-isp
set event-options policy primary-down then execute-commands commands "set routing-options static route 0.0.0.0/0 qualified-next-hop 10.0.0.254 preference 30"
set event-options policy primary-down then execute-commands commands "set routing-options static route 0.0.0.0/0 qualified-next-hop pp0.0 preference 10"

set event-options policy primary-up events rpm-test-completed
set event-options policy primary-up attributes-match rpm-test-owner primary-isp
set event-options policy primary-up then execute-commands commands "set routing-options static route 0.0.0.0/0 qualified-next-hop 10.0.0.254 preference 10"
set event-options policy primary-up then execute-commands commands "set routing-options static route 0.0.0.0/0 qualified-next-hop pp0.0 preference 20"
```

## 6. Настройка DNS forwarding

6.1. Настроить DNS серверы для основного канала:

```
set system name-server 8.8.8.8
set system name-server 8.8.4.4
```

6.2. Настроить DNS forwarding с автоматическим переключением:

```
set system services dns forwarding server 8.8.8.8
set system services dns forwarding server 8.8.4.4

set event-options policy primary-down then execute-commands commands "delete system services dns forwarding server 8.8.8.8"
set event-options policy primary-down then execute-commands commands "delete system services dns forwarding server 8.8.4.4"
set event-options policy primary-down then execute-commands commands "set system services dns forwarding server [DNS_сервер_4G_провайдера]"

set event-options policy primary-up then execute-commands commands "delete system services dns forwarding server [DNS_сервер_4G_провайдера]"
set event-options policy primary-up then execute-commands commands "set system services dns forwarding server 8.8.8.8"
set event-options policy primary-up then execute-commands commands "set system services dns forwarding server 8.8.4.4"
```

## 7. Настройка LAG между SRX300 и Cisco Catalyst

7.1. Настроить Link Aggregation на SRX300:

```
set chassis aggregated-devices ethernet device-count 2
set interfaces ae0 aggregated-ether-options minimum-links 1
set interfaces ae0 aggregated-ether-options lacp active
set interfaces ge-0/0/3 ether-options 802.3ad ae0
set interfaces ge-0/0/4 ether-options 802.3ad ae0
set interfaces ae0 unit 0 family ethernet-switching vlan members vlan-internal
```

7.2. Настройка EtherChannel на Cisco Catalyst:

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

## 8. Проверка и тестирование

8.1. Проверить статус HA кластера:

```
show chassis cluster status
show chassis cluster interfaces
```

8.2. Проверить работу LAG:

```
show interfaces ae0 extensive
```

8.3. Протестировать failover:
   - Физически отключить основной WAN-канал
   - Проверить, переключилось ли соединение на 4G
   - Убедиться, что DNS forwarding корректно изменился
   - Подключить основной канал обратно и проверить возврат к нему

8.4. Протестировать HA:
   - Выключить primary устройство SRX300
   - Убедиться, что secondary устройство взяло на себя функции
   - Включить primary устройство и убедиться в корректном восстановлении кластера

Эта инструкция обеспечит настройку высокодоступной архитектуры сети с использованием пары Juniper SRX300 и резервированием через 4G WAN, а также корректную интеграцию со стеком коммутаторов Cisco Catalyst через агрегированный канал.