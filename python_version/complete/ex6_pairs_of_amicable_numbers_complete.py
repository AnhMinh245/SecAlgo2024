# Câu 6. Hai số tạo thành một cặp số thân thiết khi chúng tuân theo quy luật: Số này bằng tổng tất 
# cả các ước của số kia (trừ chính số đó) và ngược lại. Viết chương trình tìm hai số dạng này nhỏ 
# hơn N (với N nhập vào từ bàn phím)

""" Pseudocode: 
function sum_of_proper_divisors(n):
    sum = 0
    for i from 1 to n-1:
        if n % i == 0:
            sum += i
    return sum

function find_amicable_numbers(N):
    for a from 1 to N-1:
        b = sum_of_proper_divisors(a)
        if b > a and b < N:
            if sum_of_proper_divisors(b) == a:
                print(a, b)

"""
import math

def sum_of_divisors(n):
    divisors = []
    # Append divisors to the list of divisors.
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def find_amicable_numbers(n):
    """Finds and prints all pairs of amicable numbers less than N."""
    for a in range(1, n):
        b = sum_of_divisors(a)
        if b > a and b < n: # ensure b is greater than a and less than N to avoid duplicates
            if sum_of_divisors(b) == a:
                print(a, b)
                
# Main program
if __name__ == "__main__":
    N = int(input("Enter a number N: "))
    find_amicable_numbers(N)          