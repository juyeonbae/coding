#B2_10820 문자열 분석.py

def cnt(s):
    low, up, num, space = 0,0,0,0
    for i in s:
        if i.isdigit(): num += 1
        elif i.isupper(): up += 1
        elif i.islower(): low += 1
        else: space += 1
    return low, up, num, space

#main
while True:
    try:
        s = input()
        if cnt(s):
            print(*cnt(s))
        else:
            break
    except EOFError:
        break
