import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v = int(input())

tree = [[] for _ in range(v+1)]
for _ in range(v):
    s = list(map(int, input().split()))
    root = s[0]  # root node

    for i in range(1, len(s)-1, 2):
        tree[root].append((s[i], s[i+1]))

def dfs(node, dist, visited):
    visited[node] = True

    far_node = node
    max_dist = dist

    for child, weight in tree[node]:
        if not visited[child]:
            curr_node, curr_dist = dfs(child, dist+weight, visited)

            if max_dist < curr_dist:
                max_dist = curr_dist
                far_node = curr_node 

    return far_node, max_dist


visited = [False] * (v+1)
A, _ = dfs(1, 0, visited)

visited = [False] * (v+1)
_, B = dfs(A, 0, visited)
print(B)