import sys, heapq
input = sys.stdin.readline
INF = float('inf')

# N개의 헛간, M개의 길, 양방향 
def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    q = [] 
    heapq.heappush(q, (0, 1))
    distance[1] = 0 

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    
    print(distance[n])

solve()