T = int(input())
for t in range(T):
    n = int(input())
    exp = n * (n+1) // 2

    lv, left, right = 1, 0, n

    while left <= right:
        mid = (left + right) // 2
        need = mid * (mid + 1)

        if need <= exp:  # 경험치가 충분하면 더 높은 레벨 가능
            lv = mid
            left = mid + 1
        else:  # 경험치가 부족하면 더 낮은 레벨을 찾는다.
            right = mid - 1

    print(lv+1)