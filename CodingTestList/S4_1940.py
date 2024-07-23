# S4_1940_주몽.py
N = int(input()) # 재료의 개수
M = int(input()) # 갑옷을 만드는 데 필요한 수
arr = list(map(int, input().split())) # 재료들 고유 번호

d, cnt = {}, 0
for i in arr:
    if (M - i) in d:
        cnt += d[M - i]

    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(cnt)
