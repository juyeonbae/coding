#dfs
x = []
def backtracking(start):
    if len(x) == m:
        print(*x)
        return 
    
    for i in range(start, n+1):
        if visit[i]:
            continue
        visit[i] = True
        x.append(i)
        backtracking(i+1)
        x.pop()
        visit[i] = False
        
#main
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
visit = [False] * (n+1)
backtracking(1)