import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

# 0. 입력 받기
arr = [list(input().strip()) for _ in range(5)]
answer = 0

# 3. BFS - 7명이 모두 연결되어 있는지 확인 
def bfs(selected):
    q = deque([selected[0]]) # 7개 중 한 점에서 시작
    visited = set([selected[0]])
    selected_set = set(selected)

    while q:
        x, y = q.popleft()

        for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            nx, ny = x + dx, y + dy

            if (nx, ny) in selected_set and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))

    return len(visited) == 7



# 1. 25명 중 7명을 그냥 뽑는다. (조합)
for comb in combinations(range(25), 7):
    # 2-1. 좌표 변환
    nums = [(x//5, x%5) for x in comb]
    
    s_count = 0 
    for i, j in nums:
        # 2-2. 이다솜파(S)가 4명 이상인지 확인
        if arr[i][j] == 'S':
            s_count += 1
            
    if s_count < 4:
        continue

    if bfs(nums):
        answer += 1

print(answer)