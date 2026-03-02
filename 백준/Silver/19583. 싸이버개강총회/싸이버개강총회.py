import sys
input = sys.stdin.readline

S, E, Q = input().split()
h, m = map(int, S.split(":"))
s = h * 60 + m 
h, m = map(int, E.split(":"))
e = h * 60 + m 
h, m = map(int, Q.split(":"))
q = h * 60 + m 


enter = set()
cnt = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    time, name = line.split()
    h, m = map(int, time.split(":"))
    t = h * 60 + m 

    if s >= t:
        enter.add(name)

    elif e <= t <= q and name in enter:
        cnt += 1
        enter.remove(name)

    elif t > q:
        break

print(cnt)