""" Câu 26. Một số được gọi là số mạnh mẽ khi nó đồng thời vừa chia hết cho số nguyên tố và chia 
hết cho bình phương của số nguyên tố đó. Tìm số mạnh mẽ nhỏ hơn số N cho trước (N < 10000) """

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

# Define a function to print all powerful numbers less than n
def print_all_powerful_numbers(n):
    for i in range(2, n):
        for j in range(2, int(math.sqrt(i))+1):
            if is_prime(j) and i % j == 0 and i % (j*j) == 0:
                print(i)
                break

# Get the number from the user
n = int(input("Nhập số N: "))


# Print all powerful numbers less than n
if print_all_powerful_numbers(n) is None:
    print()
else:
    print(print_all_powerful_numbers(n))
