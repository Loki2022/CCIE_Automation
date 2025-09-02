from netmiko import ConnectHandler

with open('config') as f:
    send_cmd = (f.read().splitlines())

with open('device_list') as f:
    devices = (f.read().splitlines())

for device in devices:
    print('connecting to device ' + device) 
    ip_add = device
    
ios_device = {'device_type':'cisco_ios','ip': ip_add , 'username': 'admin','password': 'cisco'}

net_connect = ConnectHandler (**ios_device)
output = net_connect.send_config_set(send_cmd)
print(output)
