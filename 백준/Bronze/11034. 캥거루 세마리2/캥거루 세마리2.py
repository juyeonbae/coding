import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break

    a, b, c = map(int, line.split())

    print(max(b-a-1, c-b-1))
    