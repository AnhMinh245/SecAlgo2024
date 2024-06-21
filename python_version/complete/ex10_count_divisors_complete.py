# Câu 10. Viết chương trình đếm số ước và số ước nguyên tố của một số N nhập vào từ bàn phím.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_divisors(n): 
    count = 0
    prime_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            if is_prime(i):
                prime_count += 1
    return count, prime_count

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    divisors, prime_divisors = count_divisors(n)
    print(divisors)
    print(prime_divisors)