from netmiko import ConnectHandler
from getpass import getpass

sw1 = {'ip':'192.168.1.71', 'username':'admin', 'password': 'cisco','device_type':'cisco_ios'}
sw2 = {'ip':'192.168.1.72', 'username':'admin', 'password': 'cisco','device_type':'cisco_ios'}

lst =[sw1,sw2]

for sw in lst:
    print('connecting to '+ sw['ip'])
    connect = ConnectHandler(**sw)
    output = connect.send_command('sh vlan brie')
    print(output)