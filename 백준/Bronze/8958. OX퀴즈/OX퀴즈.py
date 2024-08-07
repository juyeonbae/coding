T = int(input())
for tc in range(T):
    s = input()

    cnt, answer = 0, 0
    for i in s:
        if i == 'O':
            cnt += 1
            answer += cnt * 1
        else:
            cnt = 0

    print(answer)
