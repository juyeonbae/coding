# n: 못들은 사람, m: 못본 사람
n, m = map(int, input().split())

p = {input(): 1 for _ in range(n)}

cnt, lst = 0, []
for i in range(m):
    s = input()
    if s in p:
        cnt += 1
        p[s] -= 1

print(cnt)

res = []
for k, v in p.items():
    if v == 0:
        res.append(k)

res.sort()

for i in res: print(i)