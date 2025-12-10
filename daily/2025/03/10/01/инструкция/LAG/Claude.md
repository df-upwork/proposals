# Пошаговая инструкция по настройке LAG между парой Juniper SRX300 HA и стеком коммутаторов Cisco Catalyst

## 1. Подготовка инфраструктуры

1.1. Определить интерфейсы, которые будут использоваться для LAG:
   - На устройствах Juniper SRX300 выбрать доступные физические порты (например, ge-0/0/3, ge-0/0/4)
   - На стеке коммутаторов Cisco Catalyst выбрать соответствующие порты (например, GigabitEthernet1/0/1, GigabitEthernet1/0/2)

1.2. Подключить физические кабели между устройствами:
   - Соединить выбранные порты SRX300 с портами на Cisco Catalyst
   - Убедиться в работоспособности физических соединений (световая индикация активна)

## 2. Настройка LAG на устройствах Juniper SRX300

2.1. Активировать поддержку aggregated Ethernet интерфейсов:

```
set chassis aggregated-devices ethernet device-count 2
```

2.2. Создать aggregated Ethernet интерфейс (ae0) и настроить LACP в активном режиме:

```
set interfaces ae0 aggregated-ether-options minimum-links 1
set interfaces ae0 aggregated-ether-options lacp active
```

2.3. Добавить физические интерфейсы в LAG:

```
set interfaces ge-0/0/3 ether-options 802.3ad ae0
set interfaces ge-0/0/4 ether-options 802.3ad ae0
```

2.4. Настроить параметры сети для ae0 интерфейса (в зависимости от требуемой конфигурации сети):

```
set interfaces ae0 unit 0 family ethernet-switching
```

или для Layer 3 интерфейса:

```
set interfaces ae0 unit 0 family inet address 10.1.1.1/24
```

## 3. Интеграция LAG с конфигурацией HA на SRX300

3.1. Создать redundant Ethernet интерфейс для LAG:

```
set interfaces reth2 redundant-ether-options redundancy-group 1
```

3.2. Настроить сетевые параметры на redundant интерфейсе:

```
set interfaces reth2 unit 0 family ethernet-switching
```

или для Layer 3:

```
set interfaces reth2 unit 0 family inet address 10.1.1.1/24
```

3.3. Связать aggregated Ethernet интерфейс с redundant интерфейсом:

```
set interfaces ae0 redundant-ether-options redundant-parent reth2
```

3.4. Повторить аналогичную конфигурацию на втором устройстве SRX300 в кластере HA.

## 4. Настройка EtherChannel на стеке коммутаторов Cisco Catalyst

4.1. Войти в режим конфигурации:

```
enable
configure terminal
```

4.2. Создать и настроить Port-channel интерфейс:

```
interface Port-channel1
 description Uplink to SRX300 HA Pair
 switchport mode trunk
 switchport trunk allowed vlan all
 no shutdown
```

4.3. Настроить физические порты для участия в EtherChannel с активным LACP:

```
interface range GigabitEthernet1/0/1 - 2
 description Uplink to SRX300 HA Pair
 switchport mode trunk
 switchport trunk allowed vlan all
 channel-group 1 mode active
 no shutdown
```

## 5. Проверка работоспособности LAG

5.1. На устройствах Juniper SRX300 проверить статус LAG:

```
show interfaces ae0 extensive
show interfaces reth2 extensive
show lacp interfaces ae0
```

5.2. На коммутаторах Cisco Catalyst проверить статус EtherChannel:

```
show etherchannel summary
show etherchannel 1 detail
show interfaces port-channel 1
```

5.3. Проверить работу отказоустойчивости:
   - Отключить один из физических кабелей LAG
   - Убедиться, что соединение остается активным через оставшиеся линки
   - Проверить статус LAG после отключения порта

## 6. Дополнительные настройки для оптимальной работы

6.1. Настроить параметры агрегирования для оптимальной балансировки нагрузки на SRX300:

```
set forwarding-options enhanced-hash-key family inet layer-3
set forwarding-options enhanced-hash-key family inet layer-4
```

6.2. Настроить метод балансировки нагрузки на Cisco Catalyst:

```
port-channel load-balance src-dst-ip
```

6.3. При необходимости настроить параметры LACP:

```
lacp system-priority 32768
```

## 7. Сохранение конфигурации

7.1. На устройствах Juniper SRX300 применить и сохранить изменения:

```
commit
```

7.2. На коммутаторах Cisco Catalyst сохранить изменения:

```
write memory
```

7.3. Создать резервные копии конфигураций:

```
# На Juniper SRX300
show configuration | display set > `srx300_lag_config.txt`

# На Cisco Catalyst
show running-config > `catalyst_lag_config.txt`
```

## 8. Мониторинг и обслуживание

8.1. Настроить мониторинг LAG через SNMP для интеграции с системой мониторинга сети.

8.2. Регулярно проверять статус LAG:
   - Использовать команды `show interfaces` на SRX300
   - Использовать команды `show etherchannel` на Cisco Catalyst

8.3. Документировать внесенные изменения и сохранять обновленные конфигурации при модификациях.

Данная инструкция обеспечивает настройку высокодоступного LAG-соединения между парой устройств Juniper SRX300 в режиме HA и стеком коммутаторов Cisco Catalyst, что позволяет достичь увеличенной пропускной способности и отказоустойчивости сетевого соединения.