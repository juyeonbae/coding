import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def solve():
    tc = 1
    
    while True:
        n = int(input())
        
        if n == 0:
            sys.exit()

        graph = [list(map(int, input().split())) for _ in range(n)]
        distance = [[INF] * n for _ in range(n)]
        
        q = []
        heapq.heappush(q, (0, 0))
        distance[0][0] = graph[0][0]

        dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while q:
            x, y = heapq.heappop(q)

            if distance[x][y] < graph[x][y]:
                continue

            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    cost = distance[x][y] + graph[nx][ny]
    
                    if distance[nx][ny] > cost:
                        distance[nx][ny] = cost
                        heapq.heappush(q, (nx, ny))
            
        print("Problem", str(tc)+":", distance[n-1][n-1])    
        tc += 1

solve()