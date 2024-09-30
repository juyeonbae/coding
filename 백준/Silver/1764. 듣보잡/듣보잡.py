n, m = map(int, input().split())

# 못들은 사람과 못본 사람을 각각 집합으로 생성
heard = {input().strip() for _ in range(n)}
seen = {input().strip() for _ in range(m)}

# 두 집합의 교집합 구하기
result = sorted(heard & seen)

# 결과 출력
print(len(result))
for name in result:
    print(name)
