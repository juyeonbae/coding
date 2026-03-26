import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]

k = 0 
q = deque([(0, 0, 0)])
dist[0][0][0] = 1 # 시작 칸도 포함해서 센다. 

while q:
    x, y, wall = q.popleft()

    # 종료 조건 
    if x == n-1 and y == m-1:
        print(dist[x][y][wall])
        exit()

    for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            # 1. 다음 칸이 0이고 방문 안 했을 때
            if arr[nx][ny] == 0 and dist[nx][ny][wall] == -1:
                dist[nx][ny][wall] = dist[x][y][wall] + 1
                q.append((nx, ny, wall))

            # 2. 다음 칸이 벽이고, 아직 벽을 부순 적이 없을 때 
            elif arr[nx][ny] == 1 and wall == 0:
                # 벽을 부순 상태(1)로 이동 기록
                if dist[nx][ny][1] == -1:
                    dist[nx][ny][1] = dist[x][y][wall] + 1
                    q.append((nx, ny, 1))

print(-1)