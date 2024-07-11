""" Câu 22. Với một số nguyên dương N thoả mãn 0<N<10000, đặt:
F ( N ) = N nếu N là một số nguyên tố
F ( N ) = 0 nếu là hợp số
Cho L và R nhập vào từ bàn phím, với mọi cặp i , j trong khoảng [ L , R ] hãy viết chương trình 
in ra màn hình giá trị tổng của F ( i ) * F ( j ) với j > i. """

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def F(N):
    return N if is_prime(N) else 0

def calculate_sum(L, R):
    total_sum = 0
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            total_sum += F(i) * F(j)
    return total_sum

def main():
    L = int(input("Enter integer L: "))
    R = int(input("Enter integer R: "))
    
    if not (0 < L < R < 10000):
        print("L and R must satisfy 0 < L < R < 10000.")
        return
    
    result = calculate_sum(L, R)
    
    print(f"The sum of F(i) * F(j) for all i, j in range [{L}, {R}] with j > i is: {result}")

if __name__ == "__main__":
    main()
