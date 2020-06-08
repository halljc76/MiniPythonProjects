import time # Check elapsed time for running function.

def fibonacci(n):
    start = time.time()
    
    # If parameter is not an integer.
    if type(n) != int:
        raise TypeError("Parameter must be a positive integer.")
        
    # If parameter is non-positive (< 1).
    if n < 1:
        raise ValueError("Parameter must be a positive integer.")
    
    # Function uses conventional sequence "1, 1, 2..." instead of "0, 1, 1..."
    # Thus, a parameter for the first or second term (n = 1 or 2) returns 1.
    elif n <= 2:
        return 1
    
    # Function invariants
    term_one = 1 
    term_two = 1 
    
    print(term_one)
    print(term_two)
    
    # Range to the n-2 term because the function already returns 2 terms
    # from a sequence of n. It must return the other n-2 terms.
    for i in range(1, n-2):
        sum = term_one + term_two
        print(sum)
        
        term_one = term_two
        term_two = sum
    end = time.time()
    
    # Elapsed time.
    print("Total time: ", end - start)

# Testing function
fibonacci(-1) # Invokes ValueError
fibonacci("three") # Invokes TypeError
fibonacci(1) # Equivalent to fibonacci(2), returns 1
fibonacci(1000) # Example of Valid Function Call
