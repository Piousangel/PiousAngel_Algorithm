import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

trees, lens = map(int, input().split())
tree_list = list(map(int, input().split()))
# print(sum(tree_list))
temp = sum(tree_list)// len(tree_list)

answer = 0

def dfs(tree_list, temp, halfAnswer) :
    global answer
    for i in range(len(tree_list)) :
        if tree_list[i] > temp :
            halfAnswer += tree_list[i] - temp
    
    if halfAnswer == lens :
        answer = temp
        return 
    elif halfAnswer > lens :
        dfs(tree_list, temp-1, 0)
    elif halfAnswer < lens :
        dfs(tree_list, temp+1, 0)

    return
     
dfs(tree_list, temp, 0)
print(answer)