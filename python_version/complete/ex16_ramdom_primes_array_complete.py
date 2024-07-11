""" Câu 16. Viết chương trình tìm các số nguyên tố từ một mảng sinh ngẫu nhiên có kích thước N, 
với N nhập vào từ bàn phím.
"""

""" 
1. Input Handling: Read the integer N from the user.
2. Random Array Generation: Generate an array of N random integers.
3. Prime Checking: Create a function to check if a number is prime.
4. Finding Primes in the Array: Iterate through the array and find all prime numbers.
5. Output: Print all the prime numbers found in the array. """

import random

def isPrime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True

def randomArray(n):
    return [random.randint(1, 100) for _ in range(n)]

def findPrimes(arr):
    return [num for num in arr if isPrime(num)]

if __name__ == "__main__":
    N = int(input("Enter the size of the array: "))
    random_array = randomArray(N)
    print(f"Random Array: {random_array}")
    primes = findPrimes(random_array)
    print(f"Prime Numbers: {primes}")