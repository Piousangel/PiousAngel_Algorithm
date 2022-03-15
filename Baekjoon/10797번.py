n = int(input())
cnt = 0
n_list = list(map(str, input().split()))

for str1 in n_list:
    if str1[0:1] == str(n):
        cnt +=1         
print(cnt)