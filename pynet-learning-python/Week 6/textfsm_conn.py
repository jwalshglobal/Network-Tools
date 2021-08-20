"""
TextFSM Templates for network devices
Parse outputs to put into structured data

https://github.com/networktocode/ntc-templates

pip install ntc_templates
Installed ntc-templates to home directory (install into pycharm)
Or git clone https://https://github.com/networktocode/ntc-templates
"""

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
output = net_conn.send_command("show arp", use_textfsm=True)
print(output)

output = net_conn.send_command("show interfaces")
print(output)