# N명의 학생, M개의 도로, 단방향, T의 시간 
# 갔다가 돌아와야 함
# 가장 많은 시간을 소비하는 학생

import heapq, sys
input = sys.stdin.readline
INF = float('inf')

def solve():
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))


    def dijkstra(start):
        distance = [INF] * (n+1)
        
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0 

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

    # 파티 장소(X)에서 각자의 집으로 돌아오는 시간들
    comeback = dijkstra(x) 

    max_total_time = 0 

    # 각 마을(i)에서 파티 장소(x)로 가는 시간 
    for i in range(1, n+1):
        go_to_party = dijkstra(i)

        total_time = go_to_party[x] + comeback[i]

        if total_time > max_total_time:
            max_total_time = total_time

    print(max_total_time)

solve()
        