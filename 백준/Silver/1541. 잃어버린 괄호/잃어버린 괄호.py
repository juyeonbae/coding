s = input()  # 55-50+40
arr = s.split("-")

tmp = []
for m in arr:
    if "+" in m:
        plus = list(map(int, m.split("+")))
        tmp.append(sum(plus))

    else: tmp.append(int(m))

res = tmp[0]
for t in range(1, len(tmp)):
    res -= tmp[t]

print(res)