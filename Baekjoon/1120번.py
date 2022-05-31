import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

str_list = list(map(str, input().split()))

answer = 0
print(str_list[0])
print(str_list[1])
for i in range(1, len(str_list[0])) :
    str1 = str_list[0][:i]
    str2 = str_list[0][i:]

    if str1 in str_list[1] :
        answer = max(len(str1), answer)
        print(str1)
    elif str2 in str_list[1] :
        print(str2)
        answer = max(len(str2), answer)

print(answer)