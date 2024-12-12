n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

visited = [False] * n  # 방문 체크 배열
current = 0  # 시작점
count = 0    # 이동 횟수

while True:
    # 이미 방문한 노드라면 사이클이 발생한 것
    if visited[current]:
        print(-1)
        break
    
    # 현재 노드 방문 체크
    visited[current] = True
    count += 1
    
    # 보성이(k)를 찾았다면
    if current == k:
        print(count - 1)  # 마지막 이동은 제외
        break
    
    # 다음 사람으로 이동
    current = arr[current]