from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
parent[1] = -1

while q:
    x = q.popleft()

    for next in graph[x]:
        if parent[next] == 0:
            parent[next] = x
            q.append(next)

for i in range(2, n+1):
    print(parent[i])
