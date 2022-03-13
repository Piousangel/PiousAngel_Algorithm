from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    row_len = len(maps)
    col_len = len(maps[0])
    
    visited = [[-1 for _ in range(col_len)] for _ in range(row_len)]
    q = deque()
    q.append([0,0])
    
    visited[0][0] = 1
    
    while q:
        y,x = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= ny < row_len and 0 <= nx < col_len and maps[ny][nx] == 1:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x]+1
                    q.append([ny,nx])
                    
    answer = visited[-1][-1]
    return answer