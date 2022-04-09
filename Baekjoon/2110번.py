import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, C = map(int, input().split())

n_list = []

for i in range(N):
    n_list.append(int(input()))

n_list.sort()



left_v = n_list[0]
right_v = n_list[-1]
mid_v = n_list[(len(n_list)-1) // 2]

right_d = right_v - mid_v
left_d = mid_v - left_v
print(n_list)
# print(right_d)
# print(left_d)
answer = 0

if right_d >= left_d :
    while right_d >= left_d :

        # mid_v = n_list[ (n_list.index(right_v) + n_list.index(left_v)) // 2]

        left_d = mid_v - left_v
        right_d = right_v - mid_v
        print(right_d)
        print(left_d)   
        if right_d > left_d :
            right_v = n_list[n_list.index(mid_v)+1]
        else:
            left_v = n_list[n_list.index(mid_v)-1]
            answer = left_d
else:
    while right_d <= left_d :

        mid_v = n_list[ (n_list.index(right_v) + n_list.index(left_v)) // 2]

        left_d = mid_v - left_v
        right_d = right_v - mid_v

        if left_d > right_d :
            left_v = n_list[n_list.index(mid_v)-1]
        else:
            right_v = n_list[n_list.index(mid_v)+1]
            answer = right_d

print(answer)


