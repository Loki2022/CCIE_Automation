from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter Username: ')
password = getpass("Enter Password: ")

with open('s1234') as f:
    sw = (f.read().splitlines())

with open('sec') as f:
    cmd = (f.read().splitlines())

for i in sw:
    print('connecting to ' + i)
    ip_add = i
    ios = {'ip':ip_add, 'username':username, 'password': password, 'device_type': 'cisco_ios'}
    connect = ConnectHandler(**ios)
    send_command = ['vlan 2-10']
    output = connect.send_config_set(cmd)
    print(output)
    output = connect.send_config_set(send_command)
    print(output)