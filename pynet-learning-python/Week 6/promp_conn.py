"""

How to handle mutli-line prompts

pynet-rtr1# delete flash:/small_file_bim.txt
Delete flash:/small_file_bim.txt? [confirm] n
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
    }

net_conn = Netmiko(**my_device)
filename = "small_file_bim.txt"
cmd = "delete flash:{}".format(filename)
# print(cmd)

# Solution 1: change the timing with send command
output = net_conn.send_command_timing(cmd)
if 'confirm' in output:
    output += net_conn.send_command_timing("\n")

# Solution 2: change router prompt

# Use delay factor to wait for commands to complete


#Gracefully disconnect ssh session
net_conn.disconnect()

print(output)