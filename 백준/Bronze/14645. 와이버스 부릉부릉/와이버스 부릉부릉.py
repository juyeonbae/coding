n, k = map(int, input().split())

bus = k
for i in range(n):
    a, b = map(int, input().split())
    bus = bus + a - b
print("비와이")