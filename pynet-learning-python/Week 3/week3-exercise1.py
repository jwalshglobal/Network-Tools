"""
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of the VLAN_ID,
VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple
consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""

#f = open("show_vlan.txt")
#vlan_list = f.readlines()
#vlan_list = vlan_list.strip()
#print(vlan_list)


from pprint import pprint

vlan_list = []
with open("show_vlan.txt") as f:
    #output = f.readlines()
    output = f.read()
    #sliced_vlans = output[2::]
    pprint(output)

print('*'*10)

for line in output.splitlines():
    if "VLAN" in line or "----" in line or line.startswith("  "):
        continue
    fields = line.split()
    #pprint(fields)
    vlan_id = fields[0]
    vlan_name = fields[1]
    #print(vlan_id)
    vlan_list.append((vlan_id,vlan_name))

print()
pprint(vlan_list)
print()

#pprint(output)
print('*'*10)

#pprint(sliced_vlans)