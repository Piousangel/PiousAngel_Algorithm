import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline
n = int(input())

n_list = []
stack = []
for i in range(n) :
    n_list.append(int(input()))

for k in n_list :
    if len(stack) == 0 :
        stack.append(k)
    else :
        if stack[-1] > k :
            stack.append(k)
        else:
            while len(stack) > 0 :
                if stack[-1] <= k :
                    stack.pop()
                else:
                    break
            stack.append(k)

print(len(stack))