import sys

N, M = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

max_v = max(n_list)
min_v = 0

while max_v >= min_v : 
    mid_v = (max_v + min_v) // 2
    total = 0
    for n in n_list:
        if n > mid_v :
            total += n - mid_v

    if total >= M :
        min_v = mid_v + 1
    else :
        max_v = mid_v -1

print(max_v)