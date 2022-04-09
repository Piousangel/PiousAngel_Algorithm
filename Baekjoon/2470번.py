n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

# left_v = n_list[0]
# right_v = n_list[-1]
# mid_v = n_list[(len(n_list)-1)//2]
# temp_answer = abs(right_v - left_v)

answer = [0,0]

def dfs(n_list, left_idx, right_idx, tmp_answer) :
    global answer

    if abs(left_idx - mid_idx) == 1 or abs(right_idx - mid_idx) == 1 :
        return

    left_value = n_list[left_idx]
    right_value = n_list[right_idx]
    # print(left_value, right_value, tmp_answer, abs(left_value+ right_value))
    mid_idx = (right_idx + left_idx) // 2
   
    if tmp_answer > abs(right_value + left_value):
        answer[0] = left_value
        answer[1] = right_value

    dfs(n_list, (left_idx+mid_idx)//2, right_idx, min(abs(right_value+left_value), tmp_answer))
    dfs(n_list, left_idx, (right_idx+mid_idx)//2, min(abs(right_value+left_value), tmp_answer))

dfs(n_list, 0, len(n_list)-1, 100000001)

print(answer[0], answer[1])

