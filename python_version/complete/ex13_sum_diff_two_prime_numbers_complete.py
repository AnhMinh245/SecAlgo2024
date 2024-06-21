# Câu 13. Viết chương trình tìm hai số nguyên tố nhỏ hơn hoặc bằng N với N nhập vào từ bàn 
# phím, sao cho tổng và hiệu của chúng đều là số nguyên tố.

import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

""" def findPrimeNumbers(n):
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes """

def findPrimeNumbers(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]

def sum_diff_two_prime_numbers(n):
    primes = findPrimeNumbers(n)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] + primes[j] <= n and isPrime(primes[i] + primes[j]) and isPrime(abs(primes[i] - primes[j])):
                return primes[i], primes[j]
    return ()  # Return an empty tuple if no sequence is found

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    result = sum_diff_two_prime_numbers(n)
    for i in result:
        print(i)
