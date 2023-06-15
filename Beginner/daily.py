#Random numbers in percentage
import random
import time

start_time  = time.time()

q = int(input("Loop how many times: "))

even = 0
even_p = 0
odd = 0
odd_p = 0

for n in range(q):
    rand_num = random.randrange(1, 1001)
    if rand_num % 2 == 0:
        even += 1
        print("{} is even". format(rand_num))
    else:
        odd += 1
        print("{} is an odd number ".format(rand_num))

total = even + odd

even_p = (even/total) * 100
odd_p = (odd/total) * 100

print("Probability of an odd number ",odd_p)
print("Probability of an even number ",even_p)

end_time  = time.time()

execution_time = end_time - start_time

print("Execution time : {}".format(execution_time))