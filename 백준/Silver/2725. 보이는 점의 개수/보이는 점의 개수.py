import sys
input = sys.stdin.readline

MAX_N = 1000

# phi[i] = 오일러 피 함수 값
#        = 1 ~ i 중에서 i와 서로소인 수의 개수
phi = [i for i in range(MAX_N + 1)]

# 에라토스테네스처럼 phi를 한 번에 계산
for i in range(2, MAX_N + 1):
    # phi[i] == i 이면 i는 아직 한 번도 처리되지 않은 수 = 소수
    if phi[i] == i:
        # i의 배수들에 대해
        for j in range(i, MAX_N + 1, i):
            # 오일러 피 함수 공식 적용
            # phi[j] = phi[j] * (1 - 1/i)
            # 정수 계산으로는 아래처럼 쓸 수 있음
            phi[j] -= phi[j] // i

# prefix[n] = phi(1) + phi(2) + ... + phi(n)
prefix = [0] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    prefix[i] = prefix[i - 1] + phi[i]

# 테스트케이스 개수
c = int(input())

for _ in range(c):
    n = int(input())

    # 정답 공식
    # answer(n) = 2 * (phi(1) + phi(2) + ... + phi(n)) + 1
    print(2 * prefix[n] + 1)