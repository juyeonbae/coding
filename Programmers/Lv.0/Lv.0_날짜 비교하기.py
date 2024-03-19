#나는 모든 경우의 수를 쪼개서 생각했는데 굳이 그럴 필요가 없었다.  
def solution(date1, date2):
    y,m,d = date2[0] - date1[0],date2[1] - date1[1],date2[2] - date1[2]
    
    if y > 0: return 1
    elif y == 0:
        if m > 0: return 1
        elif m == 0:
            if d > 0: return 1
            else: return 0
        else: return 0
    else: return 0

#조건문 한 번만 사용
def solution(date1, date2):
    for i in range(3):
        if date1 < date2:
            return 1
        else: return 0

# int로 부울대수 출력 
def solution(date1, date2):
    return int(date1<date2)
