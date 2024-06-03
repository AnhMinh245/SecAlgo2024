""" Pseudocode
1. Read 𝑁 from the input.
2. If N is not between 2 and 10, print an error message and exit.
3. Calculate the range for N-digit numbers:
start = 10^(N-1)
end = 10^N - 1
4. Implement the Sieve of Eratosthenes to find all prime numbers in the range [start,end].
5. Print each prime number followed by ".0". """

import math
from math_modules.eratosthenes_in_range import sieve_of_eratosthenes_range


def find_primes(n):
    # Kiểm tra điều kiện đầu vào
    if n < 2 or n > 10:
        print("N must be between 2 and 10.")
        return
    # Sử dụng hàm eratosthenes để tìm các số nguyên tố trong khoảng 
    primes = sieve_of_eratosthenes_range(10**(n-1), 10**n -1)
    for prime in primes:
        print(f"{prime}.0")
    
if __name__ == "__main__":
    N = int(input("Enter the number of digits (2 ≤ N ≤ 10): "))
    find_primes(N)



