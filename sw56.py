from netmiko import ConnectHandler

sw5 = {'ip':'192.168.1.61', 'username': 'admin', 'password':'cisco', 'device_type':'cisco_ios'}
sw6 = {'ip':'192.168.1.62', 'username': 'admin', 'password':'cisco', 'device_type':'cisco_ios'}
lst = [sw5,sw6]
with open('psec')  as f:
    send_cmd = (f.read().splitlines())

for i in lst:
    print('connecting to '+ i['ip'])
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send_cmd)
    print(output)