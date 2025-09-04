from netmiko import ConnectHandler

vios1={'ip': '192.168.1.61', 'username':'admin', 'password':'cisco', 'device_type': 'cisco_ios'}
vios2={'ip': '192.168.1.62', 'username':'admin', 'password':'cisco', 'device_type': 'cisco_ios'}
vios3={'ip': '192.168.1.63', 'username':'admin', 'password':'cisco', 'device_type': 'cisco_ios'}
vios4={'ip': '192.168.1.64', 'username':'admin', 'password':'cisco', 'device_type': 'cisco_ios'}

# lst1 = [vios1]
# with open('vios1') as f:
#     send = (f.read().splitlines())
# for i in lst1:
#     print('connecting to vios1')
#     connect = ConnectHandler(**i)
#     output = connect.send_config_set(send)
#     print(output)

# lst2 = [vios2]
# with open('vios2') as f:
#     send = (f.read().splitlines())
# for i in lst2:
#     print('connecting to vios2')
#     connect = ConnectHandler(**i)
#     output = connect.send_config_set(send)
#     print(output)

# lst3 =[vios3]
# with open('vios3') as f:
#     send = (f.read().splitlines())
# for i in lst3:
#     print('connecting to vios3')
#     connect = ConnectHandler(**i)
#     output = connect.send_config_set(send)
#     print(output)
    
# lst4 =[vios4]
# with open('vios4') as f:
#     send = (f.read().splitlines())
# for i in lst4:
#     print('connecting to vios4')
#     connect = ConnectHandler(**i)
#     output = connect.send_config_set(send)
#     print(output)

lst =[vios1, vios2,vios3,vios4]
for vios in lst:
    print('connecting to ' + vios['ip'] )
    connect = ConnectHandler(**vios)
    print('connecting to ')
    output = connect.send_command('show ip route ospf')
    print(output)    
  