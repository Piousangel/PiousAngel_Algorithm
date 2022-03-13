str1 = input()
alph = 'abcdefghijklmnopqrstuvwxyz'
    
for ch in alph:
    if ch in str1:
        print(str1.index(ch), end=" ")
    else:
        print(-1, end=" ")


# cStr = input()
# charBox = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# for x in charBox:
#     print(cStr.find(x))

# import sys

# cStr = str(sys.stdin.readline().strip())
# charBox = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# for ch in range(charBox):
#     if ch in cStr :
#         print(cStr.index(ch), end=" ")
#     else:
#         print(-1, end=" ")