from __future__ import print_function

try:
    ip_addr = raw_input("Enter an IP address: ")
except NameError:
    ip_addr = input("Enter an IP address: ")
print(ip_addr)