""" Câu 43. Cho N nhập vào từ bàn phím (0<N<1000), sinh một số nguyên tố p<100. Hãy viết 
chương trình tìm tất cả các số nguyên a<N sao cho a^p mod N là số nguyên tố """


import random


# Hàm kiểm tra một số là số nguyên tố
def isPrime(n):
    if n < 2: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): # Duyệt qua các số từ 2 đến căn bậc 2 của n
        if n % i == 0:
            return False
    return True

# Hàm tìm các số nguyên tố nhỏ hơn N
def findPrimes(N):
    primes = []
    for i in range(2, N):
        if isPrime(i):
            primes.append(i)
    return primes

# Thuật toán nhân bình phương có lặp 
def nhan_binh_phuong_co_lap(a, p ,N):
    result = 1
    a = a % N # Lấy phần dư của a khi chia cho N
    while p > 0: # Duyệt qua các bit của p
        if p % 2 == 1: # Nếu bit cuối cùng của p là 1
            result = (result * a) % N # Nhân kết quả với a và lấy phần dư khi chia cho N
        p = p // 2 # Chia p cho 2
        a = (a * a) % N # Bình phương a và lấy phần dư khi chia cho N
    return result

if __name__ == "__main__":
    # Nhập N từ bàn phím
    N = int(input("Nhập số nguyên N (0 < N < 1000): "))
    if N <= 0 or N >= 1000:
        print("Đầu vào không hợp lệ! N phải nằm trong khoảng 0 < N < 1000.")
        exit()
    # Tìm các số nguyên tố nhỏ hơn N
    primes = findPrimes(100)
    # Hàm sinh số p ngẫu nhiên
    p = random.choice(primes)
    print(f"Số nguyên tố p < 100: {p}")
    # Tìm các số nguyên a<N sao cho a^p mod N là số nguyên tố
    print(f"Các số nguyên a < N sao cho a^{p} mod {N} là số nguyên tố:")
    for a in range(1, N):
        if isPrime(nhan_binh_phuong_co_lap(a, p, N)):
            print(a)
