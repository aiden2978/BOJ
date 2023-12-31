import sys

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

N = int(sys.stdin.readline())
tree = {}
for _ in range(N):
    root, left, right = map(str, sys.stdin.readline().strip().split( ))
    # tree라는 딕셔너리에 tree[루트] = [왼쪽 자식, 오른쪽 자식] 형태로 저장
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')