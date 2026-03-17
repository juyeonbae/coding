import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    root, child, weight = map(int, input().split())
    # 그래프를 양방향으로 저장
    tree[root].append((child, weight))
    tree[child].append((root, weight))

def dfs(node, dist, visited):
    visited[node] = True

    far_node = node # 가장 먼 노드 번호
    max_dist = dist # 가장 먼 거리 

    for next, weight in tree[node]:
        if not visited[next]:
            c_node, c_dist = dfs(next, dist + weight, visited)

            # 더 먼 거리면 갱신
            if c_dist > max_dist:
                max_dist = c_dist
                far_node = c_node

    return far_node, max_dist

# 1번에서 가장 먼 노드 찾기
visited = [False] * (n+1)
A, _ = dfs(1, 0, visited)

# A에서 가장 먼 거리 찾기
visited = [False] * (n+1)
_, diameter = dfs(A, 0, visited)

print(diameter)