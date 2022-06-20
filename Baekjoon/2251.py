import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n_list = list(map(int, input().split()))
answer = []

def dfs(bottle1, bottle2, bottle3, n_list) :
    global answer

    if bottle1 == 0 :
        answer.append(a)
    
    for i in range(3) :
        if bottle1 >= bottle2 :
            



dfs(0, 0, n_list[-1], n_list)