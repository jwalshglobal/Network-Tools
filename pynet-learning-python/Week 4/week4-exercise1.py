"""
1. Create a dictionary representing a network device. The dictionary should have key-value pairs representing the
'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then set the
'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as',
 and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
"""

from __future__ import unicode_literals, print_function
from pprint import pprint
import os

#Cisco Device
network_device = {'ip_addr': '192.168.1.1', 'vendor': 'cisco', 'username': 'admin', 'password': 'admin123'}
#Juniper Device
network_device = {'ip_addr': '192.168.1.1', 'vendor': 'juniper', 'username': 'admin', 'password': 'admin123'}

#Print out the 'ip_addr' key from the dictionary.
for key, value in network_device.items():
    if key == 'ip_addr':
        print(value)

print()
print('*'*40)
print()

ios_platform = {'platform': 'ios'}
junos_platform = {'platform': 'juniper'}

if network_device['vendor'].lower() == 'cisco':
    network_device.update(ios_platform)
    #network_device['platform'].lower() == 'ios'
elif network_device['vendor'].lower() == 'juniper':
    #network_device['platform'].lower() == 'junos'
    network_device.update(junos_platform)
print(network_device)

print()
print('*'*40)
print()

#Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.
bgp_fields = {
    'bgp_as': '60005',
    'peer_as': '60010',
    'peer_ip': '10.10.10.1'
}
network_device.update(bgp_fields)
print(network_device)

print()
print('*'*40)
print()

#Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.
for key, value in network_device.items():
    print("key: "+ key)

print()
print('*'*40)
print()

#Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
for key, value in network_device.items():
    print(key + " " + value)