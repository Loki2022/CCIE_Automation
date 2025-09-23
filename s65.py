from netmiko import ConnectHandler
from getpass import getpass

username = input('enter username: ')
password = getpass()

with open ('s65') as f:
    sw = (f.read().splitlines())

for i in sw:
    print('connecting to '+ i)
    ip_add = i
    ios = {'ip':ip_add, 'username': username, 'password': password, 'device_type':'cisco_ios'}
    connect = ConnectHandler(**ios)
    for j in range(11,21):
        send = ['vlan ' + str(j)]
        output = connect.send_config_set(send)
        print(output)