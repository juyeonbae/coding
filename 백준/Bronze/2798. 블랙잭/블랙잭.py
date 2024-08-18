from itertools import combinations as c

N, M = map(int,input().split())
lst = list(map(int,input().split()))

bjack = []
for x in list(c(lst, 3)):
    if sum(x) <= M:
        bjack.append(sum(x))

print(max(bjack))

