def fibonacci(n):
    num_list = []
    if n <= 1:
        return 1
    elif n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        return result


numFibValues = int(input("How many fibonacci values do you want : "))

i = 1
while i < numFibValues:
    fibValue = fibonacci(i)
    print(fibValue)

    i += 1

print("All Done!")
