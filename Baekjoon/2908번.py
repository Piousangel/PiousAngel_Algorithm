num1, num2 = map(int, input().split())

s1 = str(num1)
s2 = str(num2)
s11 = ""
s22 = ""
for i in range(0, len(s1)):
    s11 += s1[len(s1)-1-i]

for i in range(0, len(s2)):
    s22 += s2[len(s2)-1-i]

s1 = int(s11)
s2 = int(s22)

if s1 > s2 :
    print(s1)
else :
    print(s2)