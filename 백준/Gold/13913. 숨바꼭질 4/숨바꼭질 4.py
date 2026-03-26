import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 10**5
# 1. 모든 거리를 -1로 초기화 (미방문 상태)
dist = [-1] * (MAX + 1)
parent = [-1] * (MAX + 1)

q = deque([n])
dist[n] = 0 # 시작점의 거리는 0

while q:
    curr = q.popleft()
    
    if curr == k:
        print(dist[k])
        path = []
        temp = k 
        while temp != -1:
            path.append(temp)
            temp = parent[temp]
        
        print(*(path[::-1]))
        exit() 

    for i in (curr + 1, curr - 1, curr * 2):
        # 2. dist[i]가 -1인 경우에만 방문 (중복 방문 방지)
        if 0 <= i <= MAX and dist[i] == -1:
            dist[i] = dist[curr] + 1
            parent[i] = curr 
            q.append(i)