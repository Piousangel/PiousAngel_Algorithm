import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
if n < m :
    print(n)
else:
    left = 0
    right = sys.maxsize
    t = None

    while left <= right :
        mid = (left + right) // 2
        cnt = m

        for i in range(m) :
            cnt += mid // n_list[i]
        if cnt >= n :
            t = mid
            right = mid - 1
        else:
            left = mid + 1
    
    #기본 들어가는 사람 + ~
    cnt = m
    for i in range(m) :
        cnt += (t-1) // n_list[i]

    # t에 탑승한 아이 계산
    for i in range(m):
        if t % n_list[i] == 0 :  #마지막에 들어가는 사람
            cnt += 1
        if cnt == n :
            print(i+1)
            break