from netmiko import ConnectHandler

sw3 = {'ip':'192.168.1.43', 'username':'admin','password':'cisco', 'device_type' :'cisco_ios'}
sw4 = {'ip':'192.168.1.44', 'username':'admin','password':'cisco', 'device_type' :'cisco_ios'}

with open('psec')as f:
    