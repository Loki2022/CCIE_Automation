from netmiko import ConnectHandler
from getpass import getpass

username = input('enter username: ')
password = getpass('enter password')

sw = {
    "host": input("Enter device IP: "),
    "username": username,
    "password": password,
    "port": 22,
    "device_type": "cisco_ios",
}
net_connect = ConnectHandler(**sw)
output = net_connect.send_command('show vlan brief')
print(output)

