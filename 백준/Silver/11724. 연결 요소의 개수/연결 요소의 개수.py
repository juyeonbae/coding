import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

tree = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n+1)
def dfs(node):
    visited[node] = True

    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            
# 트리 개수 
cnt = 0 
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)