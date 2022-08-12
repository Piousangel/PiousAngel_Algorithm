import sys

sys.stdin = open('sample.txt')

n = int(input())
# graph = [ [] for _ in range(n)]

tree = {}

for i in range(n) :
    root, left, right = map(str, input().split())
    # graph[i].append([left, right])
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def postorder(root) :
    if root != '.' :
        preorder(tree[root][0])
        preorder(tree[root][1])
        print(root, end='')

def inorder(root) :
    if root != '.' :
        preorder(tree[root][0])
        print(root, end='')
        preorder(tree[root][1])

        
