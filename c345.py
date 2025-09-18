from netmiko import ConnectHandler

csr3 ={'ip':'192.168.1.43', 'username': 'admin', 'password': 'cisco', 'device_type':'cisco_xe'}
csr4 ={'ip':'192.168.1.44', 'username': 'admin', 'password': 'cisco', 'device_type':'cisco_xe'}
csr5 ={'ip':'192.168.1.45', 'username': 'admin', 'password': 'cisco', 'device_type':'cisco_xe'}

lst1 =[csr3]
with open('csr3') as f:
    c3 = (f.read().splitlines())

for i in lst1:
    connect = ConnectHandler(**i)
    out = connect.send_config_set(c3)
    print(out)

lst2 = [csr4]

with open ('csr4') as f:
    c4 = (f.read().splitlines())

for i in lst2:
    connect = ConnectHandler(**i)
    out = connect.send_config_set(c4)
    print(out)

lst3= [csr5]

with open ('csr5') as f:
    c5 = (f.read().splitlines())

for i in lst3:
    connect = ConnectHandler(**i)
    out = connect.send_config_set(c5)
    print(out)

lst= [csr3,csr4,csr5]

for i in lst:
    print('connecting to '+ str(i['ip']))
    connect = ConnectHandler(**i)
    output = connect.send_command("sh ip ospf neigh")
    print(output)