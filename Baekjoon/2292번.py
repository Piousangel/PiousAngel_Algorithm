# 1 
# 7 +6
# 19 + 12
# 37 + 18
# 61 + 24

n = int(input())
    
basic = 1
cnt = 1
    
while n > basic:
    basic += cnt*6
    cnt += 1
        
print(cnt)


