'''
Fibonacci Sequence
-	Problem: Write a recursive function that returns the nth number in the Fibonacci sequence.
-	Example Input: fibonacci(6)
-	Expected Output: 8

'''

def fibonacci(n):
    if n <= 0 : 
        return 0
    elif n == 1:
        return 1
    else:    
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))