""" Câu 32. Áp dụng các thuật toán đã được học em hãy cài đặt chương trình giải bài toán mô 
phỏng cách mã và giải mã của hệ mật RSA như sau:
- Tìm số nguyên số p, q (trong đó 100 < p, q < 500)
- Tính n = p.q; phi(n) = (p – 1) (q – 1) 
- Chọn e (1<e< phi(n)) là số nguyên tố cùng nhau với phi(n) (gcd(e, phi(n)) = 1) và tính d = e^-1 mod (n)
- Tính bản mã c của thông điệp m, với m = SBD (nhập từ bàn phím) + 123, c = m^e mod n
- Giải mã thông điệp, tính m = c^d mod n  """

import random

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m): # Extended Euclidean Algorithm
    m0, x0, x1 = m, 0, 1 
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# Function to generate a random prime number in the range (100, 500)
def generate_prime():
    while True:
        num = random.randint(101, 499)
        if isprime(num):
            return num

# RSA encryption and decryption
def rsa_encrypt_decrypt(SBD):
    # Step 1: Generate two prime numbers p and q
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()

    # Step 2: Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(e, phi_n) == 1:
            break

    # Step 4: Calculate d as the modular inverse of e modulo phi(n)
    d = mod_inverse(e, phi_n)

    # Step 5: Encrypt the message
    m = SBD # Original message 
    c = pow(m, e, n)

    # Step 6: Decrypt the message
    decrypted_message = pow(c, d, n)

    return p, q, n, phi_n, e, d, m, c, decrypted_message

# Input SBD from the user
SBD = int(input("Enter your SBD: "))
p, q, n, phi_n, e, d, m, c, decrypted_message = rsa_encrypt_decrypt(SBD)

print(f"p = {p}")
print(f"q = {q}")
print(f"n = {n}")
print(f"phi(n) = {phi_n}")
print(f"e = {e}")
print(f"d = {d}")
print(f"Original message (m) = {m}")
print(f"Encrypted message (c) = {c}")
print(f"Decrypted message = {decrypted_message}")
