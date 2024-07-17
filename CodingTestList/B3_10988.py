# B3_10988_팰린드롬인지 확인하기.py

### 방법 1 - 36ms ###
s = input()
stack = []
for i in range(len(s)//2):
    stack.append(s[i])

l = len(s)//2 if len(s)%2 == 0 else len(s)//2+1
for i in range(l, len(s)):
    tmp = stack.pop()
    if tmp != s[i]:
        print(0)
        break
else: print(1)


### 방법 2 - 36ms ### 
s = input()
if s[:] == s[::-1]: print(1)
else: print(0)