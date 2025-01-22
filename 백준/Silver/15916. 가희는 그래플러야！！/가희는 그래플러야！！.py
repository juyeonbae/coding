import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
k = int(input())

for i in range(1, n+1):
    if num[i] == k * i:
        print("T")
        exit()

    if (num[i-1] - k * (i-1)) * (num[i] - k * i) < 0:
        print("T")
        exit()

print("F")