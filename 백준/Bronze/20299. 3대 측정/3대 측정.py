import sys
input = sys.stdin.readline 

n, k, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer, cnt = [], 0 
for a in arr:
    x, y, z = a 
    if x >= l and y >= l and z >= l and sum(a) >= k:
        cnt += 1
        answer.append(x)
        answer.append(y)
        answer.append(z)


print(cnt)
print(*answer)
        