import sys
input = sys.stdin.readline

n = int(input())
X, Y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.append(X[0])
Y.append(Y[0])

A, B = 0, 0
for i in range(n):
    A += X[i] * Y[i+1]
    B += Y[i] * X[i+1]

print(f"{abs(A-B)*0.5:.1f}")