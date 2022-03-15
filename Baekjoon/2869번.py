A,B,V = map(int, input().split())

temp = (V-B)/(A-B)
print(int(temp) if temp == int(temp) else int(temp)+1)

# cnt = 1
# total = 0
# while V > 0:
#     V -= A
#     if V <= 0:
#         break
#     V += B
#     cnt += 1
    
# print(cnt)