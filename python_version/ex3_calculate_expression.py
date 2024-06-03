from math_modules.find_divisors import *

if __name__ == "__main__":
    n = int(input("Enter N: "))
    k = count_prime_divisors(n) # số ước nguyên tố của n
    q = sum(prime_divisor for prime_divisor in find_prime_divisors(n)) # tổng của các ước nguyên tố của N
    p = sum(divisor for divisor in find_all_divisors(n)) # tổng các ước số của n
    s = count_divisors(n) # số ước nguyên tố của n
    
    print("List of divisors of " + str(n) + ": (" + str(s) + " numbers)")
    print(find_all_divisors(n))
    print("List of prime divisors of " + str(n) + ": (" + str(k) + " numbers)")
    print(find_prime_divisors(n))
    
    print("Caculate Expression: N + p + s - q - k = " + str(n) + " + " + str(p) + " + " + str(s) + " - " + str(q) + " - " + str(k) + " = " + str(n + p + s - q - k))
    
    
    

