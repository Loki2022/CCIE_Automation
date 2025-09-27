from netmiko import ConnectHandler
from getpass import getpass

username = input('enter username: ')
password = input("enter password: ")

vios1 = {'host': input('enter ip address: '), 'username': username, 'password': password, 'device_type': 'cisco_ios', 'port': '22'}

connect = ConnectHandler(**vios1)
send_cmd = ['int lo0', 'ip address 1.1.1.1 255.255.255.255' ,'ip ospf 1 area 0']
output = connect.send_config_set(send_cmd)
print(output)
send = ['int g0/0', 'ip address 10.1.12.1 255.255.255.0' ,'ip ospf 1 area 0', 'ip ospf network point-to-point','no shut', 'do wr']
out = connect.send_config_set(send)
print(out)