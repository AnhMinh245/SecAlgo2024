""" Câu 27. Viết chương trình in ra các cặp số (a,b) thoả mãn điều kiện 0<a,b<1000, sao cho ước 
chung lớn nhất của 2 số đó là một số nguyên tố. """

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_valid_paris(a, b):
    for i in range(a, b):
        for j in range(i+1, b):
            if is_prime(gcd(i, j)):
                print(f'({i}, {j})')

if __name__ == '__main__':
    a = int(input('Nhập a: '))
    b = int(input('Nhập b: '))
    find_valid_paris(a, b)

