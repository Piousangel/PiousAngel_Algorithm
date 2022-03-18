n, m = map(int, input().split())
box = [[0 for _ in range(m+1)] for _ in range(n+1)]

box[1][1] = 1
for y in range(1, n+1):
    for x in range(1, m+1):
        dx = x + 1
        dy = y + 1
        if 0 < dx <=m :
            box[y][dx] += box[y][x]
        if 0 < dy <= n:
            box[dy][x] += box[y][x]
        if 0 <dx <=m and 0 < dy <= n:
            box[dy][dx] += box[y][x]
            
print(box[-1][-1]%1000000007)