# Functions!
# Always have have a retrun value

#define the function
def print_ip():
    print("My IP Address is 192.168.1.1")

#call the function
print_ip()
print_ip()

#pass an argument
def print_ip(ip_addr, username, password):
    print("My IP Address is {}".format(ip_addr))
    print(username)
    print(password)
    return

print_ip('10.1.1.0', 'admin', 'admin123')
print_ip('10.1.1.100', 'admin', 'admin123')
print_ip(ip_addr='10.10.10.10', username='read-only', password='mypass')

#pass an argument with default values
def print_ip(ip_addr, username='def-admin', password='def-pass'):
    print("My IP Address is {}".format(ip_addr))
    print(username)
    print(password)
    return

print_ip('10.1.1.0')

#pass a dictionary and use each element of the list
# Caution: Be careful of using mutable types like lists
def print_ip(ip_addr, username='def-admin', password='def-pass'):
    print("My IP Address is {}".format(ip_addr))
    print(username)
    print(password)
    return

my_list = ['10.1.1.1', 'admin', 'admin123']

my_dict = {
    'ip_addr': '172.16.31.1',
    'username': 'admin_dict',
    'password': 'juniper123'
}
# Pass list -- Not so great... Use dictionary instead
print_ip(*my_list)

# Add a DOUBLE star
print_ip(**my_dict)

print()
# Variables - global namespaces - local variables are checked first, then global variables
ip_addr = '172.16.1.1'

def print_ip(ip_addr, username='def-admin', password='def-pass'):
    print("My IP Address is {}".format(ip_addr))
    print(username)
    print(password)
    return

print_ip('3.3.3.3')