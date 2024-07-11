# Câu 23. Viết chương trình in ra màn hình YES trong trường hợp tổng của các số nguyên tố trong 
# khoảng [A, B] là cũng là một số nguyên tố và NO nếu ngược lại. Với A,B là hai số được nhập vào từ bàn phím. 


def sieveOfEratosthenes(A, B):
    if B < 2: return 0
    if A < 2: A = 2
    if A > B: 
        A, B = B, A
    
    primes = [True for _ in range(B + 1)] # 
    primes[0] = primes[1] = False
    sumPrimes = 0

    for p in range (2, int(B ** 0.5) + 1):
        if primes[p]:
            for i in range(p * p, B + 1, p):
                primes[i] = False
    for i in range(A, B + 1):
        if primes[i]:
            sumPrimes += i
    return sumPrimes

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    sumPrimes = sieveOfEratosthenes(A, B)
    print("YES" if isPrime(sumPrimes) else "NO")



