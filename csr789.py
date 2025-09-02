from netmiko import ConnectHandler

csr7 = {'ip':'192.168.1.67', 'username': 'admin', 'password':'cisco', 'device_type':'cisco_ios'}
csr8 = {'ip':'192.168.1.68', 'username': 'admin', 'password':'cisco', 'device_type':'cisco_ios'}
csr9 = {'ip':'192.168.1.69', 'username': 'admin', 'password':'cisco', 'device_type':'cisco_ios'}

lst1 = [csr7]
with open('csr7') as f:
    send = (f.read().splitlines())

for i in lst1:
    print('connecting to CSR7')
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send)
    print(output)

lst2 = [csr8]
with open('csr8') as f:
    send = (f.read().splitlines())

for i in lst2:
    print('connecting to CSR-8')
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send)
    print(output)
    
lst3 = [csr9]
with open('csr9') as f:
    send = (f.read().splitlines())

for i in lst3:
    print('connecting to CSR-9')
    connect = ConnectHandler(**i)
    output = connect.send_config_set(send)
    print(output)