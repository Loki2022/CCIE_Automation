from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = input('Enter password: ')

sw ={'ip':input('enter ip: '), 'username': username, 'password': password, 'device_type': 'cisco_ios'}

connect = ConnectHandler(**sw)
for i in range(1,11):
    print('connecting to '+ str(sw['ip']))
    cmd = ['vlan '+ str(i)]
    out = connect.send_config_set(cmd)
    print(out)
    send_cmd = ['int g0/0', 'switchport trunk encap dot1', 'switchport mode trunk','switchport nonegotiate']
    out = connect.send_config_set(send_cmd)
    print(out)


output = connect.send_command('sh vlan brief')
print(output)