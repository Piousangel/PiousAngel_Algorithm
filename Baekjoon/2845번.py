a, b = map(int, input().split())
temp = a*b

n_list = list(map(int, input().split()))

for i in range(len(n_list)):
    print(n_list[i]-temp, end=' ')