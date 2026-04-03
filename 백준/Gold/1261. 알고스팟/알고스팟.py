import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def solve():
    m, n = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    distance = [[INF] * m for _ in range(n)]

    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0 

    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                cost = dist + graph[x][y]
                
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    answer = distance[n-1][m-1]
    
    print(answer)

solve()