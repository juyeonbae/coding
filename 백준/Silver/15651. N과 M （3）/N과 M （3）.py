import sys
input = sys.stdin.readline

n, m = map(int,input().split())

x = []
def backtracking(start):
    if len(x) == m:
        print(*x)
        return
    
    for i in range(1,n+1):
        x.append(i)
        backtracking(i+1)
        x.pop()
    
backtracking(1)