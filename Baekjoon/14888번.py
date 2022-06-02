import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N = int(input())

n_list = list(map(int, input().split()))
cal_list = list(map(int, input().split()))

def dfs(total, n_list, plus, minus, mul, div, idx) :
    global max_num, min_num

    if idx == len(n_list) :
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return

    if plus > 0 :
        dfs(total + n_list[idx], n_list, plus-1, minus, mul, div, idx+1)
    if minus > 0 :
        dfs(total - n_list[idx], n_list, plus, minus-1, mul, div, idx+1)
    if mul > 0 :
        dfs(total*n_list[idx], n_list, plus, minus, mul-1, div, idx+1)
    if div > 0 :
        dfs(int(total/n_list[idx]), n_list, plus, minus, mul, div-1, idx+1)

max_num = -1000001
min_num = 1000001
dfs(n_list[0], n_list, cal_list[0], cal_list[1], cal_list[2], cal_list[3], 1)
print(max_num)
print(min_num)