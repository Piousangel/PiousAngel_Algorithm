import sys

n = int(sys.stdin.readline())

for i in range(n):
    n_str = list(sys.stdin.readline())
    sum = 0
    plus = 1
    for j in range(len(n_str)):
        if n_str[j] == 'O':
            sum = sum + plus
            plus = plus + 1
        else :
            plus = 1
            
    print(sum)