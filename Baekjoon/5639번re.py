import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

idx = 0
tree = []
while True :
    node = input()
    if node == "":
        break
    node = int(node)
    tree.append(node)
    idx += 1

def dfs(start, end):

    if start >= end :
        return
    
    root = tree[start]
    idx = 0

    if tree[end-1] <= root : 
        dfs(start+1, end)
        print(root)
        return
    
    for i in range(start+1, end):
        if tree[i] > root :
            idx = i
            break

    dfs(start+1, idx)
    dfs(idx, end)
    print(root)     

dfs(0, len(tree))