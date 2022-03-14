n = int(input())

n_list = [[0 for _ in range(2)] for _ in range(n)]

for i in range(n):
    x,y = map(int, input().split())
    n_list[i][0] = y
    n_list[i][1] = x
    
n_list.sort()
        
for i in range(n):
    print(f'{n_list[i][1]} {n_list[i][0]}')