from netmiko import ConnectHandler
from getpass import getpass

username = ('Enter username: ')
password = getpass()

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.52",   
    "username": username,
    "password": password,
 }
connect = ConnectHandler(**device)
connect.enable()
for i in range(11,20):
    cmd = ['vlan '+ str(i)]
    out = connect.send_config_set(cmd)
    print(out)