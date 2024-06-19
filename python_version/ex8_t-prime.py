# find T-prime numbers less than or equal to a given number N 

from math_modules.isPrime import *

def t_prime(n):
    """
    Find T-prime numbers less than or equal to n.
    Args:
        n: The number to find T-prime numbers of.
    Returns: 
        A list of T-prime integers less than or equal to n
    """
    t_primes = []
    for i in range (2, int(n**0.5) + 1):
        if isPrime(i):
            t_prime = i*i
            if t_prime <= n:
                t_primes.append(t_prime)
    return t_primes

# Main
if __name__ == "__main__":
    N = int(input("Enter a number: "))
    t_primes_list = t_prime(N)
    print("T-prime numbers less than or equal to", N, "are:")
    print(t_primes_list)