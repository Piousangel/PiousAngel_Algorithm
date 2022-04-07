import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

n_list = list(map(int, input().split()))


max_v = max(n_list)
min_v = 1

while max_v >= min_v : 
    total = 0
    mid_v = (max_v + min_v) // 2

    for i in range(len(n_list)):
        if n_list[i] > mid_v :
            total += n_list[i]- mid_v

    if total > M :
        # min_v = mid_v
        # mid_v = (max_v + min_v) // 2
        mid_v += 1

    elif total < M :
        # max_v = mid_v
        # mid_v = (max_v + min_v) // 2
        mid_v += 1

print(mid_v)


 