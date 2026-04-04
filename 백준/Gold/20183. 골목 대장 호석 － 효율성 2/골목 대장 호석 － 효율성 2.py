# N개 교차로, M개 골목 
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def solve():
    n, m, a, b, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    max_weight = 0 
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        max_weight = max(max_weight, w)

    def dijkstra(limit):
        distance = [INF] * (n+1)

        q = []
        heapq.heappush(q, (0, a))
        distance[a] = 0 
    
        while q:
            dist, now = heapq.heappop(q)
    
            if distance[now] < dist:
                continue
    
            for next_node, weight in graph[now]:
                
                # 이번에 정한 limit보다 비싼 길은 아예 무시 
                if weight <= limit:
                    cost = dist + weight

                    # 총비용이 가진 돈 c 이내일 때만 이동 
                    if cost <= c and distance[next_node] > cost:
                        distance[next_node] = cost
                        heapq.heappush(q, (cost, next_node))

        # 목적지에 도달했고, 비용이 가진 돈 c 이내인가? 
        return distance[b] <= c

    # 이분 탐색 부분
    low = 1
    high = max_weight
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        # mid 요금 이하만 써서 갈 수 있다면? 
        if dijkstra(mid):
            answer = mid # 정답 후보 저장
            high = mid - 1
        else: # 갈 수 없다면 
            low = mid + 1 # 요금 기준 높이기 
        
    print(answer)

solve()