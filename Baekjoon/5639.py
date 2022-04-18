import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

preorder = []
while True :

    try:
        n = int(input())
        preorder.append(n)

    except:
        break


def postorder(start, end) :

    if start >= end :
        return

    root = preorder[start]

    if root >= preorder[end-1] :   # 루트가 가장 끝노드보다 크다? only 왼쪽
        postorder(start+1, end)    # 루트 빼고 다시 돌려
        print(root)
        return

    idx = 0
    for i in range(start, end) :
        if preorder[i] > root :
            idx = i
            break
    
    postorder(start+1, idx)
    postorder(idx, end)
    print(root)

root = preorder[0]
start = 0
end = len(preorder)
postorder(start, end)