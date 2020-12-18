'''
#Open file, read, and print output. Returns a STRING

f = open("show_version.txt")
output = f.read()
print(output)
f.close()
'''

'''
Opens file, reads each lines and returns a LIST

f = open("show_version.txt")
output = f.readlines()
print(type(output))
print(output)
f.close()
'''

'''
Alternate Way

f = open("show_version.txt")
output = f.read()
splt_lines = output.splitlines()
print(type(splt_lines))
print(output)
f.close()
'''

'''
Automatically close file. Prints to string
'''

with open("show_version.txt") as f:
    output = f.read()
print(type(output))
print(output)