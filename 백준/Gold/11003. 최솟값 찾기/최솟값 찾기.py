import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()
write = sys.stdout.write

buf = []
FLUSH = 10000  # 1만개씩 출력

for i, x in enumerate(A):
    start = i - L + 1
    while dq and dq[0][1] < start:
        dq.popleft()

    while dq and dq[-1][0] > x:
        dq.pop()

    dq.append((x, i))

    buf.append(str(dq[0][0]))
    if len(buf) == FLUSH:
        write(" ".join(buf) + " ")
        buf.clear()

# 남은 것 출력 (마지막은 공백 없이)
if buf:
    write(" ".join(buf))