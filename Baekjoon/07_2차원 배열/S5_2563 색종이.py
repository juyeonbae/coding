n = int(input()) 
paper = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    x, y = map(int,input().split())
    for dx in range(x,x+10):
        for dy in range(y,y+10):
            paper[dx][dy] = 1
    
cnt = 0
for i in paper:
    cnt += i.count(1)

print(cnt)
