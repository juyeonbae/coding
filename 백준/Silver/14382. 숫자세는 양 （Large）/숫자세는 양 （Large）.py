import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    n = int(input())

    if n == 0:
        print(f"Case #{t}: INSOMNIA")
        continue

    visited = [False] * 10
    count = 0 
    i = 0
    current_n = 0 
    
    while count < 10:
        i += 1
        current_n = i * n

        for s in str(current_n):
            digit = int(s)
            if not visited[digit]:
                visited[digit] = True
                count += 1

    print(f"Case #{t}: {current_n}")