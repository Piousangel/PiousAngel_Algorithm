from collections import deque
from collections import deque
from http.client import OK
from signal import siginterrupt

def solution(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    r_len = len(maps)
    c_len = len(maps[0])
    visited = [[-1 for _ in range(c_len)]for _ in range(r_len)]
    visited[0][0] = 1
    
    q = deque()
    q.append([0,0])
    

    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(0 <= ny and ny < r_len and 0 <= nx and nx < c_len):
                if(maps[ny][nx] == 1 and visited[ny][nx] == -1):
                    visited[ny][nx] = visited[y][x] +1
                    q.append([ny,nx])
    
    answer = visited[r_len-1][c_len-1]
    
    return answer
    
# def solution(maps):
#     answer = 0
    
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     row_len = len(maps)
#     col_len = len(maps[0])
    
#     visited = [[-1 for _ in range(col_len)] for _ in range(row_len)]
#     q = deque()
#     q.append([0,0])
    
#     visited[0][0] = 1
    
#     while q:
#         y,x = q.popleft()
        
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
            
#             if 0 <= ny < row_len and 0 <= nx < col_len and maps[ny][nx] == 1:
#                 if visited[ny][nx] == -1:
#                     visited[ny][nx] = visited[y][x]+1
#                     q.append([ny,nx])
                    
#     answer = visited[-1][-1]
#     return answer


