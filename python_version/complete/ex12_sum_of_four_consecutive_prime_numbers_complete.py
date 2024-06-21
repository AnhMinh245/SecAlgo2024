# Câu 12. Viết chương trình tìm bốn số nguyên tố liên tiếp, sao cho tổng của chúng là số nguyên tố nhỏ hơn hoặc bằng N (với N được nhập vào từ bàn phím).
# Input: 20
# Output: 2 3 5 7 

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def generate_prime_up_to(n):
    """Generate all prime numbers up to N using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5 + 1)):
        if sieve[i]:
            for j in range (i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]] 


def sum_of_four_consecutive_prime_numbers(n):
    primes = generate_prime_up_to(n)
    for i in range(len(primes) - 3):
        if primes[i] + primes[i + 1] + primes[i + 2] + primes[i + 3] <= n and isPrime(primes[i] + primes[i + 1] + primes[i + 2] + primes[i + 3]):
            return primes[i], primes[i + 1], primes[i + 2], primes[i + 3]
    return ()  # Return an empty tuple if no sequence is found

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    result = sum_of_four_consecutive_prime_numbers(n)
    for i in result:
        print(i)