from netmiko import ConnectHandler

sw3 = {'ip':'192.168.1.43', 'username':'admin','password':'cisco', 'device_type' :'cisco_ios'}
sw4 = {'ip':'192.168.1.44', 'username':'admin','password':'cisco', 'device_type' :'cisco_ios'}

lst = [sw3,sw4]

with open('psec')as f:
    send_cmd = (f.read().splitlines())

for i in lst:
    print('connecting to '+ str(i['ip']))
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send_cmd)
    print(output)
    for vlan in range (2,15):
        cmd = ['vlan ' + str(vlan)]
        out = connect.send_config_set(cmd)
        print(out)
        