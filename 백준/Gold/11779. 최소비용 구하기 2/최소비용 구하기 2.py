# n개의 도시, m개의 버스, 최소 비용과 경로 출력 
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def solve():
    n = int(input()) # 도시 개수 
    m = int(input()) # 버스 개수 

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    # 각 노드의 이전 노드를 기록할 배열 
    parent = [0] * (n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    start, end = map(int, input().split())

    def dijstra(start, end):
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

                    # 최단 거리가 갱신될 때 부모 노드 기록
                    parent[next_node] = now
        
        return distance[end]

    print(dijstra(start, end))
    
    # 경로 역추적 
    path = []
    curr = end
    while curr != 0: 
        path.append(curr)
        curr = parent[curr] 

    # 역순으로 저장되었으므로 뒤집기
    path.reverse()
    
    print(len(path))
    print(*path)

solve() 