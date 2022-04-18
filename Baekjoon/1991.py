import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

tree = {}

for i in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]

# tree.sort(key = lambda x : x[0])

def preorder(root):

    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
        
def inorder(root) :

    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):

    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

root = 'A'
preorder(root)
print()
inorder(root)
print()
postorder(root)



# import sys
# sys.stdin = open('sample.txt')
# n = int(sys.stdin.readline().rstrip())

# tree = {}

# for n in range(n):
#     root, left, right = sys.stdin.readline().strip().split()
#     tree[root] = [left, right]
    
# def preorder(root):
#     if root != '.':
#         print(root, end='')
#         preorder(tree[root][0])
#         preorder(tree[root][1])
      
# def inorder(root):
#     if root != '.':
#         inorder(tree[root][0])
#         print(root, end='')
#         inorder(tree[root][1])
      
# def postorder(root):
#     if root != '.':
#         postorder(tree[root][0])
#         postorder(tree[root][1])
#         print(root, end='')
        
# ch = 'A'
# preorder(ch)
# print()
# inorder(ch)
# print()
# postorder(ch)


