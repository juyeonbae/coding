import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 맥도날드 수, 맥세권 조건 x
    mdn_num, x = map(int, input().split())

    # 맥도날드 정점 
    mdn = list(map(int, input().split()))

    # 스타벅스 수, 스타벅스 조건 y
    stb_num, y = map(int, input().split())

    # 스타벅스 정점 
    stb = list(map(int, input().split()))
    

    def dijkstra(starts): # 여러 시작점 한 번에 넣기 
        distance = [INF] * (n+1)
        
        q = []
        for s in starts:
            distance[s] = 0
            heapq.heappush(q, (0, s))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for next_node, weight in graph[now]:
                cost = dist + weight
                
                if distance[next_node] > cost:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
        
        return distance

    # 1. 모든 맥도날드로부터 최단 거리 계산 
    dist_to_mdn = dijkstra(mdn)
    # 2. 모든 스타벅스로부터 최단 거리 계산
    dist_to_stb = dijkstra(stb)

    # 집이 될 수 없는 노드 
    spots = set(mdn) | set(stb)

    result_dist = INF

    for i in range(1, n+1):
        # 집이 될 수 없는 노드(맥도날드, 스타벅스) 
        if i in spots:
            continue 

        # 조건 확인 (맥세권 x 이하, 스세권 y 이하)
        if dist_to_mdn[i] <= x and dist_to_stb[i] <= y:
            total = dist_to_mdn[i] + dist_to_stb[i]

            if total < result_dist:
                result_dist = total
    
    print(-1 if result_dist == INF else result_dist)

solve()