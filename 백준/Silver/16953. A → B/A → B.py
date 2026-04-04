import sys
input = sys.stdin.readline

from collections import deque

a, b = map(int, input().split())

q = deque([(a, 1)])
result = -1 

while q:
    x, cnt = q.popleft()

    if x == b:
        result = cnt
        break

    for i in (x*2, int(str(x) + '1')):
        if i <= b:
            q.append((i, cnt+1))

print(result)

