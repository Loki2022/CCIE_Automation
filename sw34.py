from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = getpass('Enter password: ')

sw = {'ip': input('enter ip address: '), 'username': username , 'password': password, 'device_type': 'cisco_ios'}

connect = ConnectHandler(**sw)
send_cmd = ['int g0/0', 'switchport trunk encap dot1q','switchport mode trunk','no shut']
output = connect.send_config_set(send_cmd)
print(output)

for i in range(2,11):
    send = ['vlan '+ str(i)]
    output = connect.send_config_set(send)
    print(output)

int = ['int g0/1', 'switchport mode access', 'switchport access vlan 10','no shut']
output = connect.send_config_set(int)
print(output)