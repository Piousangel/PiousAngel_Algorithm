n = int(input())
cnt = 0
  
for _ in range(n):
    str1 = input()
    c_list = []
    flag = True
    for i in range(len(str1)):
        if str1[i] not in c_list:
            c_list.append(str1[i])
        else:
            if str1[i-1] != str1[i]:
                flag = False
                break
    if flag:
        cnt +=1
        
print(cnt)