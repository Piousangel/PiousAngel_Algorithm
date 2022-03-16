str1 = ""
for i in range(8):
    for j in range(8):
        str1 += input()
odd = 1
cnt = 0
for ch in str1:
    if(odd %2 == 0):
        if ch == 'F':
            cnt += 1
    odd += 1
                
print(cnt)