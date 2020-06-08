from functools import lru_cache
import time

@lru_cache(maxsize = 1000)
def recursiveFibonacci(n):
    if type(n) != int:
        raise TypeError("Parameter must be a positive integer.")
    elif n < 1:
        raise ValueError("Parameter must be a positive integer.")
    
    if n <= 2:
        return 1 
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

start = time.time()
for i in range(1,501):
    print(str(i) + ": ", recursiveFibonacci(i))
end = time.time()
print(end - start)