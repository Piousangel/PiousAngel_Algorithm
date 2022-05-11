import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()

left = 0
right = n_list[-1]
mid = 0
answer = 0

while left <= right :

    mid = (left + right) // 2
    total = 0

    for tree in n_list :
        if tree > mid :
            total += tree - mid

    if total >= m :
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)