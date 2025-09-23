from netmiko import ConnectHandler

sw5 = {'ip':'192.168.1.55', 'username': 'admin', 'password': 'cisco', 'device_type': 'cisco_ios'}
sw6 = {'ip':'192.168.1.56', 'username': 'admin', 'password': 'cisco', 'device_type': 'cisco_ios'}

lst = [sw5,sw6]

with open('psec') as f:
    cmd = (f.read().splitlines())

for i in lst:
    print('connecting to ' + str(i['ip']))
    connect = ConnectHandler(**i)
    output = connect.send_config_set(cmd)
    print(output)