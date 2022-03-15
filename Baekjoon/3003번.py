c_list = [1,1,2,2,2,8]
n_list = list(map(int, input().split()))
    
for i in range(len(c_list)):
    print(c_list[i] - n_list[i], end=' ')