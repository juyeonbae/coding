T = int(input())
for i in range(T):
    r,s = input().split()
    answer = ''
    for j in s:
        answer += int(r) * j
    print(answer)
