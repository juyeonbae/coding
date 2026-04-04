import sys
input = sys.stdin.readline

n = int(input())
sx, sy, fx, fy = map(int, input().split())

mn, answer = float('inf'), 0 
for i in range(1, n+1):
    m = int(input())
    x, y = sx, sy
    tmp = 0
    
    for _ in range(m):
        nx, ny = map(int, input().split())
        dist = abs(nx-x) + abs(ny-y)
        tmp += dist
        x, y = nx, ny

    tmp += abs(x-fx) + abs(y-fy)
    
    if tmp < mn:
        answer = i 
        mn = tmp 

print(answer)

        