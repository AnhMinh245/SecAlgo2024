import math

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

# Define a function to find the number of prime numbers in the range [a, b] 
# that can be expressed as the sum of two squares
def find_primes(a, b):
    count = 0
    for i in range(a, b+1):
        if is_prime(i):
            for x in range(1, int(math.sqrt(i))+1):
                for y in range(x, int(math.sqrt(i))+1):
                    if x*x + y*y == i:
                        count += 1
                        break
    return count



# Get the range from the user
a = int(input("Nhập giới hạn dưới của phạm vi: "))
b = int(input("Nhập giới hạn trên của phạm vi: "))

# Find and print the number of primes
print(f"Số lượng số nguyên tố trong phạm vi [{a}, {b}] có thể được biểu diễn dưới dạng tổng của hai bình phương là {find_primes(a, b)}.")
