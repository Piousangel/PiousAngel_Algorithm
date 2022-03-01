def solution(n):
    
    return fibo(n) % 1234567

def fibo(n) :

    if(n == 0) : return 0
    if(n == 1) : return 1
    
    return (fibo(n-2) + fibo(n-1)) % 1234567


# 시초나는거 알면서 재귀로 풀어봤습니다.