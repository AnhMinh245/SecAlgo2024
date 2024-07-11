""" Câu 25. Cho 2 số M và N thoả mãn điều kiện: 1<=N<=10000; 2<M<=100; Hãy viết chương trình 
xác định xem số N có thể được phân tích thành tổng của M số nguyên tố hay không? Nếu có thì in 
ra các số đó """

import itertools

# Define a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

# Define a function to generate prime numbers up to n
def generate_primes(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

# Define a function to check if a number can be expressed as the sum of m prime numbers
def can_be_expressed_as_sum_of_primes(n, m):
    primes = generate_primes(n)
    for combination in itertools.combinations(primes, m):
        if sum(combination) == n:
            return True, combination
    return False, None

# Get the numbers from the user
n = int(input("Nhập số N: "))
m = int(input("Nhập số M: "))

# Check if n can be expressed as the sum of m prime numbers and print the result
result, combination = can_be_expressed_as_sum_of_primes(n, m)
if result:
    print(f"Số {n} có thể được biểu diễn dưới dạng tổng của {m} số nguyên tố: {combination}")
else:
    print(f"Số {n} không thể được biểu diễn dưới dạng tổng của {m} số nguyên tố.")
