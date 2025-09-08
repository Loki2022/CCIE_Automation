from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter Name: ")
password = getpass()

with open('vios') as f:
    router = (f.read().splitlines())
    
for i in router:
    print('connecting to '+ i)
    ip_add = i
    ios = {'ip':ip_add,'username': username, 'password': password, 'device_type': 'cisco_ios'}
    connect= ConnectHandler(**ios)
    output = connect.send_command("show ip bgp summary")
    print(output)