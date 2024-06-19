def reverse_number(n):
    """Reverse the digits of a number."""
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
    return reversed_n

