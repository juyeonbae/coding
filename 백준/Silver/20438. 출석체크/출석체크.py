import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = [False] * (n + 3)

for x in map(int, input().split()):
    sleep[x] = True

senders = list(map(int, input().split()))

received = [False] * (n + 3)

# 1) 코드 전파 
for x in senders:
    if sleep[x]:
        continue
    for j in range(x, n + 3, x):
        if not sleep[j]:
            received[j] = True

# 2) 결석(=출석 못한) 누적합 만들기
prefix = [0] * (n + 3)
for i in range(3, n + 3):
    prefix[i] = prefix[i - 1] + (0 if received[i] else 1)

# 3) 질의는 O(1)
out = []
for _ in range(m):
    s, e = map(int, input().split())
    out.append(str(prefix[e] - prefix[s - 1]))

print("\n".join(out))