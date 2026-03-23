import sys
input = sys.stdin.readline

while True:

    # 입력 받기
    chk = input().strip()
    if chk == '0':
        sys.exit()
        
    s = list(map(int, chk.split()))
    k, arr = s[0], s[1:]

    path = []
    visited = [False] * (k+1)

    # 백트래킹으로 6개 수 고르기 
    def backtrack(num):
        if len(path) == 6:
            print(*path)
            return

        for i in range(num, k):
            if visited[i]:
                continue
            path.append(arr[i])
            visited[i] = True
            backtrack(i+1)
            path.pop()
            visited[i] = False

    backtrack(0)
    print()
            