def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

print(factorial(5))

def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result

print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(20))
print(fibonacci(7))
print(fibonacci(9))


customer = []

while True:
    ask = input("Do you want to input name(y/n) : ")

    if ask == 'n':
        break
    else:
        fName, lName = input("Give your first and last name : ").split()
        customer.append({"fName" :fName, "lName" : lName})


