box = ['A','B','C','D','E']
for i in range(3):
    n_list = list(map(int,input().split()))
    cnt = 0
    for j in n_list:
        if j == 0:
            cnt +=1
    print(box[cnt-1])