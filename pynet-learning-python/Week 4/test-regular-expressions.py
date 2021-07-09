import  re

line = "10.220.100.9"

ip_addr = line

# match one character in the ip_addr variable
character = re.search(r".", ip_addr)
print(character)

# match all characters
character = re.search(r".+", ip_addr)
print(character)

# match on zero or more chacters
character = re.search(r".*", ip_addr)
print(character)

#Anchors - start at the beginning of string and end of the string
character = re.search(r"^.+$", ip_addr)
print(character)

#Digit 0 - 9
character = re.search(r"\d\d", ip_addr)
character = re.search(r"\d\d\d", ip_addr)
character = re.search(r"\d+$", ip_addr)
print(character)

#non white-space character class
ip_addr = '      10.220.100.9    '
character = re.search(r"^\S+", ip_addr)
print(character)

# Save with parentheses - save to groups
character = re.search(r"^\s+(\S+)", ip_addr).group(0)
print(character)
character = re.search(r"^\s+(\S+)", ip_addr).group(1)
print(character)
# show groups
character = re.search(r"^\s+(\S+)", ip_addr).group(0)
print(character)

print()
print("*"*40)
print()

# Use raw strings for patterns i.e. avoid \n used as a new line

