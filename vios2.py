from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = input('Enter password: ')

with open('vios2') as f:
    send_cmd = (f.read().splitlines())

vios2 = {'host': input ('enter ip address: '), 'username': username, 'password': password, 'device_type': 'cisco_ios', 'port':'22' }

net = ConnectHandler(**vios2)
output = net.send_config_set(send_cmd)
print(output)