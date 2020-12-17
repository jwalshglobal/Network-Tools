# Fun with strings
from __future__ import print_function, unicode_literals

ip_addr1 = "172.16.1.1"
ip_addr2 = "10.1.1.1"
ip_addr3 = "192.168.1.1"
print("-" * 80)
#Print all three together
print("{}{}{}".format(ip_addr1, ip_addr2, ip_addr3))
#Create formatting (positional arguments)
print("{:20}{:20}{:20}".format(ip_addr1, ip_addr2, ip_addr3))
#Align to the left
print("{:>20}{:>20}{:>20}".format(ip_addr1, ip_addr2, ip_addr3))
#Center align
print("{:^20}{:^20}{:^20}".format(ip_addr1, ip_addr2, ip_addr3))

print("#Pass in named arguments")
print("-" * 80)

print("{my_ip:^20}{ip:^20}{ip_alt:^20}".format(ip_alt=ip_addr2,my_ip=ip_addr1,ip=ip_addr3))

print("\n")
print("-" * 80)
new_ip = "172.16.16.1"
octets = new_ip.split('.')

print(octets)
#Trick to pass each element of list into format (uses the *)
print("{:10}{:10}{:10}{:10}".format(*octets))

print("\n")
print("-" * 80)
ip_addr1 = "192.168.1.1"
port1 = 80
ip_addr2 = "192.168.2.1"
port2 = 443

#Deprecated formatting
print("%s %s" % (ip_addr1, ip_addr2))

#Python 3.6 and higher: F String

print(f"{ip_addr1}")
print(f"My IP address is: {ip_addr1:^20}")
print(f"My IP address is: {ip_addr1:^20}{port1:^10}")
print("-" * 80)
IP = "IP ADDRESS: "
PORT = "PORT: "

print("{:^10}{:^10}".format(IP,PORT))
print(f"{ip_addr1:^10}{port1:^10}")