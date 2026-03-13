import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 1. 입력 받기 
n = int(input())
parents = list(map(int, input().split()))
delete_node = int(input())

# 2. 부모 -> 자식 트리 만들기 
tree = [[] for _ in range(n)] 
root = -1 
for i in range(len(parents)):
    if parents[i] == -1:
        root = i
    else: 
        parent = parents[i] 
        tree[parent].append(i)

# 3. 루트를 삭제하는 경우 
if root == delete_node:
    print(0)
    sys.exit()

# 4. 리프 개수 저장할 변수 
leaf_count = 0

# 5. DFS 함수 
def dfs(node):
    global leaf_count
    childs = []

    # 5-1. 살아있는 자식 개수 세기 
    for child in tree[node]:
        if child != delete_node:
            childs.append(child)

    # 리프 판단 
    if not childs:
        leaf_count += 1
        return 

    # 5-2. 자식들 DFS 탐색 
    for child in childs:
        dfs(child)

dfs(root)
print(leaf_count)