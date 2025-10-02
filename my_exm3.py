from netmiko import ConnectHandler
from getpass import getpass

username = input('enter username: ')
password = getpass('enter password')

sw = {'host': input('Enter ip address: '), 'username':username, 'password': password, 'port': 22, 'device_type': 'cisco_ios', }

connect = ConnectHandler(**sw)
for i in range(1,11):
    cmd = ['vlan '+ str(i)]
    output = connect.send_config_set(cmd)
    print(output)

connect.disconnect()