def fibonacci(n):
    num_list = []
    if n <= 1:
        return 1
    elif n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        num_list.append(result)
        return num_list

print(fibonacci(9))

