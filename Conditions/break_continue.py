#Break statement for even when the condition is true.
a = 746
b = 474

while b < a:
    print(b)
    if b == 500:
        break
    b += 1

while b < a:
    b += 1
    if b == 500:
        continue
    print(b)

#else statement will not be executed if the conditional
#is stopped by a break statement.