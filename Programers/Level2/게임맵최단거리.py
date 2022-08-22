from collections import deque

def solution(maps):
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    row = len(maps)
    col = len(maps[0])
    
    visited = [ [-1 for i in range(col)] for _ in range(row)]    
    
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    
    while q :
        
        y, x = q.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < col and 0 <= ny < row :
                if maps[ny][nx] == 1 and visited[ny][nx] == -1 :
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny,nx])
        
    answer = visited[-1][-1]
    
    return answer