#B2_25501 재귀의 귀재.py

def recursion(s, l, r, cnt):
    if l >= r:
        return print(1, cnt)
    elif s[l] != s[r]:
        return print(0, cnt)
    return recursion(s, l+1, r-1,cnt+1)

def isPalindrome(s):
    cnt = 1
    return recursion(s, 0, len(s)-1, cnt)

#main
T = int(input())
for i in range(T):
    s = input()
    isPalindrome(s)
