""" Câu 3. Cho một số nguyên dương N, gọi:
- k là số ước nguyên tố của N;
- q là tổng của các ước nguyên tố của N;
- p là tổng của các ước số của N;
- s là số ước của N;
Hãy viết chương trình tính giá trị của: N+p+s-q-k với N cho trước nhập từ bàn phím.
Ví dụ: N=24, có các ước là {1,2,3,4,6,8,12, 24} do đó: 
p=1+2+3+4+6+8+12+24=60 và s=8
trong đó có 2 ước nguyên tố là {2,3} do đó:
q=2+3=5 và k=2
Và từ đó: N+p+s-q-k = 24+60+8-5-2=85;
"""

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


if __name__ == "__main__":
    n = int(input()) 
    if n <= 0:
        raise ValueError("n must be a positive integer")

    prime_divisors = list(find_prime_divisors(n))  # Calculate once and store
    all_divisors = list(find_all_divisors(n))  # Calculate once and store

    k = len(prime_divisors)  # Number of prime divisors of n
    q = sum(prime_divisors)  # Sum of prime divisors of n
    p = sum(all_divisors)  # Sum of all divisors of n
    s = len(all_divisors)  # Number of divisors of n

    result = n + p + s - q - k
    print(result)
