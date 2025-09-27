from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = input('Enter password: ')

vios ={'host': input('Enter ip: '), 'username': username, 'password': password, 'device_type':'cisco_ios', 'port':'22'}

net_connect = ConnectHandler(**vios)
print('connecting to '+ vios['host'])
output = net_connect.send_command('show ip ospf neigh')
print(output)