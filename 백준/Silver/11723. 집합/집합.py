import sys
input = sys.stdin.readline

m = int(input())
s = set()  # 숫자를 저장할 집합

for _ in range(m):
    op_str = input().strip()

    if op_str == 'all':
        s = set(range(1, 21))  # 1부터 20까지의 숫자로 모든 원소를 채움
    elif op_str == 'empty':
        s = set()  # 빈 집합으로 초기화
    else:
        op, x = op_str.split()
        x = int(x)  # 문자열을 숫자로 변환

        if op == 'add':
            s.add(x)  # 집합에 x를 추가
        elif op == 'remove':
            s.discard(x)  # 집합에서 x를 제거 (존재하지 않으면 무시)
        elif op == 'toggle':
            if x in s:
                s.discard(x)  # x가 있으면 제거
            else:
                s.add(x)  # 없으면 추가
        else:
            print(1 if x in s else 0)  # x가 있으면 1, 없으면 0 출력
