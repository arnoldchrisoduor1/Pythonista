import math
import random

even_list = [k*2 for k in range(10)]

for k in even_list:
    print(k, end=", ")

listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4), math.pow(m, 5)]
                for m in even_list]

for k in listOfValues:
    print(k)
print()
