# Câu 14. Viết chương trình tìm số nguyên tố có ba chữ số, biết rằng nếu viết số đó theo thứ tự ngược lại 
# thì ta được một số là lập phương của một số tự nhiên.

# Hàm kiểm tra số nguyên tố
def isPrime(n):
    if n < 2: 
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: 
            return False
    return True

# Hàm đảo ngược số
def reverseNumber(n):
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n = n // 10
    return reversed_n

# Hàm kiểm tra số có phải là lập phương của một số tự nhiên hay không
def isCube(n):
    cube_root = int(n ** (1/3)) # Lấy căn bậc 3 của n
    return cube_root ** 3 == n # Kiểm tra n có phải là lập phương của cube_root hay không

# Tìm số nguyên tố có ba chữ số thỏa mãn yêu cầu đề bài
def findThreeDigitPrime():
    for i in range(100, 1000):
        if isPrime(i):
            if isCube(reverseNumber(i)):
                return i
    return None
# Main
if __name__ == "__main__":
    result = findThreeDigitPrime()
    if result is not None:
        print(result)