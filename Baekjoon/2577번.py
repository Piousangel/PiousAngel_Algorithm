import sys

sum = 1
for i in range(3) :
    sum = sum * int(sys.stdin.readline())

n_list = list(str(sum))
        
for i in range(0,10) :
    cnt = 0
    for j in range(len(n_list)) :
        if(i == int(n_list[j])) :
            cnt = cnt+1
    print(cnt)


# total = 1
# for i in range(3):
#     total *= int(input())

# n_list = list(str(total))
# c_list = [0 for i in range(0,10)]

# for s in n_list :
#     c_list[int(s)] += 1

# for i in c_list:
#     print(i)