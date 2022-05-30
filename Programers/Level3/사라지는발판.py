# 플레이어 A와 B가 서로 게임을 합니다
# 양 플레이어가 캐릭터를 몇번 움직이게 될지 예측하려고 합니다
# 보드에는 발판이 있는 부분과 없는 부분이 있다
# 발판이 있는 곳에만 캐릭터가 서있을 수 있다. 처음 캐릭 -> 항상 발판 있음
# 발판 o, 보드 밖으로 이동 x
# 밟고 있던 발판은 캐릭터가 다른 곳으로 이동과 동시에 사라짐
# 양 플레이어는 상하좌우 인접한 4개의 칸 중에 발판이 있는 칸으로 옮겨야 합니다

# 움직일 차례 -> 움직일 발판 없거나 , 보드 밖인 경우
# 두 캐릭터가 같은 발판 위에 있을 때, 상대 플레이어의 캐릭터가 다른 발판으로 이동하여 자신의 캐릭터가
# 서있던 발판이 사라지게 되면 패배
# A가 먼저, 다들 최적의 플레이만 한다. 이길려면 빨리 이길려고, 질 것같은 사람은 최대한 뻐팅길려고
# 양 플레이어가 최적의 플레이를 했을 때, 두 캐릭터가 움직인 횟수의 합을 return 하도록 solution 함수를 완성하기
# 보드 수가 작은 것으로 보아 백트레킹인가,,,걍 BFS? 완탐느낌인뎅...

#다시 .... 5/31

from collections import deque

def bfs(board, visited, aloc, bloc, row, col) :
    global answer
    q = deque()
    cnt = 0
    # aloc.append(0)
    # bloc.append(0)
    q.append(aloc) # player A
    q.append(bloc) # player B
    #visited는 옮기고 나서 해주자 왜냐? A,B가 같은 발판을 밟을 수도 있기 때문
    
    while q :
        
        y, x = q.popleft()
        print("cnt", cnt)
        
        if visited[y][x] == True : #같은 곳에 있다 A가 다른 곳으로 이동했을 때
            break
            
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < col and 0 <= ny < row :
                if board[ny][nx] == 1 and visited[ny][nx] == False :
                    visited[y][x] = True  #이전 발판을 True로 바꿔준다
                    q.append([ny, nx])
                    cnt += 1
                    
    answer = min(answer, cnt)         
    
answer = 100001

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def solution(board, aloc, bloc):
    
    global answer
    row = len(board) 
    col = len(board[0])
    visited = [[False] * col for _ in range(row)]
    bfs(board, visited, aloc, bloc, row, col)

    return answer