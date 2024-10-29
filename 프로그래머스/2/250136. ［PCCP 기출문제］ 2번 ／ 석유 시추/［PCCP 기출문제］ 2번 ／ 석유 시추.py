from collections import deque

def bfs(land, x, y, visited, cluster_size, cluster_id):
    n, m = len(land), len(land[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(x, y)])
    visited[x][y] = True
    cluster_size_map = 1  # 덩어리 크기 초기화

    while queue:
        cx, cy = queue.popleft()
        cluster_size[cx][cy] = cluster_id  # 덩어리 ID 저장
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cluster_size_map += 1

    return cluster_size_map

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    cluster_size = [[0] * m for _ in range(n)]
    cluster_id_size = {}
    cluster_id = 1

    # 각 덩어리의 크기를 미리 계산하여 저장
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size = bfs(land, i, j, visited, cluster_size, cluster_id)
                cluster_id_size[cluster_id] = size  # 덩어리 크기 저장
                cluster_id += 1

    max_oil = 0

    # 각 열에 대해 가능한 최대 석유량 계산
    for col in range(m):
        visited_clusters = set()  # 열별로 중복 덩어리 방지
        total_oil = 0
        for row in range(n):
            cluster_id = cluster_size[row][col]
            if cluster_id > 0 and cluster_id not in visited_clusters:
                total_oil += cluster_id_size[cluster_id]
                visited_clusters.add(cluster_id)
        
        max_oil = max(max_oil, total_oil)

    return max_oil