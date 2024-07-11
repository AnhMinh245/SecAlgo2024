""" Câu 15. Viết chương trình Hai số nguyên tố sinh đôi là hai số nguyên tố hơn kém nhau 2 đơn vị. 
Tìm hai số nguyên tố sinh đôi nhỏ hơn hoặc bằng N, với N được nhập vào từ bàn phím """

""" 
1. Input Handling: Read the integer N from the user.
2. Prime Checking: Create a function to check if a number is prime.
3. Finding Twin Primes:
- Iterate through numbers from 2 to N.
- Check if the current number and the number 2 units ahead are both prime.
4. If both are prime, record the pair as a twin prime.
Output: Print all the twin prime pairs found. """

def isPrime(n):
    if n < 2: 
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    N = int(input())
    for i in range(2, N - 1):
        if isPrime(i) and isPrime(i + 2):
            print(f"({i}, {i + 2})")