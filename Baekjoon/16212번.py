import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n  = int(input())

n_list = list(map(int, input().split()))
n_list.sort()
for num in n_list :
    print(num, end= " ")