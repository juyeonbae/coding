n, m = map(int, input().split())

d = {}
for i in range(n):
    url, pw = input().split()
    d[url] = pw

for i in range(m):
    chk = input()
    print(d[chk])
