import sys
from collections import deque

input = sys.stdin.readline

# n: 수빈이 위치, k: 동생 위치
n, k = map(int, input().split())
MAX = 100000
dist = [-1] * (MAX+1)

q = deque([n])
dist[n] = 0 

while q:
    curr = q.popleft()

    # 동생을 찾았다면 결과 출력 
    if curr == k:
        print(dist[curr])
        exit()

    # 1. 순간이동 (0초 소요) 
    # 가장 높은 우선순위를 가지므로 가장 먼저 체크하고 큐의 앞에 넣는다. 
    next_pos = curr * 2
    if 0 <= next_pos <= MAX and dist[next_pos] == -1:
        dist[next_pos] = dist[curr] # 시간은 그대로
        q.appendleft(next_pos)

    # 2. 걷기 (1초 소요)
    # 0초 이동보다 나중에 처리되어야 하므로 큐의 뒤에 넣는다. 
    for next_pos in (curr-1, curr+1):
        if 0 <= next_pos <= MAX and dist[next_pos] == -1:
            dist[next_pos] = dist[curr] + 1 
            q.append(next_pos) 
