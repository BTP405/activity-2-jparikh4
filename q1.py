def getprimenumbers(n):
    "checking if prime number are there or not within given number"""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
#Example:
n = 30
prime_number= getprimenumbers(n)
print(f"Prime numbers between 2 and {n}: {prime_number}")
