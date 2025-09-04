from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter username: ")
password = getpass()

with open('config1') as f:
    send_cmd = (f.read().splitlines())

with open('routers') as f :
    router = (f.read().splitlines())

for i in router:
    print('connecting to csr ' + i)
    ip_add = i
    ios_devices = {'ip': ip_add, 'username' : username, 'password': password, 'device_type': 'cisco_ios' }
    connect = ConnectHandler(**ios_devices)
    output = connect. send_config_set(send_cmd)
    print(output)
    