import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
period = [0] + list(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

last_brushed = [0] * (n+1) # 마지막으로 빗은 날
is_tangled = [False] * (n+1) # 엉킴 유무
con_brush = [0] * (n+1) # 연속으로 빗은 횟수

for i in range(1, m+1):
    dog = arr[i] 

    # 강아지 빗질 
    con_brush[dog] += 1 

    # 연속 빗고, 엉켜있으면 -> 풀기 
    if con_brush[dog] >= 2 and is_tangled[dog]:
        is_tangled[dog] = False

    # 오늘 빗은 날짜 갱신 
    last_brushed[dog] = i # 1일

    # 다른 강아지들 연속 횟수 초기화 
    for j in range(1, n+1):
        if dog != j:
            con_brush[j] = 0 

    # 엉킴 판정
    for l in range(1, n+1):
        if i - last_brushed[l] >= period[l]:
            is_tangled[l] = True

print(sum(is_tangled))
    