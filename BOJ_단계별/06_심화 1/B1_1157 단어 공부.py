s = input().upper()
set_s = list(set(s))
cnt = []

for i in set_s:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(set_s[cnt.index(max(cnt))])
