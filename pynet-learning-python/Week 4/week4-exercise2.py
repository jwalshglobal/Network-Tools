"""
2. Create three separate lists of IP addresses. The first list should be the IP addresses of the Houston data center
routers, and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers, and it should have at least eight RFC1918
 IP addresses (including some addresses that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers, and it should have at least eight RFC1918
IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.

"""

from __future__ import unicode_literals, print_function
from pprint import pprint
import os

# Create List of Houston Routers
houston_dup_routers =[]
houston_routers = []
base_ip = "10."
octet_range = range(0,10)
end_ip = ".20.5"
duplicate_ip = ['10.9.20.5']
print(type(octet_range))

for last_octet in octet_range:
    new_ip = base_ip + str(last_octet) + end_ip
    #print(new_ip)
    houston_routers.append(new_ip)

houston_dup_routers = houston_routers + duplicate_ip
print(houston_dup_routers)

# Create List of Atlanta Routers
atl_dup_routers =[]
atl_routers = []
base_ip = "10.0."
octet_range = range(0,8)
end_ip = ".5"
duplicate_ip = ['10.9.20.5']
print(type(octet_range))

for last_octet in octet_range:
    new_ip = base_ip + str(last_octet) + end_ip
    print(new_ip)
    atl_routers.append(new_ip)

atl_dup_routers = atl_routers + duplicate_ip
print(atl_dup_routers)

# Create Chicago DC Routers
chi_dup_routers =[]
chi_routers = []
base_ip = "10.0.0."
octet_range = range(0,8)
duplicate_ip = ['10.0.0.5', '10.9.20.5']
print(type(octet_range))

for last_octet in octet_range:
    new_ip = base_ip + str(last_octet)
    print(new_ip)
    chi_routers.append(new_ip)

chi_dup_routers = chi_routers + duplicate_ip
print(chi_dup_routers)

print("*"*40)
# Cast duplicates to a set and remove duplicates
houston_dup_routers_set = set(houston_dup_routers)
print(houston_dup_routers)
print(houston_dup_routers_set)

atl_dup_routers_set = set(atl_dup_routers)
print(atl_dup_routers)
print(atl_dup_routers_set)

chi_dup_routers_set = set(chi_dup_routers)
print(chi_dup_routers)
print(chi_dup_routers_set)
print("*"*40)

# Duplicated IP's
duplicates = houston_dup_routers_set & atl_dup_routers_set
print(duplicates)

# Duplicated IP's in all 3 sets
duplicates = houston_dup_routers_set & atl_dup_routers_set & chi_dup_routers_set
print(duplicates)

# IP's unique in Chicago
#chi_unique = chi_dup_routers_set.difference(houston_dup_routers_set)
#print(chi_unique)
chi_unique = chi_dup_routers_set.difference(houston_dup_routers_set).difference(atl_dup_routers_set)
print(chi_unique)
