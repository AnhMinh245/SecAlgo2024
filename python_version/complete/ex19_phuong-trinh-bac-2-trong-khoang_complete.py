""" Câu 19. Viết chương trình in ra các số nguyên dương x nằm trong khoảng [m,l] sao cho giá trị
của biểu thức 𝐴𝑥
2 + 𝐵𝑥 + 𝐶 là một số nguyên tố. Với A,B,C, m,l là các số nguyên nhập từ bàn 
phím (m<l). """


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_valid_x(A, B, C, m, l):
    valid_x = []
    for x in range(m, l + 1):
        value = A * x**2 + B * x + C
        if is_prime(value):
            valid_x.append(x)
    return valid_x

def main():
    A = int(input("Enter integer A: "))
    B = int(input("Enter integer B: "))
    C = int(input("Enter integer C: "))
    m = int(input("Enter integer m: "))
    l = int(input("Enter integer l: "))
    
    if m >= l:
        print("Invalid range: m should be less than l.")
        return
    
    valid_x = find_valid_x(A, B, C, m, l)
    
    if valid_x:
        print(f"Positive integers x in the range [{m}, {l}] such that {A}x^2 + {B}x + {C} is prime are: {valid_x}")
    else:
        print(f"No positive integers x in the range [{m}, {l}] make the expression {A}x^2 + {B}x + {C} prime.")

if __name__ == "__main__":
    main()

