""" Câu 9. Viết chương trình đếm số số nguyên tố nhỏ hơn hoặc bằng N với N được nhập vào từ bàn 
phím. """

# count prime numbers less than or equal to n

def count_prime_numbers(n):
    if n < 2:
        return 0
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(n**0.5) + 1): # int(n**0.5) + 1: 2, 3, 4, ..., sqrt(n)
        if prime[i]: 
            for j in range(i*i, n+1, i): # i*i, i*i + i, i*i + 2i, ..., n
                prime[j] = False # mark all multiples of i as False
    return sum(prime)

# Main function
if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print(count_prime_numbers(N))
    
    
    
    
