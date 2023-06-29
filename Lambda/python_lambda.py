#Lambda functions can have many arguements but only one,
#expression.
print()
x = lambda a: a + 5
print(x(5))
print()

#muliple arguements.
y = lambda a, b: a * b
print(y(4, 6))
print()

#doubler by lambda
def my_func(n):
    return lambda a: a * n
my_doubler = my_func(2)
my_trippler = my_func(3)
print(my_doubler(11))
print(my_trippler(4))
print()