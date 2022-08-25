import sys
sys.stdin = open('sample.txt')

input = sys.stdin.readline

# A가 항상 루트 노드 
# 노드, 왼, 오른쪽 자식 순
# 다시
n = int(input())

graph = {}

for i in range(n) :
    root, left, right = map(str, input().split())

    graph[root] = [left, right]


def preorder(root) :
    if root != '.' :
        print(root, end='')
        preorder(graph[root][0])
        preorder(graph[root][1])
    
def postorder(root) :
    if root != '.' :
        postorder(graph[root][0])
        postorder(graph[root][1])
        print(root, end='')

def inorder(root) :
    if root != '.' :
        inorder(graph[root][0])
        print(root, end='')
        inorder(graph[root][1])

ch = 'A'
preorder(ch)
print()
inorder(ch)
print()
postorder(ch)