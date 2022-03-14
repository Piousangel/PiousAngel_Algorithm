import sys
n = int(sys.stdin.readline().rstrip())
    
s_list = set()   
for i in range(n):
    s_list.add(sys.stdin.readline().rstrip())

c_list = list(s_list)
c_list.sort()           #사전정렬
c_list.sort(key=len)    #길이정렬
for str1 in c_list:
    print(str1)