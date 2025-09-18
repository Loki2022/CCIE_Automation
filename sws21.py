from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter username: ")
password = getpass()

with open('switches') as f:
    switches = (f.read().splitlines()) 

for i in switches:
    print('connectin to '+ i)
    ip_add = i
    ios = {'ip':ip_add, 'username':username, 'password':password, 'device_type':'cisco_ios'}
    connect = ConnectHandler(**ios)
    output = connect.send_command('show vlan brief')
    print(output)
    for vlans in range(11,21):
        send = ['vlan '+ str(vlans)]
        out = connect.send_config_set(send)
        print(out)