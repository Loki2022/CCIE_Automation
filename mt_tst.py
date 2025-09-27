from netmiko import ConnectHandler, NetMikoTimeoutException ,NetMikoAuthenticationException
from getpass import getpass

username = input('Enter username: ')
password = getpass("Enter password: ")

sw = {"host": input("device ip : "), "username": username , "password": password, "device_type":"cisco_ios"}

print('connecting to '+input('device ip '))
net_connect = ConnectHandler(**sw)
send_cmd = ['vlan 100', 'int vlan 100', 'no shut','ip add 10.1.12.2 255.255.255.0', 'do wr']
output = net_connect.send_config_set(send_cmd)
print(output)
