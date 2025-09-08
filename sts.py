from netmiko import ConnectHandler
from getpass import getpass

sw1 = {'ip': '192.168.1.71', 'username':'admin', 'password': getpass('enter password: '), 'device_type':'cisco_ios'}

lst = [sw1]
connect = ConnectHandler(**sw1)
out = connect.send_command('show vlan brief')
print(out)
