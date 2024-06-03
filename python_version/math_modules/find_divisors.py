import math

def find_all_divisors(n):
    """
    Find divisors of n.
    Args:
        n: The number to find divisors of.
    Returns: 
        A list of integers that divides n
    """
    # Check that n is a positive integer.
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    divisors = []
    # Append divisors to the list of divisors.
    for  i in range (1, int(math.sqrt(n)) + 1):
        # Append to the end of the divisors.
        if n % i == 0:
            divisors.append(i)
            # appends n to the divisors list
            if n // i != i:
                divisors.append(n // i)
    return divisors

def find_prime_divisors(n):
    divisors = find_all_divisors(n)
    max_divisor = max(divisors)
    isPrime = [True] * (max_divisor + 1)
    isPrime[0] = isPrime[1] = False
    
    # Sử dụng thuật toán sàng Eratosthenes để tìm các số nguyên tố.
    for i in range(2, int(max_divisor ** 0.5) + 1):
        if isPrime[i]:
            for j in range (i * i, max_divisor + 1, i):
                isPrime[j] = False
                
    return [divisor for divisor in divisors if isPrime[divisor]]

def count_divisors(n):
    return len(find_all_divisors(n))
    
def count_prime_divisors(n):
    return len(find_prime_divisors(n))

def sum_of_divisors(n):
    divisors = []
    # Append divisors to the list of divisors.
    for  i in range (1, int(math.sqrt(n)) + 1):
        # Append to the end of the divisors.
        if n % i == 0:
            divisors.append(i)
            # appends n to the divisors list
            if n // i != i:
                divisors.append(n // i)
    return sum(divisor for divisor in divisors)
    