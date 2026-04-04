import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

ans = 0 # 발견된 PN의 수
cnt = 0 # 연속된 'IOI' 패턴의 수
i = 1 # 문자열 인덱스 확인을 위해 1부터 시작

while i < (m-1):
    # 'IOI' 패턴을 찾았을 때
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        cnt += 1

        # 패턴이 N번 연속되었다면 정답 추가 
        if cnt >= n:
            ans += 1

        # IOI 찾았으므로 인덱스 2칸 건너뜀 
        i += 2
        
    else: # 패턴이 끊기면 연속 횟수 초기화 
        cnt = 0
        i += 1

print(ans)

