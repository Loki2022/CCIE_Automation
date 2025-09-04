from netmiko import ConnectHandler

vios1={'ip': '192.168.1.61', 'username':'admin', 'password':'cisco', 'device_type': 'cisco_ios'}
vios2={'ip': '192.168.1.62', 'username':'admin', 'password':'cisco', 'device_type': 'cisco_ios'}
vios3={'ip': '192.168.1.63', 'username':'admin', 'password':'cisco', 'device_type': 'cisco_ios'}
vios4={'ip': '192.168.1.64', 'username':'admin', 'password':'cisco', 'device_type': 'cisco_ios'}

lst =[vios1, vios2,vios3,vios4]
for vios in lst:
  connect = ConnectHandler(**vios)
  print('connecting to ')
  output = connect.send_command('show ip ospf neigh')
  print(output)    
  
  
  