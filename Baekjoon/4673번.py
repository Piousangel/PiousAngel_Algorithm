def chk(n) :
    # sum = n
    # while n != 0:
    #     sum = sum + (n % 10)
    #     n = n/10
    n += sum(map(int, str(n)))
    return sum

setN = set()

for i in range(1,10001) :
    setN.add(chk(i))
        
for i in range(1,10001) :
    if i not in setN :
        print(i)