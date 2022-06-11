import sys
from collections import deque
input = sys.stdin.readline

n, s = map(int, input().split())

n_list = list(map(int, input().split()))
answer = sys.maxsize

def search(n_list, s) :
    global answer
    q = deque()
    
    q.append(n_list[0])
    idx = 0
    total = n_list[0]

    while q :
        if idx == len(n_list)-1:
            while q:  #마지막 인덱스까지 왔으면 앞에거 빼주면서 s보다 큰거 있는지 chk 
                if total >= s :
                    answer = min(answer, len(q))
                total -= q.popleft()
             
            break

        if total < s :
            idx += 1
            total += n_list[idx]
            q.append(n_list[idx])
        else:
            answer = min(answer, len(q))
            total -= q.popleft()
           

search(n_list, s)

if answer == sys.maxsize :
    print(0)
else:
    print(answer)