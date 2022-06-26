import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# 큐브는 정육면체
# 한변의 길이는 2의 제곱
# n개의 줄에 큐브의 종류와 개수가 
# 큐브의 종류는 한변의 길이를 나타낼때 쓰는 2^i의 i다

length, width, height = map(int, input().split())

n = int(input())

info_list = []
for i in range(n) :
    w, cnt = map(int, input().split())
    info_list.append([2**w, cnt])

print(info_list)