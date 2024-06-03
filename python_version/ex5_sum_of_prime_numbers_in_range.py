# Câu 5. Viết chương trình tính tổng của các số nguyên tố nằm trong khoảng [A, B] với A, B nhập vào từ bàn phím

from math_modules.eratosthenes_in_range import *

if __name__ == "__main__":
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    prime_divisors = sieve_of_eratosthenes_range(A, B)
    print(prime_divisors) # Các số nguyên tố trong khoảng [A,B]
    print(sum(prime for prime in prime_divisors))
    