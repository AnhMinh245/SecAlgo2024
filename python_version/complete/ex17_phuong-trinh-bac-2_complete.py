""" 
Câu 17. Viết chương trình tìm số nguyên dương x nhỏ nhất và nhỏ hơn N nhập từ bàn phím sao 
cho giá trị của biểu thức Ax^2 + Bx + C = 0 là một số nguyên tố với A,B,C là các số nguyên nhập vào 
từ bàn phím. 
"""


""" 
1.Input Handling: Read integers A, B, C, and N from the user.
2. Prime Checking: Create a function to check if a number is prime.
3. Finding the Smallest x:
- Iterate through integers from 1 to N -1.
- For each x, evaluate Ax + Bx + C.
- Check if the result is a prime number.
- Return the smallest xx that meets the criteria.
4. Output: Print the smallest x found, or a message if no such x exists.
"""


def isPrime(N):
    if N < 2: 
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
        
    return True

def findSmallestX(A, B, C, N):
    for x in range(1, N):
        result = A*x**2 + B*x + C
        if isPrime(result):
            return x
    return None


if __name__ == "__main__":
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    C = int(input("Enter C: "))
    N = int(input("Enter N: "))
    x = findSmallestX(A, B, C, N)
    if x is not None:
        print(f"The smallest x is: {x}")
    else:
        print("No such x exists.")
        