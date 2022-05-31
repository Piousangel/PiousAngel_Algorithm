import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# 벽 or 자신과 부딪히면 끝남
# 1행 1열 부터 시작함
n = int(input()) #보드 크기

board = [[0]* n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
m = int(input())

rotation = [ (0,1), (1,0), (0,-1), (-1,0) ]
# 
for i in range(m) :
    a, b = map(int, input().split())
    board[a-1][b-1] = 3

k = int(input())

rotation_info = []
for i in range(k):
    a, b = map(str, input().split())
    rotation_info.append([a,b])


def bfs(board, visited, rotation_info) :
    global time
    q = deque()
    q.append([0,0])
    visited[0][0] = True 
    idx = 0
    time = 0
    while q :
        
        y, x = q.popleft()
        print(y,x)
        for info in rotation_info :
            if int(info[0]) - 1 == time :
                if info[1] == 'L' :
                    if idx == 0 :
                        idx = 3
                    else:
                        idx -= 1
                    break
                else:  #D
                    idx = (idx + 1) % 4
                    break
        print("idx", idx)
        nx = x + rotation[idx][1]
        ny = y + rotation[idx][0]
        
        if 0 <= nx < len(board) and 0 <= ny < len(board) :
            if visited[ny][nx] != True and board[ny][nx] == 3 :
                time += 1
                board[ny][nx] = 0
                visited[ny][nx] = True
                q.append([ny, nx])
            elif visited[ny][nx] != True and board[ny][nx] == 0 :
                time += 1
                visited[y][x] = False
                visited[ny][nx] = True
                q.append([ny, nx])
                
            

time = 0
bfs(board, visited, rotation_info)
print(time)
# print(board)
# print(rotation_info)




# input = sys.stdin.readline

# N = int(input())
# A = int(input())

# board = [[0 for i in range(N)] for _ in range(N)]
# visited = [ [False]*N for _ in range(N)]
# # print(visited)
# # print(board)
# if A != 0:
#     for i in range(A):
#         y, x = map(int, input().split())
#         board[y-1][x-1] = 1

# R = int(input())
# rotation_info = []
# move_info = [ [0,1], [1,0], [0,-1], [-1,0] ]  #인덱스0 -> y, 인덱스 1 -> x
# for i in range(R):
#     num, alpa = map(str, input().split())
#     rotation_info.append([num, alpa])

# # print("rotation_info", rotation_info)
# answer = 0

# def bfs(board, visited):
#     global answer
#     q = deque([])
#     visited_q = deque([])
#     q.append([0,0,0,0])     #마지막은 시간
#     visited[0][0] = True
#     visited_q.append([0,0])

#     while q :
#         y, x, time, info = q.popleft()  #y,x축, 시간, 로테이션 정보
        
#         flag = True
#         for i in range(len(rotation_info)) :
#             rot = rotation_info[i]
#             if time == int(rot[0]) :
#                 flag = False
#                 if rot[1] == 'D' :
#                     #오른쪽 90도 회전
#                     info += 1
#                     if info == 4:
#                         info = 0
#                     ny = y + move_info[info][0]
#                     nx = x + move_info[info][1]
#                     # time += 1
#                     break
#                 elif rot[1] == 'L':
#                     #왼쪽 90도 회전
#                     info  -= 1
#                     if info == -1:
#                         info = 3
#                     ny = y + move_info[info][0]
#                     nx = x + move_info[info][1]
#                     # time += 1
#                     break          
#         if flag:
#             ny = y + move_info[info][0]
#             nx = x + move_info[info][1]

#         answer = time+1
    
#         # print(y, x, time, info)
#         # print(visited_q)
#         if 0 <= ny < N and 0 <= nx < N :
#             if visited[ny][nx] != True and board[ny][nx] == 1 :
#                 visited[ny][nx] = True
#                 board[ny][nx] = 0
#                 visited_q.append([ny,nx])
#                 q.append([ny,nx,time+1, info])
#             elif visited[ny][nx] != True and board[ny][nx] == 0 :
#                 visited[ny][nx] = True
#                 visited_q.append([ny,nx])
#                 chkY, chkX = visited_q.popleft()
#                 # print("ggggg",chkY, chkX)
#                 visited[chkY][chkX] = False
#                 q.append([ny,nx,time+1, info])
        
#         else:
#             return      
          
# bfs(board, visited)

# print(answer)