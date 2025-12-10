# Пошаговая инструкция по настройке 4G failover для Juniper SRX300 HA и интеграции с Cisco Catalyst

## 1. Подготовка оборудования и инфраструктуры

1.1. Проверить физическое подключение устройств:
   - Соединить fab-порты между устройствами SRX300 для организации HA-кластера
   - Подключить основной WAN-канал к обоим устройствам SRX300
   - Подключить 4G-модем к active-устройству SRX300
   - Соединить порты от каждого SRX300 к стеку Cisco Catalyst для организации LAG

1.2. Убедиться в совместимости версий программного обеспечения:
   - Рекомендуется использовать JunOS версии 15.1X49-D170 или новее для SRX300
   - Для Cisco Catalyst необходима версия IOS, поддерживающая EtherChannel/LACP

## 2. Настройка chassis cluster на устройствах Juniper SRX300

2.1. На первом устройстве SRX300 выполнить следующие команды:

```
set chassis cluster cluster-id 1 node 0
set chassis cluster reth-count 3
set chassis cluster redundancy-group 0 node 0 priority 200
set chassis cluster redundancy-group 0 node 1 priority 100
set chassis cluster redundancy-group 1 node 0 priority 200
set chassis cluster redundancy-group 1 node 1 priority 100
set chassis cluster control-ports fpc 0 port 0
set chassis cluster control-ports fpc 1 port 0
```

2.2. На втором устройстве SRX300 выполнить:

```
set chassis cluster cluster-id 1 node 1
set chassis cluster control-ports fpc 0 port 0
set chassis cluster control-ports fpc 1 port 0
```

2.3. Перезагрузить оба устройства и проверить статус кластера:

```
show chassis cluster status
```

## 3. Настройка интерфейсов для HA

3.1. Создать redundant ethernet интерфейсы:

```
set interfaces reth0 redundant-ether-options redundancy-group 1
set interfaces reth0 unit 0 family inet address 192.168.1.1/24
set interfaces reth1 redundant-ether-options redundancy-group 1
set interfaces reth1 unit 0 family inet address 10.0.0.1/30
```

3.2. Привязать физические интерфейсы к redundant интерфейсам:

```
set interfaces ge-0/0/0 gigether-options redundant-parent reth0
set interfaces ge-1/0/0 gigether-options redundant-parent reth0
set interfaces ge-0/0/2 gigether-options redundant-parent reth1
set interfaces ge-1/0/2 gigether-options redundant-parent reth1
```

## 4. Настройка 4G интерфейса и failover

4.1. Настроить интерфейс для 4G-модема (пример для USB-модема):

```
set interfaces dl0 unit 0 family inet negotiate-address
set interfaces dl0 dialer-options pool dialer-pool-4g
set interfaces pp0 unit 0 ppp-options chap access-profile 4g-profile
set interfaces pp0 unit 0 ppp-options pap access-profile 4g-profile
set interfaces pp0 unit 0 family inet negotiate-address
set access profile 4g-profile authentication-username [имя_пользователя_4G]
set access profile 4g-profile authentication-password [пароль_4G]
```

4.2. Настроить маршрутизацию для основного и резервного каналов:

```
set routing-options static route 0.0.0.0/0 qualified-next-hop 10.0.0.2 preference 10
set routing-options static route 0.0.0.0/0 qualified-next-hop pp0.0 preference 20
```

## 5. Настройка multiple probes для мониторинга канала

5.1. Настроить RPM probes для проверки доступности основного канала:

```
set services rpm probe monitor-isp test google target address 8.8.8.8
set services rpm probe monitor-isp test google probe-count 5
set services rpm probe monitor-isp test google probe-interval 1
set services rpm probe monitor-isp test google test-interval 10
set services rpm probe monitor-isp test google thresholds successive-loss 3
set services rpm probe monitor-isp test google thresholds total-loss 5

set services rpm probe monitor-isp test cloudflare target address 1.1.1.1
set services rpm probe monitor-isp test cloudflare probe-count 5
set services rpm probe monitor-isp test cloudflare probe-interval 1
set services rpm probe monitor-isp test cloudflare test-interval 10
set services rpm probe monitor-isp test cloudflare thresholds successive-loss 3
set services rpm probe monitor-isp test cloudflare thresholds total-loss 5
```

