n = list(input())
total = 0
str1 = ""
for x in n:
    total += int(x)
        
if total%3 != 0 or "0" not in n:
    print(-1)
else:
    n.sort(reverse = True)
    str1 = "".join(n)
    print(int(str1))