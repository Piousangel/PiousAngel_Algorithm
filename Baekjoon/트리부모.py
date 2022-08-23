import sys

sys.stdin = open('sample.txt')

input = sys.stdin.readline

n = int(input())

graph = [ [] for _ in range(n+1) ]
visited = [False] * n+1

for i in range(n-1) :
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)



