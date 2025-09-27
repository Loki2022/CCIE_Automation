from netmiko import ConnectHandler
from getpass import getpass

sw3 = {'ip':'192.168.1.33', 'username': 'admin','password': 'cisco', 'device_type':'cisco_ios'}
sw4 = {'ip':'192.168.1.34', 'username': 'admin','password': 'cisco', 'device_type':'cisco_ios'}
lst= [sw3,sw4]

with open('s43')as f:
    send = (f.read().splitlines())

for i in lst:
    print('connect to '+ i['ip'])
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send)
    print(output)
    for vlan in range(1,11):
        cmd = ['vlan ' + str(vlan)] 
        out = connect.send_config_set(cmd)
        print(out)
    output = connect.send_command('show vlan brie')
    print(output)
    

