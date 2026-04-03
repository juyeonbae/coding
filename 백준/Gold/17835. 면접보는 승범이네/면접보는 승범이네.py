import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def solve():
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[v].append((u, c))

    # 면접장 배치 노드 리스트 
    spots = list(map(int, input().split()))

    def dijkstra(spots):
        q = []
        for s in spots:
            heapq.heappush(q, (0, s))
            distance[s] = 0 

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

    interview = dijkstra(spots)

    city, dist = -1, -1
    for i in range(1, len(interview)):
        if interview[i] > dist:
            dist = interview[i]
            city = i 

        elif interview[i] == dist and i < city:
            city = i 

    print(city)
    print(dist)
    
solve()