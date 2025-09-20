from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = getpass()

with open('sw21') as f:
    switches = (f.read().splitlines())

for sw in switches:
    ip_add = sw
    print('connecting to '+ str(sw))
    ios = {"ip":ip_add, "username":username, "password": password, "device_type" : "cisco_ios"}
    connect = ConnectHandler(**ios)
    output = connect.send_command('sh vlan brie')
    print(output)
    