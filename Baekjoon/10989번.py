import sys

n = int(sys.stdin.readline().rstrip())
n_list = [0] * 100001
nSet = set()
    
for i in range(n):
    n_list[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(n_list)):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)