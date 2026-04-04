import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[False] * m for _ in range(n)]

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

r, c = 0, 0 # 시작 위치
dt = 0 # 현재 방향 
cnt = 0 # 꺾은 횟수
graph[r][c] = True 
visited_count = 1 # 방문한 칸의 수 

while visited_count < m * n:

    nr, nc = r + dr[dt][0], c + dr[dt][1] 
    
    # 숫자가 이미 차있거나, 그래프 밖이면, 회전 (시계방향)
    if not (0 <= nr < n and 0 <= nc < m) or graph[nr][nc]:
        dt = (dt + 1) % 4
        cnt += 1
        nr = r + dr[dt][0] 
        nc = c + dr[dt][1]

    r, c = nr, nc
    graph[r][c] = True 
    visited_count += 1


print(cnt)