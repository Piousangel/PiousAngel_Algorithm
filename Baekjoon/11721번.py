str1 = str(input())
str2 = ""
for ch in str1:
    if len(str2) == 10:
        print(str2)
        str2 = ""           
    str2 += ch   
print(str2)