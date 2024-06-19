# find T-prime numbers less than or equal to a given number N 

"""
Pseudocode:
1. Define a function to check if a number is prime.
2. Iterate through numbers to find primes.
3. Square each prime number and check if it is less than or equal to N.
4. Print the T-prime numbers.
"""

def isPrime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
    for t_prime in t_primes_list:
        print(t_prime)