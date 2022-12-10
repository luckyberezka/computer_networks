# Homework 4

Далее находится описание четвертой самостоятельной работы. Сначала показана настройка сети, далее приведены примеры использования и проверка работоспособности. Конфиги и лабораторная работа загружены в данную дирректорию. (РАБОТА ПОКА НЕДОДЕЛАНА, НАСТРОЕНО ВСЁ КРОМЕ IPSEC)

![image info](topology.jpg)

## Краткая структура сети



## Настройка сети

1) R1 (Router)

```

Router(config)#int e0/0
Router(config-if)#no shutdown
Router(config-if)#ip address 10.0.10.1 255.255.255.0
Router(config-if)#description VPC_1
Router(config-if)#exit
Router(config)#int e0/1
Router(config-if)#no shutdown
Router(config-if)#ip address 192.168.10.2 255.255.255.0
Router(config-if)#description R4
Router(config-if)#exit
Router(config)#ip route 0.0.0.0 0.0.0.0 192.168.10.1
Router(config)#ip route 10.0.20.2 255.255.255.255 10.1.10.2
Router(config)#ip route 10.0.30.2 255.255.255.255 10.2.10.2
Router(config)#interface tunnel 100
Router(config-if)#no shutdown
Router(config-if)#ip address 10.1.10.1 255.255.255.252
Router(config-if)#tunnel source 192.168.10.2
Router(config-if)#tunnel destination 192.168.20.2
Router(config-if)#ip mtu 1400
Router(config-if)#ip tcp adjust-mss 1360
Router(config-if)#exit
Router(config)#int tunnel 200
Router(config-if)#no shutdown
Router(config-if)#ip address 10.2.10.1 255.255.255.252
Router(config-if)#tunnel source 192.168.10.2
Router(config-if)#tunnel destination 192.168.30.2
Router(config-if)#ip mtu 1400
Router(config-if)#ip tcp adjust-mss 1360
Router(config-if)#exit
Router(config)#exit


```

2) R2 (Router)

```

Router(config)#int e0/0
Router(config-if)#no shutdown
Router(config-if)#ip address 192.168.20.2 255.255.255.0
Router(config-if)#description R4
Router(config-if)#exit
Router(config)#int e0/1
Router(config-if)#no shutdown
Router(config-if)#description VPC_2
Router(config-if)#ip address 10.0.20.1 255.255.255.0
Router(config-if)#exit
Router(config)#ip route 0.0.0.0 0.0.0.0 192.168.20.1
Router(config)#ip route 10.0.10.2 255.255.255.255 10.1.10.1
Router(config)#int tunnel 100
Router(config-if)#no shutdown
Router(config-if)#ip address 10.1.10.2 255.255.255.252
Router(config-if)#tunnel source 192.168.20.2
Router(config-if)#tunnel destination 192.168.10.2
Router(config-if)#ip mtu 1400
Router(config-if)#ip tcp adjust-mss 1360
Router(config-if)#exit
Router(config)#exit


```
3) R3 (Router)

```

Router(config)#int e0/0
Router(config-if)#description R4
Router(config-if)#no shutdown
Router(config-if)#ip address 192.168.30.2 255.255.255.0
Router(config-if)#exit
Router(config)#int e0/1
Router(config-if)#description VPC_3
Router(config-if)#no shutdown
Router(config-if)#ip address 10.0.30.1 255.255.255.0
Router(config-if)#exit
Router(config)#ip route 0.0.0.0 0.0.0.0 192.168.30.1
Router(config)#ip route 10.0.10.2 255.255.255.255 10.2.10.1
Router(config)#int tunnel 200
Router(config-if)#no shutdown
Router(config-if)#ip address 10.2.10.2 255.255.255.252
Router(config-if)#tunnel source 192.168.30.2
Router(config-if)#tunnel destination 192.168.10.2
Router(config-if)#ip mtu 1400
Router(config-if)#ip tcp adjust-mss 1360
Router(config-if)#exit
Router(config)#exit


```

4) R4 (Router)

```

Router(config)#int e0/0
Router(config-if)#description R1
Router(config-if)#no shutdown
Router(config-if)#ip address 192.168.10.1 255.255.255.0
Router(config-if)#exit
Router(config)#int e0/1
Router(config-if)#description R2
Router(config-if)#no shutdown
Router(config-if)#ip address 192.168.20.1 255.255.255.0
Router(config-if)#exit
Router(config)#int e0/2
Router(config-if)#no shutdown
Router(config-if)#description R3
Router(config-if)#ip address 192.168.30.1 255.255.255.0
Router(config-if)#exit
Router(config)#exit


```

5) VPC_1 (Client)

```

VPCS> ip 10.0.10.2 255.255.255.0 10.0.10.1

```

6) VPC_2 (Client)

```

VPCS> ip 10.0.20.2 255.255.255.0 10.0.20.1

```

7) VPC_3 (Client)

```

VPCS> ip 10.0.30.2 255.255.255.0 10.0.30.1

```
## Проверка работоспособности

