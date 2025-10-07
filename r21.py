from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter username: ")
password = getpass("Enter password: ")

r12 = {"ip":input("enter ip: "), "username":username, "password": password, "device_type":"cisco_ios", "port":"22",}

connect = ConnectHandler(**r12)
output = connect.send_command('sh ip ospf neigh')
print(output)