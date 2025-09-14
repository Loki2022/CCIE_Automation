from netmiko import ConnectHandler
from getpass import getpass

username = input("enter username: ")
password = getpass()

with open('sw12') as f:
    send_cmd = (f.read().splitlines())

with open('sw21') as f:
    switches = (f.read().splitlines())

for sw in switches:
    print('connecting to '+ str(sw))
    ip_add = sw
    ios = {"ip":ip_add, "username":username, "password": password, "device_type" : "cisco_ios"}
    connect = ConnectHandler(**ios)
    output = connect.send_config_set(send_cmd)
    print(output)
    for vlans in range(2,11):
        send = ['vlan '+ str(vlans)]
        output = connect.send_config_set(send)
        print(output)
        