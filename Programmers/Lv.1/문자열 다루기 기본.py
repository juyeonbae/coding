def solution(s):
    return s.isdigit() if len(s) == 4 or len(s) == 6 else False

#return문에서 바로 return s.isdigit() and len(s) in [4,6] 으로 반환 가능

"""
len(s) in [4,6] 과 len(s) in (4,6) 차이점
- 둘다 기능적으로 문자열 s의 길이가 4 인지 6인지 확인하는 것은 동일
- [4,6] : 리스트로 값이 수정 가능
- (4,6) : 튜플로 값이 수정 불가능 
"""
