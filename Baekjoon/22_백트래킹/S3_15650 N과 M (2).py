#combinations
import sys
input = sys.stdin.readline

from itertools import combinations as c

n, m = map(int,input().split())

arr = [i for i in range(1,n+1)]
x = list(c(arr,m))

for i in x:
    print(*i)


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
