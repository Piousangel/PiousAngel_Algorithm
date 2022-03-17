n = int(input())
n_list = list(map(int, input().split()))
target = int(input())
dic = {}

for x in n_list:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
if dic.get(target) == None:
    print(0)
else :
    print(dic.get(target))