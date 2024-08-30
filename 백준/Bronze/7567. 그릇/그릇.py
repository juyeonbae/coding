
s = input()
ans = 10
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        ans += 10
    else:
        ans += 5

print(ans)