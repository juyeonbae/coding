a = int(input())
b = int(input())
c = int(input())

x = str(a*b*c)

d = {}
for i in x:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for i in range(10):
    if str(i) in d.keys():
        print(d[str(i)])
    else:
        print(0)