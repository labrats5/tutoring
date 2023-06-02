from math import sqrt, floor

def ordered_divisors(n):
    prime_divisors = []
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            prime_divisors.append(i)
            if i != n//i:
                prime_divisors.append(n//i)
    print(n, 'is divisible by', sorted(prime_divisors))
    if not prime_divisors:
        print(n, 'is prime!')
    else:
        print(n, 'is not prime.')


def isprime(n):
    is_prime = True
    for i in range (2, floor(sqrt(n))+1):
        if n % i == 0:
            print(n, 'is divisible by', i)
            if i != n//i:
                print(n, 'is divisible by', n//i)
            is_prime = False
    if is_prime:
        print(n, 'is prime!')
    else:
        print(n, 'is not prime.')


def input_loop():
    n = input('type a number: ')
    try:
        n = int(n)
        ordered_divisors(n)
    except ValueError:
        print('Please enter an integer')
        input_loop()
    if input('Try another? (y/n)') in ['y', 'Y']:
        input_loop()


if __name__ == '__main__':
    input_loop()