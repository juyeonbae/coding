import sys
input = sys.stdin.readline

from itertools import combinations as comb

n,m = map(int,input().split())
arr = list(map(int,input().split()))
c = list(comb(arr,3))

res = [] 
for i in c:
    s = sum(i)
    if s <= m:
        res.append(s)

print(max(res))
