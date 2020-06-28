import time # Check elapsed time for running function.

def fibonacci(n):
    """Function to print out the first n-terms of the Fibonacci Sequence.
       This does not utilize the principles of recursion, as is common with Fibonacci algorithms."""
    
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
    
    print("1: ", term_one)
    print("2: ",term_two)
    
    # Range of n-2 terms because the function already returns 2 terms
    # from a sequence of n. It must return the other n-2 terms.
    # Note that n+1 - 3 + 2 = n - 2 + 2 = n, the length of the Fibonacci sequence.
    for i in range(3, n+1):
        sum = term_one + term_two
        print(str(i) + ": ", sum)
        
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
