import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

# ** 시간 초과 **
'''
시간복잡도 최적화) 
초기 빙산 위치를 리스트에 담기 
'''
icebergs = [(i, j) for i in range(n) for j in range(m) if ice[i][j] > 0]    

# 조건: 0이 저장된 칸의 개수만큼 높이 줄어듬 -> 4방향 확인
    # 0보다 작아지지는 않음 

# 1. 빙산 녹이기
    # 0이 아닌 칸에서 주변에 0이 몇 개 있는지 확인 
    # 주의할 점: 한 번에 녹이기 (녹아서 생긴 0이 반영될 수 있음)

'''
어떻게 한 번에 녹일 수 있을까? 
-> 새로운 배열을 만들어서 주변의 0 개수를 저장한다. 
배열 - 배열을 한다. 
'''
def melt(ice, icebergs):
    chk = [[0] * m for _ in range(n)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] 
    
    for i, j in icebergs:
        cnt = 0
        for dr in range(4):
            ni, nj = i + dx[dr], j + dy[dr]
            if 0 <= ni < n and 0 <= nj < m and ice[ni][nj] == 0:
                cnt += 1
        chk[i][j] = cnt 

    next_iceberges = []
                
    # 한 번에 녹이기
    for i, j in icebergs:
            ice[i][j] = max(0, ice[i][j] - chk[i][j])
            if ice[i][j] > 0:
                next_iceberges.append((i, j))

    return next_iceberges


# 2. 빙산 덩어리 세기
    # 1번 과정을 한 번 돌고 빙산이 분리되었는지 확인 

def bfs(s, e, visited):
    q = deque()
    q.append((s, e))
    visited[s][e] = True 
    
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] 
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if ice[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True 
                    q.append((nx, ny))

    return 1


# 결과: 빙산이 분리되는 최초의 시간을 출력
    # 만약 빙산이 다 녹을 때까지 분리되지 않으면 0
    '''
    배열 돌면서 덩어리를 확인(시작점은 배열 좌표 하나 넣어서
    모든 좌표를 다 방문했는데 bfs를 한 번만 돌렸으면 빙산 분리가 안 됨 -> 녹이기 
    '''
year = 0 
while icebergs:     
    visited = [[False] * m for _ in range(n)]

    # 배열 돌면서 bfs 몇 번 도는지 체크 
    cnt = 0 
    for i, j in icebergs:
        if not visited[i][j]:
            cnt += bfs(i, j, visited)

    if cnt >= 2:
        print(year)
        exit()
        
    icebergs = melt(ice, icebergs)
    year += 1

print(0)