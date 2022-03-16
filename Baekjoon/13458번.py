n = int(input())
n_list = list(map(int, input().split()))
boss, second = map(int, input().split())
total = 0

for i in range(n):
    if n_list[i] > 0:
        cnt = 1
        temp = n_list[i] - boss
        if temp <= 0:
            total += cnt
            continue
        if temp % second == 0:
            cnt += temp//second
        else:
            cnt += (temp//second) +1
        total += cnt
        
print(total)