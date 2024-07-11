def int_to_word_array(num, w, t):
    mask = (1 << w) - 1
    word_array = [(num >> (i * w)) & mask for i in range(t)]
    return word_array

def word_array_to_int(word_array, w):
    num = sum(word << (i * w) for i, word in enumerate(word_array))
    return num

def multiprecision_addition(A, B, w, t):
    C = [0] * t
    e = 0
    
    e, C[0] = divmod(A[0] + B[0], 1 << w)
    for i in range(1, t):
        e, C[i] = divmod(A[i] + B[i] + e, 1 << w)
    
    return e, C

def main():
    # Example input
    a = int(input("Enter integer a: "))
    b = int(input("Enter integer b: "))
    w = int(input("Enter bit width w: "))
    t = int(input("Enter number of words t: "))
    
    # Convert integers to word arrays
    A = int_to_word_array(a, w, t)
    B = int_to_word_array(b, w, t)
    
    # Perform multiprecision addition
    e, C = multiprecision_addition(A, B, w, t)
    
    # Convert result back to integer
    c = word_array_to_int(C, w)
    
    # Print the results
    print("Resulting sum in word array format:", C)
    print("Resulting sum as an integer:", c)

if __name__ == "__main__":
    main()
