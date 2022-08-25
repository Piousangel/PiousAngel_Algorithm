import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline
temp_str = list(map(str, input().rstrip()))

stack = []

for ch in temp_str :

    stack.append(ch)

    if len(stack) > 3 :

        if stack[-4] + stack[-3] + stack[-2] + stack[-1] == 'PPAP' :
            for i in range(3) :
                del stack[-1]

if len(stack) == 1 and stack[-1] == 'P' :
    print("PPAP")
else:
    print("NP")