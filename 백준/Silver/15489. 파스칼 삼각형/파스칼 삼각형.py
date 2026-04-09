r, c, w = map(int, input().split())

arr = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    for j in range(1, 31):
        if i == j or j ==1:
            arr[i][j] = 1

        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]  

answer = 0
for i in range(r, r+w):
    for j in range(c, i-r+c+1):
        answer += arr[i][j]

print(answer)