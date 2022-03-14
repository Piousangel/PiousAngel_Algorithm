import sys

def fac(n):
    answer = 1
    if n > 0:
        answer = n * fac(n-1)
    return answer

n = int(sys.stdin.readline().rstrip())

print(fac(n))