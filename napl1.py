import json
from napalm import get_network_driver
driver = get_network_driver('ios')
r11=driver('192.168.1.51', 'admin', 'cisco')
r11.open()
ios_output = r11.get_interfaces_ip()
print(json.dumps(ios_output, indent=2))
