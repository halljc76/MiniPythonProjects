import time 

def fibonacci(n):
    start = time.time()
    
    if type(n) != int:
        raise TypeError("Parameter must be a positive integer.")
    if n < 1:
        raise ValueError("Parameter must be a positive integer.")
    elif n <= 2:
        return 1
    
    term_one = 1 
    term_two = 1 
    
    print(term_one)
    print(term_two)
    
    for i in range(1, n-2):
        sum = term_one + term_two
        print(sum)
        
        term_one = term_two
        term_two = sum
    end = time.time()
    
    print("Total time: ", end - start)

fibonacci(1000)