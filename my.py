from netmiko import ConnectHandler
from getpass import getpass

username = input('enter username: ')
password = getpass('Enter passwrod: ')

sw = {'host': input('enter ip address: '), 'username': username, 'password': password, 'device_type': 'cisco_ios', 'port': '22'}

connect = ConnectHandler(**sw)
send_cmd = ['int lo1', 'ip add 1.1.1.1 255.255.255.255']
output = connect.send_config_set(send_cmd)
print(output)
out =connect.send_command('show ip int brief')
print(out)
connect.disconnect