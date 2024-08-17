T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())

    # N번째 손님의 층과 방 번호 계산
    h = N % H
    w = N // H + 1

    # N이 H의 배수인 경우
    if h == 0:
        h = H
        w -= 1

    print(f"{h}{w:02}")
