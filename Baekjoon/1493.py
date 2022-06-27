import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# 큐브는 정육면체
# 한변의 길이는 2의 제곱
# n개의 줄에 큐브의 종류와 개수가 
# 큐브의 종류는 한변의 길이를 나타낼때 쓰는 2^i의 i다

l, w, h = map(int, input().split())

n = int(input())

info_list = []
for i in range(n) :
    w, cnt = map(int, input().split())
    info_list.append([2**w, cnt])

def dfs(l, w, h, info_list) :


    for info in info_list :
        info[0]
        info[1]
        #l, w, h 중 하나가 배수의 역할을 한다면
         


    dfs(l//2, w//2, h//2, info_list)

dfs(l, w, h, info_list)