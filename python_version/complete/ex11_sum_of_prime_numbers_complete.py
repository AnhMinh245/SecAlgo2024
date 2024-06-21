# Câu 11. Viết chương trình tính tổng của các số nguyên tố nhỏ hơn hoặc bằng N với N được nhập từ bàn phím

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def sum_of_prime_numbers(n):
    sum = 0
    for i in range(2, n + 1):
        if isPrime(i):
            sum += i
    return sum

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    print(sum_of_prime_numbers(n))

    