5.2. Настроить event options для автоматического переключения маршрутизации:

```
set event-options policy primary-down events rpm-test-failed
set event-options policy primary-down attributes-match rpm-test-owner monitor-isp
set event-options policy primary-down then execute-commands commands "set routing-options static route 0.0.0.0/0 qualified-next-hop 10.0.0.2 preference 30"
set event-options policy primary-down then execute-commands commands "set routing-options static route 0.0.0.0/0 qualified-next-hop pp0.0 preference 10"

set event-options policy primary-up events rpm-test-completed
set event-options policy primary-up attributes-match rpm-test-owner monitor-isp
set event-options policy primary-up then execute-commands commands "set routing-options static route 0.0.0.0/0 qualified-next-hop 10.0.0.2 preference 10"
set event-options policy primary-up then execute-commands commands "set routing-options static route 0.0.0.0/0 qualified-next-hop pp0.0 preference 20"
```

## 6. Настройка DNS forwarding

6.1. Настроить DNS серверы для основного канала:

```
set system name-server 8.8.8.8
set system name-server 8.8.4.4
```

6.2. Настроить автоматическое переключение DNS при failover:

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

7.1. Настройка на стороне Juniper SRX300:

```
set chassis aggregated-devices ethernet device-count 2
set interfaces ae0 aggregated-ether-options minimum-links 1
set interfaces ae0 aggregated-ether-options lacp active
set interfaces ge-0/0/3 ether-options 802.3ad ae0
set interfaces ge-0/0/4 ether-options 802.3ad ae0
set interfaces ae0 unit 0 family ethernet-switching vlan members vlan-internal
```

7.2. Интеграция LAG интерфейса с HA-конфигурацией:

```
set interfaces reth2 redundant-ether-options redundancy-group 1
set interfaces reth2 unit 0 family ethernet-switching
set interfaces ae0 ether-options redundant-parent reth2
```

7.3. Настройка на стороне Cisco Catalyst (выполнить через CLI коммутатора):

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

## 8. Проверка и тестирование конфигурации

8.1. Проверить статус chassis cluster:

```
show chassis cluster status
show chassis cluster interfaces
```

8.2. Проверить работу LAG соединения:

```
# На Juniper SRX300
show interfaces ae0 extensive
show interfaces reth2 extensive

# На Cisco Catalyst
show etherchannel summary
show interfaces port-channel 1
```

8.3. Протестировать failover между основным каналом и 4G:

8.3.1. Отключить физически основной WAN-канал
8.3.2. Выполнить следующие команды для проверки переключения:
```
show route 0.0.0.0/0
ping 8.8.8.8 source [внутренний_IP]
```
8.3.3. Проверить корректность DNS резолвинга при использовании 4G:
```
show system services dns forwarding
```

8.4. Протестировать работу HA при отказе основного устройства:

8.4.1. Отключить питание на active-устройстве SRX300
8.4.2. Проверить, что второе устройство берет на себя роль active:
```
show chassis cluster status
```
8.4.3. Убедиться, что сетевое соединение продолжает работать и 4G failover функционирует

## 9. Документирование и резервное копирование настроек

9.1. Сохранить конфигурацию обоих устройств SRX300:

```
show configuration | display set > srx300_ha_config.txt
```

9.2. Сохранить конфигурацию Cisco Catalyst:

```
copy running-config startup-config
show running-config > catalyst_config.txt
```

9.3. Создать документацию с описанием сетевой архитектуры, включая:
   - Схему физических соединений
   - IP-адресацию
   - Описание логики failover и HA
   - Процедуры восстановления при сбоях

Данная инструкция обеспечивает полную настройку 4G failover на паре устройств Juniper SRX300 в режиме HA с интеграцией со стеком коммутаторов Cisco Catalyst через LAG.