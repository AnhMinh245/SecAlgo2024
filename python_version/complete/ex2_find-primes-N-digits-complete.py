# Câu 2. Viết chương trình tìm các số nguyên tố có N chữ số với N nhập từ bàn phím và 2 ≤ N ≤10.

""" Pseudocode
1. Read 𝑁 from the input.
2. If N is not between 2 and 10, print an error message and exit.
3. Calculate the range for N-digit numbers:
start = 10^(N-1)
end = 10^N - 1
4. Implement the Sieve of Eratosthenes to find all prime numbers in the range [start,end].
5. Print each prime number followed by ".0". """

import math

def sieve_of_eratosthenes_range(start, end):
    if end < 2 or start > end:
        return []
    
    # Khởi tạo danh sách prime với True từ 0 đến end
    prime = [True] * (end + 1)
    prime[0] = prime [1] = False
    
    for p in range (2, int(math.sqrt(end)) + 1):
        if prime[p]:
            for i in range (p * p, end + 1, p):
                prime[i] = False
                
    # Tạo danh sách các số nguyên tố trong khoảng start đến end
    primes = [p for p in range (start, end + 1) if prime[p]]
    return primes


def find_primes(n):
    if n < 2 or n > 10:
        print("N must be between 2 and 10.")
        return
    
    primes = sieve_of_eratosthenes_range(10**(n-1), 10**n -1)
    for prime in primes:
        print(f"{prime}.0")
    
if __name__ == "__main__":
    N = int(input("Enter the number of digits (2 ≤ N ≤ 10): "))
    find_primes(N)



