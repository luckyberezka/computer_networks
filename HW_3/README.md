'''

Router(config)#int e0/0.10
Router(config-subif)#ip dhcp pool VLAN10POOL
Router(dhcp-config)#network 10.0.10.0 255.255.255.0
Router(dhcp-config)#default-router 10.0.10.1
Router(dhcp-config)#dns-server 10.0.10.2
Router(dhcp-config)#exit
Router(config)#ip dhcp excluded-address 10.0.10.1 10.0.10.10
Router(config)#int e0/0.20
Router(config-subif)#ip dhcp pool VLAN20POOL
Router(dhcp-config)#network 10.0.20.0 255.255.255.0
Router(dhcp-config)#default-router 10.0.20.1
Router(dhcp-config)#dns-server 10.0.20.2
Router(dhcp-config)#exit
Router(config)#ip dhcp excluded-address 10.0.20.1 10.0.20.10
Router(config)#access-list 100 permit ip 10.0.10.0 0.0.0.255 any
Router(config)#access-list 100 permit ip 10.0.20.0 0.0.0.255 any
Router(config)#$ NATPOOL 11.0.10.10 11.0.10.30 netmask 255.255.255.0
Router(config)#in e0/2
Router(config-if)#no shutdown
Router(config-if)#ip address 11.0.10.1 255.255.255.0
Router(config-if)#ip nat outside
Router(config-if)#exit
Router(config)#int e0/0
Router(config-if)#ip nat inside
Router(config-if)#exit
Router(config)#int e0/0.10
Router(config-subif)#ip nat inside
Router(config-subif)#exit
Router(config)#int e0/0.20
Router(config-subif)#ip nat inside
Router(config-subif)#exit
Router(config)#ip nat inside source list 100 pool NATPOOL
Router(config)#exit

'''
