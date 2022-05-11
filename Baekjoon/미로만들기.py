import sys
from collections import deque
import heapq
sys.stdin = open('sample.txt')
input = sys.stdin.readline


dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())

board = []
visited = [[-1] *n for _ in range(n)]

for i in range(n):
    board.append(list(input().rstrip()))

# print(board)

def bfs(board, visited, idx) :

    q = deque()
    q.append(idx)

    while q :

        
    


bfs(board, visited, 0)