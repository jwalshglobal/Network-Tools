"""

https://github.com/ktbyers/netmiko



"""

# ConnectionHandler

from netmiko import Netmiko
from getpass import getpass

my_device = {
    'host': '10.8.20.100',
    'username': 'admin',
    'password': '123',
    'device_type': 'hp_procurve'
    }

net_conn = Netmiko(**my_device)

print(net_conn.find_prompt())