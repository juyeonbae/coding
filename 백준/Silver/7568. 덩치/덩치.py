N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
ranks = []

for i in range(N):
    rank = 1
    for j in range(N):
        if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
            rank += 1
    ranks.append(rank)
    
print(*ranks)