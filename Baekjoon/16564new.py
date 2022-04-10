N, T = map(int, input().split())

char_list = []
for i in range(N):
    char_list.append(int(input()))

char_list.sort()
answer = 0
left_value = char_list[0]
right_value = char_list[-1] + T

while left_value < right_value :

    mid_value = (right_value + left_value) // 2
    temp = 0

    for ch in char_list :
        if ch > mid_value :
            break
        temp += mid_value - ch

    if temp <= T :
        left_value = mid_value + 1
        answer = mid_value
    else:
        right_value = mid_value -1

print(answer)
    
    

