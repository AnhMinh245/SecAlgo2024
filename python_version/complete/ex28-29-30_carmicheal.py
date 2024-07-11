""" Câu 28. Viết chương trình tìm và đếm  các số Carmichael (là các số giả nguyên tố n thỏa mãn điều kiện 
là hợp số và thỏa mãn 𝑏^(𝑛−1) ≡ 1 (𝑚𝑜𝑑 𝑛) với mọi số nguyên dương b nguyên tố cùng nhau với n) 
nhỏ hơn một số N cho trước nhập vào từ bàn phím (với điều kiện 0 ≤ 𝑁 ≤ 10000. """

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

def is_carmichael(n):
    if is_prime(n):
        return False
    for b in range(2, n):
        if gcd(b, n) == 1: 
            if pow(b, n-1, n) != 1:
                return False
    return True

def find_carmichael_numbers(N):
    carmichael_numbers = []
    for i in range(2, N):
        if is_carmichael(i):
            carmichael_numbers.append(i)
    return carmichael_numbers

if __name__ == '__main__':
    N = int(input("Enter an integer N (0 <= N <= 10000): "))
    
    if not (0 <= N <= 10000):
        print("N must be in the range 0 <= N <= 10000.")
    else:
        carmichael_numbers = find_carmichael_numbers(N)
        print(f"Carmichael numbers less than {N}: {carmichael_numbers}")
        print(f"Total count of Carmichael numbers less than {N}: {len(carmichael_numbers)}")
        #sum of carmichael numbers
        print(f"Sum of Carmichael numbers less than {N}: {sum(carmichael_numbers)}")