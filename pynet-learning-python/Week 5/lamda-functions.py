# Lamda Functions
# one line disposible functions

def my_func(x):
    return x**2

print(my_func(10))

print('-'*40)

# assigned value is variable x, and what is the return value
# Why is it used? Useful to have function that can be passed as an argument. Easy to defice and use in one line
f = lambda x: x**2
print(f(10))