import sys
input = sys.stdin.readline

K, L = map(int, input().split())

dct = {}

for _ in range(L):
    student = input().strip()
    if student in dct:
        del dct[student]   # 기존 순서 제거
    dct[student] = True    # 다시 삽입 (맨 뒤로 감)

# 앞에서부터 K명 출력
for i, student in enumerate(dct):
    if i == K:
        break
    print(student)