from netmiko import ConnectHandler
from getpass import getpass

r1 = {'ip':'192.168.1.61','username':'admin', 'password':'cisco', 'device_type':'cisco_ios'}
r2 = {'ip':'192.168.1.62','username':'admin', 'password':'cisco', 'device_type':'cisco_ios'}
r3 = {'ip':'192.168.1.63','username':'admin', 'password':'cisco', 'device_type':'cisco_ios'}
r4 = {'ip':'192.168.1.64','username':'admin', 'password':'cisco', 'device_type':'cisco_ios'}

lst1 = [r1]
with open('bgp1') as f:
    send = (f.read().splitlines())

for i in lst1:
    print('connecting to vios1')
    connect = ConnectHandler(**i)
    out = connect.send_config_set(send)
    print(out)

lst2 = [r2]

with open('bgp2') as f:
    send = (f.read().splitlines())
for i in lst2:
    print('connecting to vios2')
    connect = ConnectHandler(**i)
    out = connect. send_config_set(send)
    print(out)

lst3 = [r3]
with open('bgp3') as f:
    send = (f.read().splitlines())
for i in lst3:
    print('connecting to vios3')
    connect = ConnectHandler(**i)
    out = connect. send_config_set(send)
    print(out)

lst4 = [r4]
with open('bgp4') as f:
    send = (f.read().splitlines())
for i in lst4:
    print('connecting to vios4')
    connect = ConnectHandler(**i)
    out = connect. send_config_set(send)
    print(out)

lst = [r1,r2,r3,r4]

for i in lst:
    connect = ConnectHandler(**i)
    output = connect.send_command('show ip bgp summary')
    print(output)
