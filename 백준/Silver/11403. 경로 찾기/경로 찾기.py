import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for k in range(n): # 거쳐가는 점
    for i in range(n): # 시작점
        for j in range(n): # 도착점 
            # i에서 k로 갈 수 있고, k에서 j로 갈 수 있다면
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1 

for row in arr:
    print(*row)