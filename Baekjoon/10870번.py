import sys

def fibo(n):
    if n <= 1:
        result = n
    else:
        result = fibo(n-1) + fibo(n-2)      
    return result
    
n  = int(sys.stdin.readline().rstrip())
print(fibo(n))