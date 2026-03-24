import sys
input = sys.stdin.readline

# 입력
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]


def backtrack(idx, broken_cnt):
    # 종료 조건 
    # 1. 가장 오른쪽에 위치한 계란일 경우
    if idx == n:
        # 깨진 계란 개수 새기 (내구도 0 이하)
        return broken_cnt
        
    # 2. 예외: 손에 든 계란이 깨진 경우 
    # 3. 예외: 다른 계란이 전부 깨진 경우
    if eggs[idx][0] <= 0 or broken_cnt == n-1:
        # 다음 계란으로 넘어감 
        return backtrack(idx + 1, broken_cnt)


    # 계란들 하나식 다 쳐보기
    max_broken = 0

    # for 선택지 in 가능한 후보들: 
    for target in range(n):
        if idx == target or eggs[target][0] <= 0: 
            continue # 자기자신 & 이미 깨진 계란 
            
        # 1. 치기(내구도 감소)
        eggs[idx][0] -= eggs[target][1]
        eggs[target][0] -= eggs[idx][1]

        # 이번 충돌로 새로 깨진 계란 수 계산
        new_broken = 0
        if eggs[idx][0] <= 0: new_broken += 1
        if eggs[target][0] <= 0: new_broken += 1

        # 2. 다음 계란으로 진행
        result = backtrack(idx+1, broken_cnt+new_broken)
        max_broken = max(max_broken, result)

        # 3. 복구(내구도 다시 더하기)
        eggs[idx][0] += eggs[target][1]
        eggs[target][0] += eggs[idx][1]

    return max_broken


# 정답 출력 
print(backtrack(0, 0))