from collections import deque
import sys
input = sys.stdin.readline 
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()

# 2차원 배열에서 최대값 올바르게 찾기
mx = 0
for i in range(n):
    for j in range(n):
        mx = max(mx, grid[i][j])

def initialized_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            
def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]

def bfs(x, y, target):
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny) and grid[nx][ny] > target:
                visited[nx][ny] = True
                q.append((nx, ny))
    
ans = []
for target in range(0, mx):  # 0부터 시작하는 것이 더 안전합니다
    initialized_visited()
    area = 0 
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] > target:
                bfs(i, j, target)
                area += 1  # 여기로 이동: 연결 요소를 하나 찾을 때마다 증가
    ans.append(area)

print(max(ans) if ans else 0)  # 안전을 위해 빈 리스트 처리