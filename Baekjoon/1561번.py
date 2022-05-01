import sys
import copy
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
wait_list = list(map(int, input().split()))

if N <= len(wait_list) :
    # print(wait_list[N-1])
    N = wait_list.index(wait_list[N-1])
    print(N)

else:
    copy_list = copy.deepcopy(wait_list)
    wait_list.sort()

    left_value = 0
    right_value = wait_list[-1] * N
    answer = 0
    real_idx = 0
    # print(wait_list)
    
    while left_value <= right_value :

        mid_vlaue = (left_value + right_value) // 2
        total = 0
        idx = 0
        print(mid_vlaue, end=" ")
        for i in range(M):
            
            # print(mid_vlaue // wait_list[i], end=" ")

            q = deque()

            for i in range(M):
                q.append(i)

            while q:
                for i in range(M):
                    

            total += mid_vlaue // wait_list[i]   # 1 2 3 4 5
            if total == N :
                idx = wait_list[i]

        print(" ")
        # print("mid", mid_vlaue)
        # print("answer", answer)
        # print("total", total)
        if total < N :
            left_value = mid_vlaue + 1
        else:
            right_value = mid_vlaue - 1
            answer = mid_vlaue
            real_idx = idx
    # print(answer)
    # print(real_idx)