import math

primes = []

def check_prime(number):
    if number <= 1:
        return False

    sqrt = math.sqrt(number)

    for prime in primes:
        if prime <= sqrt and (number % prime) == 0:
            return False

    return True

def loop_numbers():
    for i in range(1,100000):
        if check_prime(i):
            print "%d is prime" % i
            primes.append(i)

loop_numbers()
print primes
