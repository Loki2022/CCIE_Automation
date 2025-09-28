from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username: ')
password = getpass ("Enter password: ")

vios = {'ip': input('enter ip : '),'username': username, 'password':password, 'device_type': 'cisco_ios', 'port':'22'}

connect = ConnectHandler(**vios)
output = connect.send_command('ping 6.6.6.6 ')
print(output)