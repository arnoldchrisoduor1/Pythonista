import random
import math

num_list = []

for i in range(0, 5):
    num_list.append(random.randrange(0, 10))

i = len(num_list)-1

while i > 1:
    j = 0
    while j < i:
        print("\n{} : {}".format(num_list[j], num_list[j+1]))
        if num_list[j] > num_list[j+1]:
            print("switch")
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
        else:
            print("Don't switch")
        j += 1
        for k in num_list:
            print(k, end=", ")
        print()
    print("END OF ROUND")
    i -= 1
for n in num_list:
    print(n, end=", ")
