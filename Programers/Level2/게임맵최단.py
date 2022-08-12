from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    row = len(maps)
    col = len(maps[0])
    
    visited = [[-1 for _ in range(col)] for _ in range(row)]
    visited[0][0] = 1
    
    q = deque()
    q.append([0,0])
    
    while q :
        y, x = q.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < col and 0 <= ny < row :
                if visited[ny][nx] == -1 and maps[ny][nx] == 1 :
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny,nx])
                    
    return visited[-1][-1]