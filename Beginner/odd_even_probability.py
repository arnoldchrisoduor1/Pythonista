#create a random number
#determine if the number is odd or even and calculate the times it was odd or even
#calculate the probability of the number being odd or even
#itertae over a number of times

import random

q = input("How many times should we iterate over the random number: ")

q = int(q)
even = 0
even_p = 0
odd = 0
odd_p = 0


for n in range(q):
    rand_num = random.randrange(1,1001)
    if rand_num % 2 == 0:
        even += 1
        print("loading//")
    else:
        odd += 1
        print("loading_")

total = even + odd

odd_p = (odd/total) * 100
even_p = (even/total) * 100

print("The probability of the number being odd is: ",odd_p)
print("\n")
print("The probability of the number being even is: ",even_p)
