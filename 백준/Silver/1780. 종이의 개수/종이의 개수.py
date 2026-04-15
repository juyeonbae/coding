import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]

def dv(r, c, size):
    # 확인: 현재 영역이 모두 같은 숫자인지 검사
    curr = arr[r][c]
    is_same = True

    for i in range(r, r+size):
        for j in range(c, c+size):
            if arr[i][j] != curr:
                is_same = False
                break 
        if not is_same: break

    # 모두 같다면 해당 숫자 카운트 
    if is_same:
        ans[curr+1] += 1
        return 

    # 다르다면 분할 
    next_size = size//3
    for i in range(3):
        for j in range(3):
            dv(r+i*next_size, c+j*next_size, next_size)

dv(0, 0, n)
print(ans[0])
print(ans[1])
print(ans[2])
    