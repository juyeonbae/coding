import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

path = [] # 현재까지 만든 수열 
visited = [False] * (n+1)
answer = set()

def backtrack(num):
    # 길이가 m이면 완성된 수열 
    if len(path) == m:
        answer.add(tuple(path))
        return

    # 1부터 n까지 하나씩 넣어보기 
    for i in range(num, len(arr)):
        if visited[i]:
            continue
        path.append(arr[i])
        visited[i] = True
        backtrack(i+1) # 다음 자리로 
        path.pop() # 선택 취소
        visited[i] = False

backtrack(0)
for a in sorted(answer):
    print(*a)