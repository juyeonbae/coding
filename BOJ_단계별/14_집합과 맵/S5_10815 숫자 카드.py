import sys
input = sys.stdin.readline

n = int(input())
sang = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in sang:
        print(1, end=' ')
    else:
        print(0, end=' ')
