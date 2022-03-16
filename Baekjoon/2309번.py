n_list = []
a = 0
b = 0
total = 0
for i in range(9):
    temp = int(input())
    total += temp
    n_list.append(temp)

n_list.sort()
flag = True
for i in range(0, len(n_list)-1):
    for j in range(i+1, len(n_list)):
        if total - (n_list[i] + n_list[j]) == 100 :
            a = i
            b = j
            flag = False
            break
    if flag == False:
        break
        
del n_list[a]
del n_list[b-1]

for k in range(0, len(n_list)):
    print(n_list[k])

# n_list = []
# box = [0]*2
# visited = [0]*2
# total = 0
# for i in range(9):
#     n_list.append(int(input()))

# total = sum(n_list)

# def chkIdx(box):
#     for i in range(len(box)):
#         print(box[i])

# def dfs(n_list, box, visited, r, idx):
#     if(idx == r):
#         chkIdx(box)
#         return
    
#     for i in range(len(n_list)):
#         if visited[i] == 0:
#             visited[i] = 1
#             box[idx] = n_list[i]
#             dfs(n_list, box, visited, r, idx+1)
#             visited[i] = 0

# dfs(n_list,box, visited, 2, 0)