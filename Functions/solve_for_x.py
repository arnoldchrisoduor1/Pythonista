# x will always be the first input

# will only deal with additions
value = input("Write the equation in the format (x + y = ans) : ")


def solve_x(equation):
    global value
    value = value.split()
    num1 = int(value[2])
    num2 = int(value[4])

    x = num2 - num1
    print("The value of X is : ", str(x))


solve_x(value)
