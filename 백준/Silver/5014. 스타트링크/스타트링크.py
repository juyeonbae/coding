from collections import deque

# 총 층수 현재 위치, 목표 위치, 위로 가는 버튼, 아래로 가는 버튼
F, S, G, U, D = map(int, input().split())
grid = [0] * (F+1)
visited = [False] * (F+1)

q = deque()
q.append(S)
visited[S] = True

def can_go(x):
    return 0 < x <= F and not visited[x] 

def bfs():
    while q:
        x = q.popleft()
        for dx in [U, -D]:
            nx = x + dx
            if can_go(nx):
                q.append(nx)
                visited[nx] = True
                grid[nx] = grid[x] + 1

if S != G:
    bfs()

print(grid[G] if visited[G] else "use the stairs")