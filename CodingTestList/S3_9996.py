# S3_9996_한국이 그리울 땐 서버에 접속하지.py - 52ms

n = int(input())
s,e = input().split("*")
for i in range(n):
    x = input()
    if len(x) >= len(s) + len(e) and x[:len(s)] == s and x[-len(e):] == e:
        print("DA")
    else:
        print("NE")