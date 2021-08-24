from netmiko import Netmiko
from getpass import getpass

#use same password for config and enable mode
password = getpass()

my_device = {
    'host': '10.8.20.100',
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios'
    # Use invalid device type to see all supported devices
    # 'device_type': 'foo'
    }

net_conn = Netmiko(**my_device)

output = net_conn.send_config_from_file("change_file.txt")

print()
print('-'*80)
print(output)
print('-'*80)
print()