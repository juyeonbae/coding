import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    
    # 1. 초기값 설정 (첫 번째 열)
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    if n > 1:
        # 2. 두 번째 열 설정
        # 두 번째 열의 위쪽 스티커를 고르려면 첫 번째 열의 아래쪽을 골랐어야 함 
        dp[0][1] = arr[1][0] + arr[0][1] 
        dp[1][1] = arr[0][0] + arr[1][1]
    
        # 3. 점화식을 이용한 DP 진행(세 번째 열부터) 
        for i in range(2, n):
            # i번째 열의 위쪽 스티커를 고르는 경우 
            # 1) 바로 직전 대각선(아래)까지의 합
            # 2) 그 전 대각선(아래)까지의 합 중 최댓값 선택
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
    
            # i번째 열의 아래쪽 스티커를 고르는 경우도 동일하게 적용
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]

    # 마지막 열의 두 값 중 큰 값이 정답
    print(max(dp[0][n-1], dp[1][n-1]))