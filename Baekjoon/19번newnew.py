import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, target = map(int, input().split())

n_list = []

for i in range(N):
          n_list.append([int(input()), 0])

# for test in cnt_list:
#     test[1] +=1

print(n_list)

si_list = [0,1,2,3,4,1,2,3,4,5,2,3,1,2,3,3,4]

def cal(n_list, target) :

    total = 0
    for node in n_list :
        total += node[1] * node[0]
        # print("total", total, "target :", target)

    


cal(n_list, target)