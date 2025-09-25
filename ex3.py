from netmiko import ConnectHandler
from getpass import getpass

username = input('enter username: ')
password = getpass('enter password')

sw3 = {
    "host": input("Enter device IP: "),
    "username": username,
    "password": password,
    "port": 22,
    "device_type": "cisco_ios",
}
net_connect = ConnectHandler(**sw3)
send_cmd = ['int lo0', 'ip add 10.10.10.3 255.255.255.0', 'int vlan 10', 'no shut', 'ip add 10.1.13.3 255.255.255.0','ip ospf 1 area 0',]
output = net_connect.send_config_set(send_cmd)
print(output)