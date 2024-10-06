n = int(input())
s = input()

r = 31
M = 1234567891

tot = 0
for i in range(n):
    tot += (ord(s[i]) - 96) * (r**i)

print(tot % M)