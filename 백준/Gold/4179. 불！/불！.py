import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

fire = [[-1] * c for _ in range(r)]
dist = [[-1] * c for _ in range(r)]

fq = deque()
jq = deque() 

# 지훈이와 불이 난 위치 
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            jq.append((i, j))
            dist[i][j] = 0 

        if arr[i][j] == 'F':
            fq.append((i, j))
            fire[i][j] = 0

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 불의 이동 기록 
while fq:
    x, y = fq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if arr[nx][ny] != '#' and fire[nx][ny] == -1:
                fire[nx][ny] = fire[x][y] + 1
                fq.append((nx, ny))

# 지훈이 이동 확인
while jq:
    x, y = jq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            print(dist[x][y] + 1)
            exit()

        if arr[nx][ny] != '#' and dist[nx][ny] == -1:
            if fire[nx][ny] == -1 or dist[x][y] + 1 < fire[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                jq.append((nx, ny))

print("IMPOSSIBLE")