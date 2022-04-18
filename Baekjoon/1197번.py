import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

V, E = map(int, input().split())

sp_list = []
chk_list = [ i for i in range(V+1)]

for i in range(E) :

    A, B, C = map(int, input().split())

    sp_list.append([A,B,C])

sp_list.sort(key = lambda x : x[2])

def dfs(node) :

    if node != chk_list[node] :
        node = dfs(chk_list[node])
    return node

answer = 0

for arr in sp_list :              #순서대로 가면서 

    f_node = dfs(arr[0])
    s_node = dfs(arr[1])

    if f_node != s_node :

        if f_node < s_node :
            chk_list[s_node] = f_node
        else:
            chk_list[f_node] = s_node
        answer += arr[2]
    
print(answer)