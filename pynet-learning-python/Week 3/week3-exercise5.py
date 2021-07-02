"""
*** Note, to actually test this in your environment, change the test IP addresses to something in your environment that
 you can ping successfully. ***

Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or '10.10.100.'.

You should use the 'range' builtin to accomplish this.

Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.

Use Python's 'enumerate' to print out all of the IP addresses and their corresponding list index. The output should
 look similar to the following:
0 ---> 10.10.100.1
1 ---> 10.10.100.2
2 ---> 10.10.100.3
3 ---> 10.10.100.4
4 ---> 10.10.100.5
...

Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.

Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this short list. For Windows
 the command will probably be os.system("ping -n 3 10.10.100.3").

Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be similar to the
following:
WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
"""

from __future__ import unicode_literals, print_function
from pprint import pprint
import os

# Toggle this to use Windows
WINDOWS = False

base_cmd_linux = "ping -c 4 -W 100"
base_cmd_windows = "ping -n 2"
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = []
base_ip = "10.30.0."
octet_range = range(0,255)
print(type(octet_range))

for last_octet in octet_range:
    new_ip = base_ip + str(last_octet)
    #print(new_ip)
    ip_list.append(new_ip)

print(ip_list)

print()
print("-" * 40)
print()

for i, ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(i, ip_addr))

print()
print("-" * 40)
print()

#ip_list = ip_list[2:6]

print()
print("-" * 80)
for ip_addr in ip_list:
    print("IP Addr: ", ip_addr)
    return_code = os.system("{} {}".format(base_cmd, ip_addr))
    print("-" * 80)
print("-" * 80)
print()
