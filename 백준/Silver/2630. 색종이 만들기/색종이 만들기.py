def check_color(x, y, n, paper):
    # 해당 영역의 첫 번째 색상
    color = paper[x][y]
    
    # 영역 내 모든 색상이 같은지 확인
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                return -1
    return color

def divide_paper(x, y, n, paper, result):
    # 현재 영역의 색상 확인
    color = check_color(x, y, n, paper)
    
    # 모든 칸이 같은 색인 경우
    if color != -1:
        result[color] += 1
        return
    
    # 4등분으로 나누어 재귀 호출
    new_n = n // 2
    divide_paper(x, y, new_n, paper, result)  # 왼쪽 위
    divide_paper(x, y + new_n, new_n, paper, result)  # 오른쪽 위
    divide_paper(x + new_n, y, new_n, paper, result)  # 왼쪽 아래
    divide_paper(x + new_n, y + new_n, new_n, paper, result)  # 오른쪽 아래

# 입력 받기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 흰색(0)과 파란색(1) 색종이 개수를 저장할 리스트
result = [0, 0]

# 분할 정복 시작
divide_paper(0, 0, N, paper, result)

# 결과 출력
print(result[0])  # 흰색 색종이 개수
print(result[1])  # 파란색 색종이 개수