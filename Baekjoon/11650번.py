n = int(input())

n_list = [[0 for _ in range(2)] for _ in range(n)]

for i in range(n):
    x,y = map(int, input().split())
    n_list[i][0] = x
    n_list[i][1] = y
    
n_list.sort()
        
for i in range(n):
    print(f'{n_list[i][0]} {n_list[i][1]}')