import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, str1 = map(str, input().split())
str_list = []

for i in range(int(n)):
    str_list.append(input().rstrip())

# print(n)
# print(n_list)

temp = 0
answer = ""
for strs in str_list :

    idx = 0
    # cnt = 0
    flag = False
    for i in range(len(strs)):

        if strs[i] == str1[idx] :
            idx += 1

        if idx == 1 :
            # print(strs[:idx])
            if len(strs[:idx]) > 1 :
                flag = False
                break

        if idx == len(str1) :
            # print(len(strs[i:]))
            # print(strs[i+1:])
            if len(strs[i+1:]) > 1 :
                flag = False
                break
            else :
                # print(strs)
                flag = True
                break
        
    if flag :  
  
        if idx == len(str1) and temp < len(strs) :
            temp = len(strs)
            answer = strs

print(answer)




