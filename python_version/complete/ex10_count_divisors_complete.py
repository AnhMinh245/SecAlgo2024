# Câu 10. Viết chương trình đếm số ước và số ước nguyên tố của một số N nhập vào từ bàn phím.

# Hàm kiểm tra một số là số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Hàm đếm số ước và số ước nguyên tố của một số N
def count_divisors(n): 
    count = 0 # Số ước của N
    prime_count = 0 # Số ước nguyên tố của N
    for i in range(1, n + 1): # Duyệt qua các số từ 1 đến N
        if n % i == 0: # Nếu i là ước của N
            count += 1  # Tăng số ước lên 1
            if is_prime(i): # Nếu i là số nguyên tố
                prime_count += 1 # Tăng số ước nguyên tố lên 1
    return count, prime_count

if __name__ == '__main__':
    n = int(input('Nhập số N: '))
    divisors, prime_divisors = count_divisors(n) # Gọi hàm đếm số ước và số ước nguyên tố
    print(divisors) # In ra số ước của N
    print(prime_divisors) # In ra số ước nguyên tố của N