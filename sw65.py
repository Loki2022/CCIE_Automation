from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter username  ' )
password = getpass()

with open('psec')  as f:
    send_cmd = (f.read().splitlines())

with open('switches')  as f:
    switch_list= (f.read().splitlines())

for sw in switch_list:
    print('connecting to device ' + sw)
    ip_add = sw
    ios_devices = {'ip': ip_add, 'username': username, 'password': password, 'device_type':'cisco_ios'}
    net_connect = ConnectHandler(**ios_devices)
    output = net_connect.send_config_set(send_cmd)
    print(output)