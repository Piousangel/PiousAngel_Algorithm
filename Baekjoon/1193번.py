n = int(input())
cnt = 1
flower = 1
flag = True
left = 1
right = flower

while flag:
    if cnt == n :
        flag = False
        break
        
    if left == flower:
        left = 1
        flower += 1
    else:
        left += 1
        right -= 1
        
print(left+"/"+right)