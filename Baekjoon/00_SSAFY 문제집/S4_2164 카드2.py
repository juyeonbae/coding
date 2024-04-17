#S4_2164 카드2.py

from collections import deque as dq

n = int(input())
arr = [i for i in range(1,n+1)]
q = dq(arr)

while True:
    if len(q) == 1:
        print(*q)
        break
    q.popleft()
    q.append(q.popleft())
