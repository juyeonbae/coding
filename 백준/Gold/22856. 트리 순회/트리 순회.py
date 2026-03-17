import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    # 왼쪽, 오른쪽 어떻게 분류? 
    tree[a].append(b)
    tree[a].append(c)

def dfs(node):
    right = tree[node][1]
    if right == -1:
        return 0
    return 1 + dfs(right)
    
print(2 * (n-1) - dfs(1))