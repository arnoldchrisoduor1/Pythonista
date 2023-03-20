import random
rand_num = random.randrange(1,10)

while True:
    guess = int(input("Please  give a random number : "))

    if guess == rand_num:
        print("Great you guessed it!")
        break


