import sys
input = sys.stdin.readline
INF = 1e9 

def solve():
    n, m, w = map(int, input().split())
    edges = []

    # 도로: 양방향, 가중치 양수
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    # 웜홀: 단방향, 가중치 음수
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    def bellman_ford():
        # 모든 지점에서 음수 사이클을 찾아야 하므로 0으로 초기화해도 무방
        dist = [0] * (n + 1)
        
        for i in range(n):
            for u, v, weight in edges:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    # n번째 루프에서도 갱신되면 음수 사이클 존재
                    if i == n - 1:
                        return True
        return False

    if bellman_ford():
        print("YES") # 시간이 되돌아감 (음수 사이클 있음)
    else:
        print("NO")

tc = int(input())
for _ in range(tc):
    solve()