from netmiko import ConnectHandler
from getpass import getpass

# Prompt for credentials
username = input("Enter username: ")
password = getpass("Enter password: ")

# Define device details
cisco_device = {
    "device_type": "cisco_ios",
    "host": input("Enter device IP: "),
    "username": username,
    "password": password,
    "port": 22,
}

# Connect to device
print("\nConnecting to device...")
net_connect = ConnectHandler(**cisco_device)
print("Connected!")

# Run show command
output = net_connect.send_command("show ip int brief")
print("\n--- Show IP Interface Brief ---")
print(output)

# Send configuration commands
config_commands = [
    "interface loopback0",
    "description Configured_by_Netmiko",
    "ip address 10.10.10.1 255.255.255.0",
]
config_output = net_connect.send_config_set(config_commands)
print("\n--- Configuration Applied ---")
print(config_output)

# Save configuration
net_connect.save_config()

# Disconnect
net_connect.disconnect()
print("Disconnected.")
