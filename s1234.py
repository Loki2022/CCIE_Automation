from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter username: ")
password = getpass()

with open('s1234') as f:
    swi = (f.read().splitlines())

with open('s4321') as f:
    send_cmd = (f.read().splitlines())
    
for i in swi:
    print('connecting to ' + i)
    ip_add = i
    ios = {'ip': ip_add, 'username': username, 'password': password, 'device_type': 'cisco_ios'}
    connect = ConnectHandler(**ios)
    output = connect.send_config_set(send_cmd)
    print(output)
    for vlan in range(11,21):
        cmd = {'vlan ' + str(vlan)}
        out = connect.send_config_set(cmd)
        print(out)