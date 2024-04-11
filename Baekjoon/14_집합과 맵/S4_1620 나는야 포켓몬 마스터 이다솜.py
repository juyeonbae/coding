import sys
input = sys.stdin.readline

n, m = map(int,input().split())

po = {}
for i in range(1,n+1):
    po[str(i)] = input().strip()

po_rev = {v:k for k, v in po.items()}

for i in range(m):
    q = input().strip()
    
    if q.isdigit():
        print(po.get(q))
    else:
        print(po_rev.get(q))
