import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

# 최단 경로 구하기, 가중치는 10 이하의 자연수 > 다익스트라 
# 방향이 있음 > 주어진대로만 push 할 것 

def solve():
    # 1. 입력 받기
    n, m = map(int, input().split())
    start = int(input())

    # 2. 그래프 정의, 거리 배열 정의
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    # 3. 간선 입력 받고, 그래프에 저장 
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    # 4. q 우선순위 큐 정의
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 # 시작점 거리는 0 

    # dijkstra 최단 거리 구하기 
    while q:
        dist, now = heapq.heappop(q)

        # 이미 방문한 노드일 경우 continue
        if distance[now] < dist:
            continue

        # 갱신하는 경우
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                distance[next_node] = cost 
                heapq.heappush(q, (cost, next_node))

    for i in range(1, n+1):
        if distance[i] == INF:
            print("INF")
        else: print(distance[i])

solve()
    