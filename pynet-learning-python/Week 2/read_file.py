'''
Open file, read, and print output. Returns a string

f = open("show_version.txt")
output = f.read()
print(output)
f.close()
'''

f = open("show_version.txt")
output = f.readline()
type(output)
print(output)
f.close()
