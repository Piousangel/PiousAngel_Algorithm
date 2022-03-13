str1 = input()
alph = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0

for s in str1:
    for i in range(0, len(alph)):
        if s in alph[i]:
            cnt += i+2
            break
                
print(cnt + len(str1))