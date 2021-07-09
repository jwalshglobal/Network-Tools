my_ip = ['192.168.1.1', '10.220.17.9', '31.1.1.1', '192.168.1.1']

print(my_ip)

#eliminates the duplicate
set_ip = set(my_ip)
print(set_ip)

set_ip_2 =  {'10.220.17.9', '8.8.4.4', '172.31.254.1'}

#union of two sets and eliminate the duplicate elements
join_sets = set_ip | set_ip_2
print(join_sets)

#intersection of sets to get common elements
shared_sets = set_ip & set_ip_2
print(shared_sets)

#symetric differences
print('-----------------')
symetric = set_ip ^ set_ip_2
print(symetric)