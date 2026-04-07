import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

if sum(arr) >= 100:
    for i in range(len(arr)):
        x = i // 2
        if arr[i] > 100 * (x+1):
            print("hacker")
            break
    else:
        print("draw")

else:
    print("none")