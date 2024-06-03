# Câu 6. Hai số tạo thành một cặp số thân thiết khi chúng tuân theo quy luật: Số này bằng tổng tất 
# cả các ước của số kia (trừ chính số đó) và ngược lại. Viết chương trình tìm hai số dạng này nhỏ 
# hơn N (với N nhập vào từ bàn phím)

from math_modules.find_divisors import sum_of_divisors

def find_amicable_numbers(n):
    """Finds and prints all pairs of amicable numbers less than N."""
    for a in range(1, n):
        b = sum_of_divisors(a) - a
        if b > a and b < n: # ensure b is greater than a and less than N to avoid duplicates
            if sum_of_divisors(b) - b == a:
                print(a, b)
                
# Main program
if __name__ == "__main__":
    N = int(input("Enter a number N: "))
    find_amicable_numbers(N)               