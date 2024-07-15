n = int(input())
num = 1 # 1부터 시작
cnt = 1 # 시작 포함

while n>num:
    num += 6 * cnt
    cnt += 1
print(cnt)
