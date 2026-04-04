import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append((v, i))
        graph[v].append((u, i))

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

       
        for next_node, weight in graph[now]:
            wait_time = (weight - (dist % m) + m) % m
            
            arrival_time = dist + wait_time + 1
            
            if distance[next_node] > arrival_time:
                distance[next_node] = arrival_time
                heapq.heappush(q, (arrival_time, next_node))

    print(distance[n])

solve()