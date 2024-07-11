""" Câu 20. Viết chương trình in ra các cặp số (A,B) nằm trong khoảng (M,N) sao cho ước số chung 
lớn nhất của A và B có giá trị là một số D cho trước. Với M,N,D nhập vào từ bàn phím. (0<M,N, 
D < 1000) """

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_pairs(M, N, D):
    pairs = []
    for A in range(M, N + 1):
        for B in range(A, N + 1):
            if gcd(A, B) == D:
                pairs.append((A, B))
    return pairs

if __name__ == "__main__":
    M = int(input("Enter integer M: "))
    N = int(input("Enter integer N: "))
    D = int(input("Enter integer D: "))
    
    if M >= N or D >= 1000:
        print("Invalid input: M should be less than N and D should be less than 1000.")
    else:
        gcd_pairs = find_gcd_pairs(M, N, D)
        if gcd_pairs:
            print(f"Pairs (A, B) in the range ({M}, {N}) such that gcd(A, B) = {D} are: {gcd_pairs}")
        else:
            print(f"No pairs (A, B) in the range ({M}, {N}) have gcd(A, B) = {D}.")