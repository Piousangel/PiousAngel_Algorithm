import sys

n = int(sys.stdin.readline().rstrip())
idx = 1
floor = 1
left = 1
right = floor
while n > idx:
        if left == floor:
            floor +=1
            left = 1
            right = floor
        else:
            left += 1
            right -= 1
        idx += 1

print(f'{left}/{right}')

# n = int(input())
# cnt = 1
# flower = 1
# flag = True
# left = 1
# right = flower

# while flag:
#     if cnt == n :
#         flag = False
#         break
        
#     if left == flower:
#         left = 1
#         flower += 1
#     else:
#         left += 1
#         right -= 1
        
# print(left+"/"+right)