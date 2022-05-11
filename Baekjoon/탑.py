import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())
stack = []
n_list = []
answer_list = []

for i in range(n):
    n_list = list(map(int, input().split()))

for i in range(n) :
    if len(stack) == 0 :
        stack.append(n_list[i])
        answer_list.append(i)
    else:
        if stack[-1] <= n_list[i] :
            idx = len(stack) -1
            while idx > 0 :
                if stack[idx] >= n_list[i] :
                    answer_list.append(stack[idx])
                    break
                idx -= 1
            stack.append(n_list[i])
        else:
            answer_list.append(stack[-1])
            stack.append(n_list[i])