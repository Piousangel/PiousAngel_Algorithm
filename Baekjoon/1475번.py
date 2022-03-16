str1 = input()

dic = {'9': 0 , '6': 0}

for x in str1:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1

temp = dic.get('9') + dic.get('6')

if temp%2 == 0:
    temp = temp//2
else:
    temp = temp//2 + 1
dic['6'] = temp
dic['9'] = temp
    
print(max(dic.values()))