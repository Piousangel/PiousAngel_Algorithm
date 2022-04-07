import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, C = map(int, input().split())

n_list = []

for i in range(N):
    n_list.append(int(input()))

n_list.sort()

max_value = n_list[0]
min_value = n_list[-1]
mid_value = n_list[(len(n_list)-1) // 2]

# print(max_value, mid_value , min_value)
answer = 0
left_v = mid_value - min_value
right_v = max_value - mid_value

if left_v > right_v:
    flag = True
else:
    flag = False

while True :

    left_v = mid_value - min_value
    right_v = max_value - mid_value

    if flag == True :


    if left_v > right_v :
        answer = right_v
        mid_value = n_list[(len(n_list)-1) // 2 - 1]
    
    else:
        answer = left_v
        mid_value = n_list[(len(n_list)-1) // 2 + 1]
        if flag == True :

