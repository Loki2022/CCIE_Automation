from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter username: ")
password = getpass()

with open('csr987') as f:
    send_cmd = (f.read().splitlines())
    
with open('csr789') as f:
    csr = (f.read().splitlines())

for i in csr:
    print('connecting to csr' + i)
    ip_add = i
    csr_devices = {'ip': ip_add, 'username': username, 'password': password, 'device_type':'cisco_ios'}
    connect = ConnectHandler(**csr_devices)
    out = connect.send_config_set(send_cmd)
    print(out)



