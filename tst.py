from netmiko import ConnectHandler
from getpass import getpass

username = input('enter username: ')
password = getpass('enter password: ')

sw = {'ip':input("Enter device ip: "), 'username': username, 'password': password, 'device_type': 'cisco_ios'}

connect = ConnectHandler(**sw)
output = connect.send_command('show vlan brief')
print(output)

connect.disconnect()

csr = {'ip':input("Enter device ip: "), 'username': username, 'password': password, 'device_type': 'cisco_ios'}

connect = ConnectHandler(**csr)
output = connect.send_command('show ip route ospf')
print(output)