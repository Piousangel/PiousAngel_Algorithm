import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

n_list = []

visited = [False] * M

for i in range(N):
    n_list.append(int(input()))


def bfs(n_list, target, visited):
    global answer

    q = deque()

    for i in range(len(n_list)):
        if n_list[i] <= target :
            visited[target - n_list[i]] = True
            q.append([ n_list[i], target - n_list[i], 1])    #숫자랑 ,  타겟숫자 - 코인 , idx
    
    # print(len(q))
    if len(q) == 0 :
        answer = -1
        return
           
    # print(q)
    while q :

        now_coin, now_less, now_cnt = q.popleft()
        
        # print(now_coin, now_less, now_cnt)
        if now_less == 0 :
            # print(now_coin, now_less, now_idx, now_cnt)
            answer = min(now_cnt, answer)
            return 
        
        if now_coin < min(n_list) :
            answer = -1
            break
            
    
        for i in range(len(n_list)):
            if n_list[i] <= now_less and visited[now_less - n_list[i]] == False :
                visited[now_less - n_list[i]] = True
                q.append([ n_list[i], now_less - n_list[i], now_cnt+1])    
                
                
                #숫자랑 ,  타겟숫자 - 코인 , idx

        # if now_coin <= now_less :            #같은 코인 넣어주면서 증가
        #     q.append([n_list[now_idx], now_less - n_list[now_idx], now_idx, now_cnt+1])
        
        # elif now_coin > now_less and now_idx < len(n_list) - 1 :          #지금 인덱스가 마지막 인덱스 전 보다 작을 때  and now_less >= n_list[now_idx+1]
        #     tt = now_idx+1
        #     q.append([n_list[tt], now_less, tt, now_cnt])
        
    answer = -1

answer = 10000001


bfs(n_list, M, visited)


print(answer)