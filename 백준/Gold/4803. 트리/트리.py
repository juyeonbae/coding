import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break 
        
    # 양방향 트리 만들기
    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * (n+1)
    def dfs(node, parent):
        visited[node] = True
        is_tree = True

        for child in tree[node]:
            # 1. 방문 안 한 정점이면 계속 탐색 
            if not visited[child]:
                if not dfs(child, node):
                    is_tree = False

            # 2. 방문한 정점 & 부모 정점이 아니면 사이클 
            elif child != parent:
                is_tree = False

        return is_tree

    tree_count = 0 
    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i, 0):
                tree_count += 1

    if tree_count == 0:
        print("Case " + str(case) + ": No trees.")
    elif tree_count == 1:
        print("Case " + str(case) + ": There is one tree.")
    else:
        print("Case " + str(case) + ": A forest of " + str(tree_count) + " trees.")

    case += 1