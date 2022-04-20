import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, target = map(int, input().split())

cnt_list = [[0] for _ in range(N)]
num_list = []
cnt_list.sort()

for i in range(N):
    # cnt_list.append([int(input())])
    num_list.append(int(input()))           #숫자를 넣고 그냥 DFS에서 추가하는게 나을려나?

def dfs(cnt_list, num_list, target) :
    global answer
    temp_total = 0
    cnt_total = 0
    for i in range(len(cnt_list)):
        temp_total += cnt_list[i][0] * num_list[i]  #모든 코인리스트의 코인들의 합
        

    if temp_total == target:
        answer.append(cnt_list)
        return
        # print(cnt_list, "+++++++++")
        # for i in range(len(cnt_list)):
        #     print(cnt_list[i][0], end = ' ')
        #     cnt_total += cnt_list[i][0]

        # answer.append(cnt_total)
    
    if temp_total > target:
        return

    for i in range(N):
        cnt_list[i][0] += 1
        dfs(cnt_list, num_list, target)

answer = []
dfs(cnt_list, num_list, target)
print(answer)
