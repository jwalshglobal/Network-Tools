"""

Wait for commands to complete by adding delay factor

Global option or used with send command

"""

# ConnectionHandler
from netmiko import Netmiko
from getpass import getpass

password = getpass()

my_device = {
    'host': '10.8.20.100',
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios'
    # Global delay factor
    'global_delay': 2
    }

net_conn = Netmiko(**my_device)

# Double the delay factor
output = net_conn.send_command("copy run start", delay_factor=2)

# Use delay factor to wait for commands to complete


#Gracefully disconnect ssh session
net_conn.disconnect()

