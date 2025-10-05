from netmiko import ConnectHandler
from getpass import getpass

username = input('enter username')
password = getpass()

csr1 = {'ip':'192.168.1.61', 'username': username, 'password': password, 'device_type': 'cisco_ios' }
csr2 = {'ip':'192.168.1.62', 'username': username, 'password': password, 'device_type': 'cisco_ios' }

lst1 = [csr1]
with open('csr1') as f:
    send_cmd = (f.read().splitlines())

for c1 in lst1:
    print('connecting to ' + c1['ip'])
    connect = ConnectHandler(**c1)
    output = connect.send_config_set(send_cmd)
    print(output)

lst2 = [csr2]
with open('csr2')as f:
    send_cmd = (f.read().splitlines())
for c2 in lst2:
    print('connecting to ' + c2['ip'])
    connect = ConnectHandler(**c2)
    output = connect.send_config_set(send_cmd)
    print(output)