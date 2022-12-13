# computer_networks

Тут размещены кайфовые реализации самостоятельных работы по Компьютерным Сетям.

R2

```
Router(config)#int e0/1
Router(config-if)#no shutdown
Router(config-if)#ip address 211.211.1.1 255.255.255.0
Router(config-if)#exit
Router(config)#int e0/0
Router(config-if)#no shutdown
Router(config-if)#ip address 211.211.2.1 255.255.255.0
Router(config-if)#exit
Router(config)#int e0/2
Router(config-if)#no shutdown
Router(config-if)#ip address 211.211.3.1 255.255.255.0
Router(config-if)#exit
Router(config)#exit

```


R1 

```
Router(config)#int e0/1
Router(config-if)#no shutdown
Router(config-if)#ip address 10.0.10.1 255.255.255.0
Router(config-if)#exit
Router(config)#int e0/2
Router(config-if)#no shutdown
Router(config-if)#ip address 211.211.1.2 255.255.255.0
Router(config-if)#exit
Router(config)#ip route 0.0.0.0 0.0.0.0 211.211.1.1
Router(config)#exit
```

R4

```
Router(config)#int e0/1
Router(config-if)#no shutdown
Router(config-if)#ip address 211.211.2.2 255.255.255.0
Router(config-if)#exit
Router(config)#int e0/2
Router(config-if)#no shutdown
Router(config-if)#ip address 10.0.20.1 255.255.255.0
Router(config-if)#exit
Router(config)#ip route 0.0.0.0 0.0.0.0 211.211.2.1
Router(config)#exit

```

R3

```
Router(config)#int e0/1
Router(config-if)#no shutdown
Router(config-if)#ip address 211.211.3.2 255.255.255.0
Router(config-if)#exit
Router(config)#int e0/2
Router(config-if)#no shutdown
Router(config-if)#ip address 10.0.30.1 255.255.255.0
Router(config-if)#exit
Router(config)#ip route 0.0.0.0 0.0.0.0 211.211.3.1
Router(config)#exit

```
