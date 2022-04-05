n = int(input())
n_list = list(input().split())
realcnt = 0
for i in range(len(n_list)):
    if int(n_list[i]) == 1 :
        continue
    cnt = 0
    for j in range(2, int(n_list[i])+1):
        if int(n_list[i]) % j == 0 :
            cnt += 1
    if cnt == 1:
        realcnt +=1
        
print(realcnt)