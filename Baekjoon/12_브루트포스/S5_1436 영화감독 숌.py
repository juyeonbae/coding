n = int(input())
num, cnt = 666, 0

while n > 0:
    if '666' in str(num):
        cnt += 1
        if cnt == n:
            print(num)
            break
    num += 1
