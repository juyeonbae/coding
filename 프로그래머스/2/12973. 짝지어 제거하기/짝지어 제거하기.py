def solution(s):
    chk = []
    for i in range(len(s)):
        if len(chk) == 0:
            chk.append(s[i])
        elif chk[-1] == s[i]:
            chk.pop()
        else:
            chk.append(s[i])

    if len(chk) == 0:
        return 1
    return 0