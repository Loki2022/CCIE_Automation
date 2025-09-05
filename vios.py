from netmiko import ConnectHandler
from getpass import getpass

username = input("enter username: ")
password = getpass()

with open('config') as f:
    send_cmd = (f.read().splitlines())

with open('vios') as f:
    routers = (f.read().splitlines())
    
for vios in routers:
    print('connecting to '+ vios)
    ip_add= vios
    ios = {'ip':ip_add,'username': username, 'password': password, 'device_type': 'cisco_ios'}
    connect= ConnectHandler(**ios)
    out = connect.send_config_set(send_cmd)
    print(out)