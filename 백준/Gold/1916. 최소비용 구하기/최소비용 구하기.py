import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def solve():
# 2. 입력 받기:
   # 도시 수 N, 버스 수 M 입력
    n = int(input())
    m = int(input())

   # 빈 그래프 생성 (N+1 크기의 인접 리스트)
    graph = [[] for _ in range(n+1)]

   # M개의 버스 정보(출발, 도착, 비용)를 그래프에 추가
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        
   # 구하고자 하는 [시작 도시]와 [도착 도시] 입력
    start, end = map(int, input().split())

# 3. 다익스트라 함수 정의 (start_node):
    def dijkstra(start):
        
       # distance 배열을 아주 큰 값(INF)으로 초기화 (N+1 크기)
        distance = [INF] * (n+1)
        
       # 우선순위 큐(pq) 생성 및 (0, start_node) 넣기
        q = []
        heapq.heappush(q, (0, start))
        
       # 시작 도시의 거리는 0으로 설정 (distance[start_node] = 0)
        distance[start] = 0 
    
       # 우선순위 큐가 빌 때까지 반복:
        while q:
         # 현재 가장 비용이 적은 노드 정보를 꺼냄 (현재_비용, 현재_도시)
            dist, now = heapq.heappop(q)
         
         # [체크] 만약 (distance[현재_도시] < 현재_비용) 이라면:
         # 이미 더 짧은 경로를 찾은 것이므로 무시하고 다음 반복으로 (continue)
            if distance[now] < dist:
                continue

            # 현재 도시와 연결된 모든 인접 도시 확인:
            # 새로운_비용 = 현재_비용 + 인접_도시로_가는_비용
            for next_node, weight in graph[now]:
                cost = dist + weight
                
                # [갱신] 만약 (새로운_비용 < distance[인접_도시]) 라면:
                if cost < distance[next_node]:
                    
                    # distance[인접_도시]를 새로운_비용으로 업데이트
                    distance[next_node] = cost
                    
                    # 우선순위 큐에 (새로운_비용, 인접_도시) 추가
                    heapq.heappush(q, (cost, next_node))

        return distance

    # 4. 함수 실행:
    # 다익스트라(시작 도시) 호출
    result = dijkstra(start)

    # 5. 결과 출력:
    # distance[도착 도시] 값 출력
    print(result[end])

solve()