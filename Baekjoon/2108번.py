import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
    
def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]
    
    modes = []
    for num in order:
        if num[1] == miximum:
            modes.append(num[0])
    return modes
    
n_list = []
sum = 0
for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    sum += temp
    n_list.append(temp)

n_list.sort()
modes = modefinder(n_list)
modes.sort()

print(round(sum/n))
print(n_list[(len(n_list)-1)/2])
print(modes[len(modes)-2][0])
print(max(n_list) - min(n_list))