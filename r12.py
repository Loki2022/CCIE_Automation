from netmiko import ConnectHandler
from getpass import getpass

r1 ={'ip':'192.168.1.51', 'username': 'admin','password': 'cisco', 'device_type':'cisco_ios'}
r2 ={'ip':'192.168.1.52', 'username': 'admin','password': 'cisco', 'device_type':'cisco_ios'}

lst1 = [r1]
with open('r1') as f:
    send_cmd = (f.read().splitlines())
for i in lst1:
    print('connecting to ' + str(i['ip']))
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send_cmd)
    print(output)
lst2 = [r2]
with open('r2') as f:
    send_cmd = (f.read().splitlines())
for i in lst2:
    print('connecting to ' + str(i['ip']))
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send_cmd)
    print(output)