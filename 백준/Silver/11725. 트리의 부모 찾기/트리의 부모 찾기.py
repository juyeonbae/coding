import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 1. 입력 받기 
n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (n+1)
parents[1] = -1 

# 2. dfs로 부모 노드 찾기 
def dfs(node):
    
    for child in tree[node]:
        if parents[child] == 0:
            parents[child] = node
            dfs(child)
        
# 2번 노드부터 부모 노드 출력 
dfs(1)
print('\n'.join(map(str, parents[2:])))