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
Router(config-if)#ex


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
Router(config)#ip route 10.0.20.2 255.255.255.255 10.100.10.2
Router(config)#ip route 10.0.30.2 255.255.255.255 10.200.10.2
Router(config)#int tunnel 0
Router(config-if)#
*Dec 13 19:08:56.083: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel0, changed state to down
Router(config-if)#no shutdown
Router(config-if)#ip address 10.100.10.1 255.255.255.252
Router(config-if)#tunnel source 211.211.1.2
Router(config-if)#tunnel destination 211.211.2.2
Router(config-if)#ip
*Dec 13 19:11:02.769: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel0, changed state to upm
Router(config-if)#ip mtu 1400
Router(config-if)#ip tcp adjust-mss 1360
Router(config-if)#exit
Router(config)#int tunnel 1
Router(config-if)#no sh
*Dec 13 19:12:03.186: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel1, changed state to down
Router(config-if)#no shutdown
Router(config-if)#ip address 10.200.10.1 255.255.255.252
Router(config-if)#tunnel source 211.211.1.2
Router(config-if)#tunnel destination 211.211.3.2
Router(config-if)#
*Dec 13 19:13:32.881: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel1, changed state to up
Router(config-if)#ip mtu 1400
Router(config-if)#ip tcp adjust-mss 1360
Router(config-if)#exit
Router(config)#crypto isakmp policy 1
Router(config-isakmp)#ecryption aes
                       ^
% Invalid input detected at '^' marker.

Router(config-isakmp)#encryption aes
Router(config-isakmp)#authentication pre-shark
                                             ^
% Invalid input detected at '^' marker.

Router(config-isakmp)#authentication pre-share
Router(config-isakmp)#group 2
Router(config-isakmp)#hash sha
Router(config-isakmp)#exit
Router(config)#crypto isakmp key annjjjik address 211.211.3.2
Router(config)#crypto ipsec transform-set IPSEC-SET esp-aes 256 esp-sha-hmac
Router(cfg-crypto-trans)#mode transport
Router(cfg-crypto-trans)#exit
Router(config)#crypto map FIRSTMAP 10 ipsec-isakmp
% NOTE: This new crypto map will remain disabled until a peer
        and a valid access list have been configured.
Router(config-crypto-map)#set peer 211.211.3.2
Router(config-crypto-map)#ser transform-set IPSEC-SET
                            ^
% Invalid input detected at '^' marker.

Router(config-crypto-map)#set transform-set IPSEC-SET
Router(config-crypto-map)#match address 101
Router(config-crypto-map)#exit
Router(config)#access-list 101 permit gre host 211.211.1.2 host 211.211.3.2
Router(config)#int e0/2
Router(config-if)#crypto map FIRSTMAP
Router(config-if)#ex
*Dec 13 19:39:47.144: %CRYPTO-6-ISAKMP_ON_OFF: ISAKMP is ON
Router(config-if)#exit
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
Router(config)#ip route 10.0.10.2 255.255.255.255 10.100.10.1
Router(config)#int tunnel 0
Router(config-if)#
*Dec 13 19:16:17.383: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel0, changed state to down
Router(config-if)#no shutdown
Router(config-if)#ip address 10.100.10.2 255.255.255.252
Router(config-if)#tunnel source 211.211.2.2
Router(config-if)#tunnel destination 211.211.1.2
Router(config-if)#
*Dec 13 19:18:05.323: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel0, changed state to up
Router(config-if)#ip mtu 1400
Router(config-if)#ip tcp adjust-mss 1360
Router(config-if)#exit
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
Router(config)#ip route 10.0.10.2 255.255.255.255 10.200.10.1
Router(config)#int tunnel 1
Router(config-if)#
*Dec 13 19:21:07.742: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel1, changed state to down
Router(config-if)#no shutdown
Router(config-if)#ip address 10.200.10.2 255.255.255.252
Router(config-if)#tunnel source 211.211.3.2
Router(config-if)#tunnel destination 211.211.1.2
Router(config-if)#
*Dec 13 19:22:29.065: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel1, changed state to up
Router(config-if)#ip mtu 1400
Router(config-if)#ip tcp adjust-mss 1360
Router(config-if)#exit
Router(config)#wr
                ^
% Invalid input detected at '^' marker.

Router(config)#exit


```
