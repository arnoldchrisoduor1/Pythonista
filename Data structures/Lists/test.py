import random
import math

rand_list = ["Hello", 2, "two", 4.9]

new = list(range(10))

newer = rand_list + new
first3 = newer[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i),i))
print()
print(first3[0]*3)
print("string" in first3)
print("The index of string : ",first3.index("Hello"))

print("How many hello statements : ",first3.count("Hello"))

first3.append("Another")
first3.insert(4, 69)
first3.reverse()
first3.sort()
print(first3)

