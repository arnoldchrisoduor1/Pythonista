#!/usr/bin/python3

num1, num2 = input("Type out two numbers:").split()

#convert the string to integer numbers
num1 = int(num1)
num2 = int(num2)

#Sum up the numbers
sum = num1 + num2

#Show the diffrence of the numbers
difference = num1 - num2

#Find the product the numbers
product = num1 * num2

#Find the modulus of the numbers
modulus = num1 % num2

#Print out the results
print("{} + {} = {}".format(num1,num2,sum))
print("{} - {} = {}".format(num1,num2,difference))
print("{} * {} = {}".format(num1,num2,product))
print("{} % {} = {}".format(num1,num2,modulus))
