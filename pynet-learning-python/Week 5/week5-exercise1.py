"""
1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The
function should print out each of these three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.


1b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of
'cisco_ios'. Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
"""

from __future__ import unicode_literals, print_function
from pprint import pprint
import os


def funct_ssh(ip_addr, username, password):
    print("Here is the ip: {}".format(ip_addr))
    print("Here is the username: {}".format(username))
    print("Here is the password: {}".format(password))

# Positional arguments
funct_ssh('10.10.10.10', 'myname', 'mypass')

print()

# Named arguments
funct_ssh(ip_addr='192.168.3.1', username='somename', password='mypass')

print()

# Mix of positional and named
funct_ssh('192.168.99.1', username='somename', password='mypass')

