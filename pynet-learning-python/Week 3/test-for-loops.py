some_list = ['192.168.1.1', '10.1.1.1', '10.10.20.30', '172.16.31.254']

ip_address_list = some_list

print(ip_address_list)

for ip in ip_address_list:
    print("My IP address is")
    print(ip)
    print("the end")

print(ip_address_list[1])
print("-"*40)

#Enumerate with index plus the value in a tuple
for my_var in enumerate(ip_address_list):
    print(my_var)

#Enumerate both index and tuple value
for i, ip_addr in enumerate(ip_address_list):
    print(i)
    print(ip_addr)
    print('-' * 30)

# break
print("-"*40)

for ip in ip_address_list:
    print(ip)
    if ip == '10.10.20.30':
        break

# continue - goes back to original for statement (and does not print 10.10.20.30)
print("-"*40)

for ip in ip_address_list:
    print('hello')
    if ip == '10.10.20.30':
        continue
    print(ip )

# pass -- no op


# Nest for loops
print("-"*40)

some_list = ['192.168.1.1', '10.1.1.1', '10.10.20.30', '172.16.31.254']
ip_list2 = ['8.8.8.8', '8.8.4.4']

for ip in some_list:
    for ip2 in ip_list2:
        print(ip)
        print(ip2)

