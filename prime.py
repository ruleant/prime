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

def predict_primes():
    start = 1
    for i in range(0,4):
        print "loop %d, start %d" % (i, start)
        prime_list = []
        print "primes : %s" % primes
        if len(primes) > 1:
            iteration_length = 1
            for t in primes[0:i]:
                iteration_length *= t
            iterations = primes[i] - 1
            prime_list = primes[i:]
        elif len(primes) == 1:
            iterations = iteration_length = primes[0]
        else:
            iterations = 1
            iteration_length = 1

        prime_list.insert(0, 1)
        print "prime_list %s" % prime_list
        print "%d iterations, length %d" % (iterations, iteration_length)

        for j in range(1, iterations + 1):
            print "start %d" % start
            for k in prime_list:
                new_prime = start + k
                print " check %d" % new_prime
                if check_prime(new_prime):
                    print "  %d is prime" % new_prime
                    primes.append(new_prime)

            start += iteration_length

#loop_numbers()
predict_primes()
print primes
