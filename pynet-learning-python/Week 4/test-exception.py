my_dict = {}

try:
    print("Statement before")
    my_dict['ip_addr']
    #my_dict['ip_addr']
    print("Statement after")
except KeyError:
    print("Caught exception")

print("after exception")

print("*"*40)


my_dict = {}
try:
    my_dict['ip_addr']
except KeyError as e:
    print(e.__class__)
    print(str(e))
    print("Caught exception, printed info")

print("*"*40)

# Finally -- execute whether or not there is an exception

my_dict = {}
try:
    my_dict['ip_addr']
except KeyError:
    print("IP Address not found")
finally:
    print("This is always executed, exception or not")