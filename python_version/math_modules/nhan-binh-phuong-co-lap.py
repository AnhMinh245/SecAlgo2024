""" Viết chương trình của thuật toán nhân bình phương có lặp tính a^k mod n:
(1). Đặt b <- 1 .Nếu k = 0 thì Return (b) 
(2). Đặt A <- a
(3). Nếu k0 = 1 thì đặt b <- a 
(4). For i from 1 to t do:
    4.1. Đặt A <- A^2 mod n
    4.2. Nếu ki = 1 thì b <- A*b mod n
(5). Return (b)  """

def mod_exp(a, k, n):
    b = 1
    if k == 0:
        return b
    A = a
    k_bin = bin(k)[2:]  # Get the binary representation of k as a string
    print(k_bin)
    
    if k_bin[-1] == '1': # Check if the last digit of k is 1   
        b = a
        
    for i in range(1, len(k_bin)): # Loop through the binary representation of k
        A = (A * A) % n # Square A and take the modulo n
        if k_bin[-1 - i] == '1': # Check if the i-th digit of k is 1
            b = (A * b) % n
            
    return b

# Example usage:
a = 41
k = 101
n = 211
result = mod_exp(a, k, n)
print(f"{a}^{k} mod {n} = {result}")
