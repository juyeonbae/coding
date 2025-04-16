import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 로봇 좌표(r, c)와 방향 d
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 0: 북, 1: 동, 2: 남, 3: 서
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
visited[r][c] = True  # 현재 위치 청소 표시

while True:
    # 청소되지 않은 빈 칸 찾기
    cleaned = False
    
    # 네 방향 확인
    for _ in range(4):
        # 반시계 방향으로 90도 회전
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]
        
        # 범위 내이고, 빈 칸이며, 청소되지 않은 경우
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = True  # 청소 표시
            r, c = nr, nc  # 한 칸 전진
            cleaned = True
            break
    
    # 네 방향 모두 청소가 되어있거나 벽인 경우
    if not cleaned:
        # 후진
        nr, nc = r + dr[(d + 2) % 4], c + dc[(d + 2) % 4]
        
        # 후진할 수 있는 경우 (벽이 아닌 경우)
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
            r, c = nr, nc  # 한 칸 후진
        else:
            # 후진할 수 없는 경우 작동 중지
            break

# 방문 표시된 칸(청소된 칸)의 개수 세기
answer = sum(row.count(True) for row in visited)
print(answer)