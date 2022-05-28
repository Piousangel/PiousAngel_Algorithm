import sys
sys.stdin = open('sample.txt')
open = sys.stdin.readline

n = int(input())


for i in range(n):
    stack = []
    temp_list = list(input())

    for k in temp_list :
        if len(stack) == 0 :
            if k == '(' :
                stack.append(k)
            else :
                stack.append(k)
                break
        else:
            if k == '(' :
                stack.append(k)
            elif stack[-1] == '(' and k == ')':
                stack.pop()

    # print("stack :" , stack)
    if len(stack) == 0 :
        print("YES")
    else:
        print("NO")