import heapq, sys
input = sys.stdin.readline

pq = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if not pq: print(0)
        else:
            p = -heapq.heappop(pq)
            print(p)
    else:
        heapq.heappush(pq, -x)
