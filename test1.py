from getpass import getpass
from netmiko import ConnectHandler

username = input("enter username: ")
password = getpass()

with open('vios') as f:
    routers = (f.read().splitlines())

for vios in routers:
    print('connecting to '+ vios)
    ip_add= vios
    ios = {'ip':ip_add,'username': username, 'password': password, 'device_type': 'cisco_ios'}
    connect= ConnectHandler(**ios)
    out = connect.send_command('show ip ospf neigh')
    print(out)
  