"""
Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
"""

my_list = ['192.168.1.1', '192.168.2.1']
my_list.append('4.2.2.2')
print(my_list)

my_list = ['192.168.1.1', '192.168.2.1']
new_list = ['8.8.8.8', '8.8.4.4']
my_list.extend(new_list)
print(my_list)

list_concatenate = my_list + new_list
print(list_concatenate)

print(list_concatenate[0])
print(list_concatenate[-1])

pop_list = list_concatenate.pop()
print(pop_list)

pop_list2 = list_concatenate.pop(0)
print(pop_list2)

my_list = ['192.168.1.1', '192.168.2.1']
new_list = ['8.8.8.8', '8.8.4.4']
list_concatenate = my_list + new_list
print(list_concatenate)
quad_two = '2.2.2.2'
list_concatenate.insert(0, quad_two)
print(list_concatenate)
print(list_concatenate[0])