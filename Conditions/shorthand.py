#short hand if else statements
a = 3
b = 8

print("A is bigger") if a > b else print("A is smaller")

#another shorthand conditional
print("\n")
print("A") if a > b else print("=") if a == b else print("B")


#the pass statement is used to avoid errors in null
#conditinals.
print("\n")
if a > b:
    pass