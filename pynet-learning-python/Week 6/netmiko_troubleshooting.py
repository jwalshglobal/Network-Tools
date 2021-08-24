#
# Turn on Logging
# https://github.com/ktbyers/netmiko/blob/develop/COMMON_ISSUES.md
#

from netmiko import Netmiko
from getpass import getpass

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')

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