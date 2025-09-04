from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter username: ")
password = getpass()

# with open('sw_cmd') as f:
#     send_cmd = (f.read().splitlines())

with open('sw_list') as f:
    switch = (f.read().splitlines())

for i in switch:
    print('connecting to '+ i)
    ip_add = i
    ios_devices = {'ip': ip_add, 'username': username, 'password': password, 'device_type':'cisco_ios'}
    connect = ConnectHandler(**ios_devices)
    for vlan in range(1,20):
        config = ['vlan '+ str(vlan)]
        out = connect.send_config_set(config)
        print(out)