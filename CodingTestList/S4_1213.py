s = input()

# 딕셔너리 만들기 
d = {}
for i in s:
    if i not in d: d[i] = 1
    else: d[i] += 1

# 개수가 홀수인 문자 세기 
cnt = 0
for k, v in d.items():
    if v % 2 != 0:
        cnt += 1

    if cnt > 1:
        print("I'm Sorry Hansoo")
        break

else:
    palin, drome = '', ''
    lst = dict(sorted(d.items()))
    x = ''

    for k, v in lst.items():
        if v % 2 != 0:
            x = k
        palin += k * (v//2)
        drome = k * (v//2) + drome 

    print(palin + x + drome)