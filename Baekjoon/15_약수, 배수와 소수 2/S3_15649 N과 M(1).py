import sys
input = sys.stdin.readline

x = []
def backtracking():
    if len(x) == m:
        print(*x)
        return 
    
    for i in range(1, n+1):
        if i not in x:   #이 부분 대신 아래 주석이 들어갈 수 있음 
            x.append(i)
            backtracking()
            x.pop()

'''
        if visit[i]:
            continue
        visit[i] = True
        x.append(i)
        backtracking()
        x.pop()
        visit[i] = False
'''
        
#main
n, m = map(int,input().split())
visit = [False] * (n+1)
backtracking()



////////////////////////////////////
#다른 방법 

import sys
input = sys.stdin.readline

from itertools import permutations as p

n, m = map(int,input().split())

arr = [i for i in range(1,n+1)]
x = list(p(arr,m))

for i in x:
    print(*i)
