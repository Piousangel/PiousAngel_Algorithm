def fibo(n):
    if n <= 1:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input())
for i in range(n):
    dic = {}
    dic[1] = 0
    dic[0] = 0
    number = int(input())
    temp = fibo(number)
    print(f'{dic.get(0)} {dic.get(1)}')