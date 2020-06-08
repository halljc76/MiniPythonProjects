from functools import lru_cache
import time

@lru_cache(maxsize = 1000)
def recursiveFibonacci(n):
    """Recursive implementation of Fibonacci Sequence.
       Function uses the "1,1,2..." version of the sequence."""
    
    if type(n) != int:
        raise TypeError("Parameter must be a positive integer.")
    if n < 1:
        raise ValueError("Parameter must be a positive integer.")
    
    elif n <= 2:
        return 1 
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

# Prints out first n-terms of Fibonacci Sequence.
start = time.time()
for i in range(1,501):
    print(str(i) + ": ", recursiveFibonacci(i))
end = time.time()
print(end - start)

# Testing function
fibonacci(-1) # Invokes ValueError
fibonacci("three") # Invokes TypeError
fibonacci(1) # Equivalent to fibonacci(2), returns 1
fibonacci(1000) # Example of Valid Function Call
