# count divisors of input number
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):  # from 1 to the square root of n
        if n % i == 0:  # check if i is a divisor of n
            if i * i == n:  # Count each pair of divisors.
                count += 1  # a*a = n
            else:
                count += 2  # a*b = n
    return count

def find_q_primes(N):  # read the input N
    q_primes = []  # Initialize an empty list for Q-primes.
    for i in range(1, N + 1):
        if count_divisors(i) == 4:  # Use count_divisors to check if a number is a Q-prime.
            q_primes.append(i)  # Add Q-primes to the list.
    return q_primes

if __name__ == "__main__":
    try:
        N = int(input("N = "))
        q_primes = find_q_primes(N)
        if q_primes:
            for qp in q_primes:
                print(qp)
        else:
            print("No")
    except ValueError:
        print("Nhap Sai!")
