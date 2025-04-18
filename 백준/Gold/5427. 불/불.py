from collections import deque

# 4방향 이동 (오른쪽, 아래, 왼쪽, 위)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    w, h = map(int, input().split())  # 너비(w), 높이(h) 입력
    board = [list(input().strip()) for _ in range(h)]  # 빌딩 지도 입력

    fire_time = [[-1] * w for _ in range(h)]     # 불이 퍼지는 시간
    sang_time = [[-1] * w for _ in range(h)]     # 상근이가 도달한 시간

    fire = deque()  # 불의 위치를 저장할 큐
    sang = deque()  # 상근이의 위치를 저장할 큐

    # 초기 위치 탐색
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire.append((i, j))
                fire_time[i][j] = 0  # 시작점은 시간 0
            elif board[i][j] == '@':
                sang.append((i, j))
                sang_time[i][j] = 0  # 시작점은 시간 0

    # 🔥 불이 퍼지는 BFS
    while fire:
        x, y = fire.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 빌딩 내부인 경우만 진행
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    fire.append((nx, ny))

    # 🏃 상근이의 이동 BFS
    escaped = False  # 탈출 성공 여부

    while sang:
        x, y = sang.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 빌딩 밖으로 나갔을 경우 탈출 성공
            if not (0 <= nx < h and 0 <= ny < w):
                print(sang_time[x][y] + 1)
                escaped = True
                break

            # 벽이거나 이미 방문했거나, 불이 먼저 도착했거나 동시에 도착한 경우 skip
            if board[nx][ny] == '#' or sang_time[nx][ny] != -1:
                continue
            if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= sang_time[x][y] + 1:
                continue

            # 이동 가능하면 큐에 추가하고 시간 기록
            sang_time[nx][ny] = sang_time[x][y] + 1
            sang.append((nx, ny))

        if escaped:
            break

    # 탈출하지 못한 경우
    if not escaped:
        print("IMPOSSIBLE")
