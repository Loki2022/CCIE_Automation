from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter username: ")
password = getpass()

with open('ips') as f:
    routers = (f.read().splitlines())

for i in routers:
    print('connecting to  ' + i)
    ip_add = i
    ios_devices = {'ip': ip_add, 'username' : username, 'password': password, 'device_type': 'cisco_ios' }
    connect = ConnectHandler(**ios_devices)
    output = connect. send_command('show ip int brie')
    print(output)