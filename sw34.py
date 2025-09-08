from netmiko import ConnectHandler
from getpass import getpass

username = input("enter username: ")
password = getpass()

with open('sw34') as f:
    sw34 = (f.read().splitlines())

for i in sw34:
    print('connecting to ' + i)
    ip_add = i
    ios = {"ip": ip_add, "username": username , "password": password, "device_type": "cisco_ios"}
    connnect = ConnectHandler(**ios)
    output = connnect.send_command("sh vlan brief")
    print(output)
    for vlan in range(2,11):
        send_cmd = ['vlan ' + str(vlan)]
        output = connnect.send_config_set(send_cmd)
        print(output)