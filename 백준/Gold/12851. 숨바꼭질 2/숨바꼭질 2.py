import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 100000
dist = [-1] * (MAX+1)

q = deque([(n)])
dist[n] = 0 
cnt = 0 # 최단 시간으로 도달하는 방법의 수 

while q:
    x = q.popleft()

    if x == k:
        cnt += 1
        continue # 최단 시간을 구하고 다른 경로 확인 

    for i in (x-1, x+1, 2*x):
        if 0 <= i < MAX+1:
            # 1. 처음 방문하는 경우
            # 2. 이미 방문했지만, 현재 계산된 시간 = 기존 시간 
            if dist[i] == -1 or dist[i] == dist[x] + 1:
                dist[i] = dist[x] + 1 
                q.append(i)

print(dist[k])
print(cnt)

    