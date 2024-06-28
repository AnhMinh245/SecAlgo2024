""" Câu 23. Viết chương trình in ra màn hình YES trong trường hợp tổng của các số nguyên tố trong 
khoảng [A, B] là cũng là một số nguyên tố và NO nếu ngược lại. Với A,B là hai số được nhập vào 
từ bàn phím. """
""" 
Pseudocode
1. Sieve of Eratosthenes:
- Initialize a boolean array is_prime of size B + 1
- Mark non-prime numbers in this array.
2. Check if a number is prime:
- Define is_prime_number(n) function to check if n is in the list of primes.
Count primes less than X:
- Define count_primes_less_than(X) function to count the number of primes less than X.
3. Main logic:
Iterate through each number in range [A,B].
- For each number, count the primes less than it.
- Check if the count is a prime.
- If true, increment the super prime count.
4. Print the result. """

