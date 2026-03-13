import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

# 간선은 N-1개뿐이라서 인접리스트로 저장한다. 
graph = [[] for _ in range(n+1)]
            
# x -> y까지 가는 길을 찾고 그 길의 가중치들을 더해야 한다. 
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# x에서 시작해서 y를 찾을 때까지 DFS/BFS
# 누적 거리 함께 들고 다니기 
def dfs(node, target, dist):
    if node == target:
        print(dist)
        return

    for next, w in graph[node]:
        if not visited[next]:
            visited[next] = True
            result = dfs(next, target, dist + w)

for _ in range(m):
    start, end = map(int, input().split())
    visited = [False] * (n+1)
    visited[start] = True
    dfs(start, end, 0)