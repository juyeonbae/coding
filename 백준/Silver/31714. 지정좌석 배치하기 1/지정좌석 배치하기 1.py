n, m, d = map(int, input().split())  # 행, 열, 높이 차이


# (앞줄) 좌석 높이 + 키 < (뒷줄) 좌석 높이 + 키
# 주어진 조건에 맞게 모든 학생을 원하는 행의 좌석에 배치할 수 있는지 여부 출력

arr = []
for i in range(n):
    # i+1줄, i행에 앉고자 하는 학생 m명의 키
    height = list(map(int, input().split()))
    for j in range(m):
        height[j] += d * (i + 1)

    height.sort()
    arr.append(height)


def chk():
    for i in range(m):
        for j in range(n - 1):
            if arr[j][i] >= arr[j + 1][i]:
                return False
    return True


if chk():
    print("YES")
else:
    print("NO")
