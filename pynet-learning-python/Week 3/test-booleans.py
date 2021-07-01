a = True
print(type(a))

b = False
print(type(b))

print("> AND")
print(a and a)
print(a and b)
print(b and b)

print("> OR")
print(a or a)
print(a or b)

print("> NOT")
print(not(a))

print("> MATH")
print((10 > 2))
print((10 >2) and (9 < 73) or 7 == 7)

print("> Ternary Operator")
my_val = 1
a = 'whatever' if my_val >2 else 'something'
print(a)

#### Same thing as:

if my_val > 2:
    a = 'whatever'
else:
    a = 'something'
print(a)