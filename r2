int g0/0
ip add 10.1.12.2 255.255.255.0
ip ospf 1 area 0
ip ospf network point-to-point
no shut
int lo0
ip add 2.2.2.2 255.255.255.255
ip ospf 1 area 0