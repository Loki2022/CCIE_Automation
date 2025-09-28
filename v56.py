from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = getpass ("Enter password: ")

vios5 = {'ip': '192.168.1.35', 'username': username, 'password': password, 'device_type':'cisco_ios'}
vios6 = {'ip': '192.168.1.36', 'username': username, 'password': password, 'device_type':'cisco_ios'}

lst = [vios5]

with open('v5') as f :
    send = (f.read().splitlines())

for vios in lst:
    print('connecting to ' + vios['ip'])
    connect = ConnectHandler(**vios)
    output = connect.send_config_set(send)
    print(output)

lst1 = [vios6]

with open('v6') as f :
    send = (f.read().splitlines())

for vios in lst1:
    print('connecting to ' + vios['ip'])
    connect = ConnectHandler(**vios)
    output = connect.send_config_set(send)
    print(output)