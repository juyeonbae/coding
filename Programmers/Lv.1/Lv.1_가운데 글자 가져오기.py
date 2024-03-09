def solution(s):
    answer = ''
    if len(s) % 2 != 0:
        answer += s[len(s)//2]
    else:
        answer += s[len(s)//2-1] + s[len(s)//2]
    return answer


"""
조건문 대신 문자열 슬라이스로 축약 가능 
return s[(len(str)-1)//2 : len(str)//2 + 1] 
"""

