# checking for prime numbers up to a particular value

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

        return True


def max_prime(max_num):
    list_of_prime = []

    for num1 in range(2, max_num):
        if is_prime(num1):
            list_of_prime.append(num1)

    return list_of_prime


max_num_prime = input("Give prime numbers up to which maximum point : ")

prime_num = int(max_num_prime)
primes = max_prime(prime_num)

for prime in primes:
    print(prime)
