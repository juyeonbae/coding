import math as m

n = int(input())
s = str(m.factorial(n))

rev_s = s[:][::-1]

cnt = 0
for i in range(n):
    if rev_s[i] != '0':
        break
    cnt += 1

print(cnt)