from getpass import getpass
from netmiko import ConnectHandler

username = input("Enter username: ")
password = getpass()

with open('switches') as f:
    switch = (f.read().splitlines())

for i in switch:
    print('connecting to sw')
    ip_add = i
    ios = {'ip': ip_add, 'username' : username, 'password':password, 'device_type':'cisco_ios' }
    connect = ConnectHandler(**ios)
    output = connect.send_command('show vlan brie')
    print(output)
    for x in range(2,11):
        send = ['vlan ' + str(x)]
        output = connect.send_config_set(send)
        print(output)
      