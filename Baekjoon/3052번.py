import sys

n_list = []

for i in range(10) :
    temp = int(sys.stdin.readline()) % 42
    if not temp in n_list :
        n_list.append(temp)
print(len(n_list))

# n_list.contains 이딴건 파이썬에 업써!