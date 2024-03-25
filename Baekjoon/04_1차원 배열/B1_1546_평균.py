N = int(input())
score = list(map(int,input().split()))

newScore = []
for i in score:
    newScore.append(i/max(score)*100)

print(sum(newScore)/N)
