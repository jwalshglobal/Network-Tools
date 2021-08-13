import pdb

def print_ip(ip_addr, username='def-admin', password='def-pass'):
    print("My IP Address is {}".format(ip_addr))
    print(username)
    print(password)
    return

#python break point
pdb.set_trace()
print_ip('10.1.1.1')

# Can see (Pdb)
 list .
 list 1, 20
# commands:
 s
 args
 pp ip_addr
 up
 down
 next

#Use Python debugger on command line
python -m pdb my_func.py

# Create Break Point
# Execute python in pdb:
!print_ip("172.1.1.1")
!username = 'cisco'

