import sys

str1 = sys.stdin.readline().strip().upper()

s_list = list(set(str1))
c_list = []

for ch in s_list:
    cnt = str1.count(ch)
    c_list.append(cnt)

if c_list.count(max(c_list)) > 1:
    print('?')
else:
    max_idx = c_list.index(max(c_list))
    print(s_list[max_idx])


# str1 = sys.stdin.readline().strip().upper()
# s_list = list(str1)
# dict = {}

# for s in str1:
#     if s not in dict:
#         dict[s] = 1
#     else:
#         dict[s] += 1

# max_cnt = 0
# answer = 0

# for key, value in dict.items():
#     if max_cnt < value:
#         max_cnt = value
#         answer = key
#     elif max_cnt == value:
#         answer = '?'
            
# print(answer)