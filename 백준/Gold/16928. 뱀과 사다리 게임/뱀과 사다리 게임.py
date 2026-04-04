import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split()) # 사다리 수, 뱀 수
board = [i for i in range(101)]

for _ in range(n+m):
    a, b = map(int, input().split())
    board[a] = b

dist = [-1] * 101  # 방문 안 함 표시
q = deque([(1)])
dist[1] = 0

while q:
    x = q.popleft()

    if x == 100:
        print(dist[x])
        break 

    for dice in range(1, 7):
        nx = x + dice

        if nx < 101:
            final = board[nx]

            if dist[final] == -1:
                dist[final] = dist[x] + 1
                q.append(final)

