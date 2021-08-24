from netmiko import Netmiko
from getpass import getpass

#use same password for config and enable mode
password = getpass()

my_device = {
    'host': '10.8.20.100',
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'juniper_junos'
    # Use invalid device type to see all supported devices
    # 'device_type': 'foo'
    }

net_conn = Netmiko(**my_device)

output = net_conn.send_command("show run | inc logging")
print(output)

cfg_commands = ['set system syslog archive size 120k files 3']
output = net_conn.send_config_set(cfg_commands)
print(output)

output = net_conn.commit()
print(output)

output = net_conn.exit_config_mode()
output = net_conn.send_command("show configuration")

# Cisco Devices
# cfg_commands = ['logging bufered 10000', 'no logging console']
# output = net_conn.send_command(cfg_commands)
# copy running config to start
# save_command()

print()
print('-'*80)
print(output)
print('-'*80)
print()