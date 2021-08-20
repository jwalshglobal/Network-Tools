"""

https://github.com/ktbyers/netmiko

# To see all supported devices, use 'device_type': 'foo'
# Get past enable --

"""

# ConnectionHandler
from netmiko import Netmiko
from getpass import getpass

#use same password for config and enable mode
password = getpass()

my_device = {
    'host': '10.8.20.100',
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'hp_procurve'
    # Use invalid device type to see all supported devices
    # 'device_type': 'foo'
    }

net_conn = Netmiko(**my_device)
output = net_conn.send_command("show arp")
print(output)

output = net_conn.send_command("show interfaces")
print(output)

#Gracefully close ssh connection
net_conn.disconnect()

# fix issue with router prompt that sometimes does not work
# output = net_conn.send_command("show interfaces", expect_string=r'#')

# show config prompt
# net_conn.send_command_timing("disable")
# print(net_conn.find_prompt())

# get to enable prompt
# net_conn.enable()
# print(net_conn.find_prompt())

# Multi-line commands (i.e. confirm you want to delete a file)
