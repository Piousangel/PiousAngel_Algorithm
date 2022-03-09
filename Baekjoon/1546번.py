import sys

n = int(sys.stdin.readline())
maxN = 0
sum = 0
n_list = list(map(int, sys.stdin.readline().split()))
maxN = max(n_list)

for i in range(n):
    sum = sum + n_list[i]/maxN*100

print(sum/n)