def solution(m, w, num):
    answer = 0 
    
    n = (m + w - 1) // w
    arr = [[0] * w for _ in range(n)]

    ds = [1, -1]
    dr = 0
    x, y, fy = 0, 0, 0
    t = 1
    arr[x][y] = t

    while t < m:
        nx, ny = x, y + ds[dr]

        if ny >= w or ny < 0:
            dr = (dr + 1) % 2
            nx = x + 1
            ny = y

        t += 1
        arr[nx][ny] = t
        if t == num: 
            fy = ny 
        x, y = nx, ny
    
    for i in range(n-1, -1, -1):
        if arr[i][fy] != 0:
            answer += 1
            
        if arr[i][fy] == num:
            break 
    
    return answer