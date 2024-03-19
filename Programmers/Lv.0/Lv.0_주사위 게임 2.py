def solution(a, b, c):
    answer = 0
    if a != b and a != c and b != c:
        answer += a + b + c
    elif a == b and a == c and b == c:
        answer += 27 * (a**6)
    else:
        answer += (a + b + c) * (a**2 + b**2 + c**2)
    return answer


#set으로 동일값 추출 가능 
