import math

def find_all_divisors(n):
    """
    Find divisors of n.
    Args:
        n: The number to find divisors of.
    Returns: 
        A list of integers that divides n
    """
    
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return sorted(divisors)

def find_prime_divisors(n):
    """
    Find prime divisors of n.
    Args:
        n: The number to find prime divisors of.
    Returns: 
        A list of prime integers that divides n
    """
    divisors = find_all_divisors(n)
    max_divisor = max(divisors)
    isPrime = [True] * (max_divisor + 1)
    isPrime[0] = isPrime[1] = False
    
    for i in range(2, int(max_divisor ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, max_divisor + 1, i):
                isPrime[j] = False
                
    return [divisor for divisor in divisors if isPrime[divisor]]

def count_divisors(n):
    """
    Count divisors of n.
    Args:
        n: The number to count divisors of.
    Returns: 
        The count of divisors of n
    """
    return len(find_all_divisors(n))

def count_prime_divisors(n):
    """
    Count prime divisors of n.
    Args:
        n: The number to count prime divisors of.
    Returns: 
        The count of prime divisors of n
    """
    return len(find_prime_divisors(n))

if __name__ == "__main__":
    n = int(input("Enter N: "))
    if n <= 0:
        raise ValueError("n must be a positive integer")
    k = count_prime_divisors(n)  # Number of prime divisors of n
    q = sum(prime_divisor for prime_divisor in find_prime_divisors(n))  # Sum of prime divisors of n
    p = sum(divisor for divisor in find_all_divisors(n))  # Sum of all divisors of n
    s = count_divisors(n)  # Number of divisors of n
    
    print(n + p + s - q - k)
