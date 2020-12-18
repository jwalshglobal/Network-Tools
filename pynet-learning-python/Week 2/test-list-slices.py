f = open("show_version.txt")

output = f.readlines()
#print(len(output))
#print(output)

# Create new lists from existing list
new_slice = output[0:5]
print(new_slice)
print('-'*80)

new_slice = output[30:57]
print(new_slice)
print('-'*80)

new_slice = output[-1:-6]
print(new_slice)
print('-'*80)