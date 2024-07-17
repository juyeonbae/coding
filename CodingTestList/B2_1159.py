# B2_1159_농구 경기.py

N = int(input())

arr, lst = [], {}
for i in range(N):
    arr.append(input().strip())

arr.sort()
for i in arr:
    if i[0] not in lst:
        lst[i[0]] = 1
    else:
        lst[i[0]] += 1

answer = ''
for key, value in lst.items():
    if value >= 5:
        answer += key

if len(answer) == 0:
        print("PREDAJA")
else: print(answer)

'''
성의 첫 글자가 같은 선수 < 5 인 경우 -> 기권 (PREDAJA 출력)
5 이상인 경우 -> 가능한 성의 첫 글자를 사준선으로 공백없이 모두 출력 
'''