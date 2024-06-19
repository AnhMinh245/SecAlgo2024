# Câu 7. Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được 
# một số nguyên tố. Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím

from math_modules.isPrime import *
from math_modules.reverse_number import *

def is_emirp(n):
    if is_prime(n):
        reversed_n = reverse_number(n)
        if is_prime(reversed_n):
            return True
    return False

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print("Emirp numbers less than", N, "are:")
    for i in range(2, N):
        if is_emirp(i):
            print(i, end=" ")