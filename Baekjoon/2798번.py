import sys

a,b = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
answer = 0
    
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1, a):
            if n_list[i] + n_list[j] + n_list[k] > b:
                continue
            else:
                answer = max(answer, n_list[i] + n_list[j] + n_list[k])
print(answer)
