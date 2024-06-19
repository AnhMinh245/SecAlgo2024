# Câu 7. Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được 
# một số nguyên tố. Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím

# Pseudocode:
# 1. Define a function to check if a number is prime.
# 2. Define a function to reverse the digits of a number.
# 3. Iterate through each number from 2 to N-1
# 4. For each number, check if it is a prime.
# 5. If it is prime, reverse its digits and check if the reversed number is also prime.
# 6. If both conditions are satisfied, print the number.

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    """Reverse the digits of a number."""
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
    return reversed_n

def is_emirp(n):
    if is_prime(n):
        reversed_n = reverse_number(n)
        if is_prime(reversed_n):
            return True
    return False

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    for i in range(2, N):
        if is_emirp(i):
            print(i)