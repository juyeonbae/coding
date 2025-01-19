import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for i in range(M):
    k = int(input())
    st = list(map(int, input().split()))
    if st != sorted(st, reverse=True):
        print("No")
        break
else:
    print("Yes")