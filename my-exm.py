from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = getpass('Enter password: ')

ios1 = {'ip':'192.168.1.81', 'username':username, 'password': password, 'device_type': 'cisco_ios'}
ios2 = {'ip':'192.168.1.82', 'username':username, 'password': password, 'device_type': 'cisco_ios'}

lst = [ios1]

with open('vios1') as f:
    send_cmd = (f.read().splitlines())

for i in lst:
    print('connecting to ' + i['ip'])
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send_cmd)
    print(output)
    out = connect.send_command('show ip ospf neigh')
    print(out)

lst = [ios2]

with open ('vios2') as f:
    send_cmd = (f.read().splitlines())

for i in lst :
    print('connecting to ' + i['ip'])
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send_cmd)
    print(output)
    out = connect.send_command('show ip ospf neigh')
    print(out)