import sys
sys.stdin = open('sample.txt')

input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))
cal_list = list(map(int, input().split()))

def dfs(total, n_list, plus, minus, mul, div, idx) :
    global max_num, min_num

    if idx == len(n_list) :
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return

    if plus > 0 :
        
        dfs(total + n_list[idx], n_list, plus - 1, minus, mul, div, idx + 1)
    if minus > 0 :
        dfs(total - n_list[idx], n_list, plus, minus - 1, mul, div, idx + 1)
    if mul > 0 :
        dfs(total * n_list[idx], n_list, plus, minus, mul - 1, div, idx + 1)
    if div > 0 :
        dfs( int(total / n_list[idx]), n_list, plus, minus, mul, div - 1, idx + 1)

min_num = sys.maxsize
max_num = - sys.maxsize

dfs(n_list[0], n_list, cal_list[0], cal_list[1], cal_list[2], cal_list[3], 1)

print(max_num)
print(min_num)
# import sys
# sys.stdin = open('sample.txt')
# input = sys.stdin.readline

# # 첫줄 수의 개수
# # 2개 숫자
# # + - x / 순으로 나옴
# n = int(input())
# n_list = list(map(int, input().split()))
# plus, minus, mul, div = map(int, input().split())

# print(plus, minus, mul, div)

# def dfs(total, n_list, plus, minus, mul, div, idx) :
#     global max_num, min_num

#     if idx == len(n_list) :
#         max_num = max(max_num, total)
#         min_num = min(min_num, total)
#         return

#     if plus > 0 :
#         dfs(total + n_list[idx], n_list, plus - 1, minus, mul, div, idx+1)
#     if minus > 0 :
#         dfs(total - n_list[idx], n_list, plus, minus - 1, mul, div, idx+1)
#     if minus > 0 :
#         dfs(total * n_list[idx], n_list, plus, minus, mul - 1, div, idx+1)
#     if div > 0 :
#         dfs(int(total / n_list[idx]), n_list, plus, minus, mul, div - 1, idx+1)
    

# max_num = -sys.maxsize - 1
# min_num = sys.maxsize
# dfs(n_list[0], n_list, plus, minus, mul, div, 0)


# print(max_num)
# print(min_num)

