# Câu 5. Viết chương trình tính tổng của các số nguyên tố nằm trong khoảng [A, B] với A, B nhập vào từ bàn phím

import math 

def sieve_of_eratosthenes_range(start, end): 
    if end < 2 or start > end:  # Nếu end nhỏ hơn 2 hoặc start lớn hơn end, hàm sẽ trả về một danh sách rỗng 
        return []               # vì không có số nguyên tố nào trong khoảng này.
    
    # Khởi tạo danh sách prime với True từ 0 đến end
    prime = [True] * (end + 1) 
    prime[0] = prime [1] = False # Đặt prime[0] và prime[1] là False vì 0 và 1 không phải là số nguyên tố.
    
    for p in range (2, int(math.sqrt(end)) + 1):
        # Nếu prime[p] là True, thì tất cả các bội số của p từ p*p đến end sẽ được đánh dấu là False 
        # vì chúng không phải là số nguyên tố.
        if prime[p]:
            for i in range (p * p, end + 1, p): 
                prime[i] = False
                
    # Tạo danh sách các số nguyên tố trong khoảng start đến end
    return [p for p in range (start, end + 1) if prime[p]]



if __name__ == "__main__":
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    prime_divisors = sieve_of_eratosthenes_range(A, B)
    print(sum(prime for prime in prime_divisors))