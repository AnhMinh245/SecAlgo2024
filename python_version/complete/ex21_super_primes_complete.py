""" Câu 21. Một số gọi là siêu số nguyên tố nếu số lượng các số nguyên tố từ 1 đến X (ngoại trừ X) là 
một số nguyên tố. Hãy viết chương trình đếm số lượng các siêu số nguyên tố này trong khoảng 
[A,B] cho trước nhập từ bàn phím. """
""" 
Pseudocode
1. Sieve of Eratosthenes:
- Initialize a boolean array is_prime of size B + 1
- Mark non-prime numbers in this array.
2. Check if a number is prime:
- Define is_prime_number(n) function to check if n is in the list of primes.
3. Count primes less than X:
- Define count_primes_less_than(X) function to count the number of primes less than X.
4. Main logic:
Iterate through each number in range [A,B].
- For each number, count the primes less than it.
- Check if the count is a prime.
- If true, increment the super prime count.
5. Print the result. """

def sieve_of_eratosthenes(B):
    primes = [True ] * (B + 1)
    primes[0] = primes[1] = False

    for p in range(2, int(B ** 0.5) + 1):
        if primes[p]:
            for i in range(p * p, B + 1, p):
                primes[i] = False

    return [p for p in enumerate(primes) if primes[p]]

def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_less_than(X):
    count = 0
    for i in range(2, X):
        if is_prime_number(i):
            count += 1
    return count

def super_primes_count(A, B):
    count = 0
    for i in range(A, B + 1):
        if is_prime_number(count_primes_less_than(i)):
            count += 1
    return count

A = int(input())
B = int(input())

print(super_primes_count(A, B))




                
