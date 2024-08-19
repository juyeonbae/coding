from collections import deque

def solution(q, M):
    findX, cnt = q[M], 0 # 찾으려는 값, 출력 순서
    findIdx = M # 찾는 값 인덱스 저장

    while True:
        qMax = max(q) # q의 max 값

        # 종료 조건
        if qMax == findX and findIdx == 0:
            return cnt + 1

        if q[0] == qMax:
            q.popleft()
            cnt += 1

        else:
            q.rotate(-1) # 첫번째 위치 값이 같지 않으면 rotate

        if findIdx == 0: # rotate 할 때마다 찾는 값 인덱스 갱신
            findIdx = len(q) - 1
        else: findIdx -= 1

T = int(input())
for tc in range(T):
    # N: 문서 개수 / M: 출력 순서가 궁금한 문서의 인덱스
    N, M = map(int, input().split())
    # N개의 문서 중요도
    arr = list(map(int, input().split()))
    q = deque(arr)
    # 문서의 중요도가 높은 순으로 출력
    print(solution(q, M))

