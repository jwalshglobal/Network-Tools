#### Classes
# Hierarchy to share code
# CamelCase + Capitalize


class MyClass(object):
    # Initialize
    def __init__(self, ip_addr, username, password):
        print('My IP address is:')


### Modules - python file to import
## import my_fuct.py in previous example
# Where python looks when importing files
import sys
from pprint import pprint
pprint(sys.path)

### Second way to import
from my_func import print_ip
