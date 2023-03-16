#take input and convert to integer

num = input("Upto which number: ")

num = int(num)
num = num + 1

"""use rnge to iterate through all the numbers upto the input number
while checking using modulus"""

#print numbers stating whether even or odd

for n in range(num):
    if n % 2 == 0:
        print("{} is an even number".format(n))
        print("\n")
    else:
              print("{} is an odd number".format(n))
              print("\n")

print("The program was executed successfully")
