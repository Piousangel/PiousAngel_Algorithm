N, K = map(int, input().split())

def fac(n):
    answer = 1
    for i in range(2,n+1):
        answer *= i
    return answer

print(fac(N) // fac(K) // fac(N-K))