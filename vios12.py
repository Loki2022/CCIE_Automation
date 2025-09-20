from netmiko import ConnectHandler
from getpass import getpass

vios1 = {'ip':'192.168.1.41', 'username': 'admin','password': getpass(), 'device_type':'cisco_ios'}

with open('config') as f:
    send = (f.read().splitlines())

lst1 =[vios1]

for i in lst1 :
    print('connecting to '+ str(i['ip']))
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send)
    print(output)
    
vios2 = {'ip':'192.168.1.42', 'username': 'admin','password': getpass(), 'device_type':'cisco_ios'}

with open('config1') as f:
    send = (f.read().splitlines())

lst2 =[vios2]

for i in lst2 :
    print('connecting to '+ str(i['ip']))
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send)
    print(output)