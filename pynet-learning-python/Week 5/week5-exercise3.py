"""
 Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return the normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
"""

mac_list1 = ['aaaa.1dea.0eb6', 'aaaa.1dea.1111']
mac_list2 = ['bbbb.1dea.0eb6', 'bbbb.1dea.1111']
mac_list3 = ['cccc.2fdb.0eb6', 'cccc.2fdb.1111', 'cccc.2fdb.2222']

def gen_mac(mac_list):
    for mac in mac_list:
        mac_addr = mac
        #print(mac)
        for dotted_mac in mac_addr.splitlines():
            no_dot_mac = dotted_mac.replace(".","")
            #print(no_dot_mac)
            for mac in no_dot_mac.splitlines():
                colon_mac = ':'.join(mac[i:i + 2] for i in range(0, 12, 2))
                print(colon_mac.upper())

new_mac_list1 = gen_mac(mac_list1)
print(new_mac_list1)

new_mac_list2 = gen_mac(mac_list2)
print(new_mac_list2)

new_mac_list3 = gen_mac(mac_list3)
print(new_mac_list3)