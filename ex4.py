from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = getpass('Enter password: ')

sw4 = {'host': input('enter ip: '), 'username':username, 'password': password, 'device_type': 'cisco_ios','port':'22',}

connect = ConnectHandler(**sw4)
send_cmd = ['int lo0', 'ip add 10.10.10.4 255.255.255.0', 'int vlan 10', 'no shut', 'ip add 10.1.13.4 255.255.255.0','ip ospf 1 area 0',]
output = connect.send_config_set(send_cmd)
print(output)
