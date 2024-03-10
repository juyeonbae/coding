def solution(s):
    return ''.join(reversed(sorted(s)))

"""
* sort() vs sorted()
(1) sort()
- 리스트명.sort() : 리스트형의 메소드
- 리스트 원본 값을 직접 수정
- 정렬된 값은 리턴 값이 None
- 내림차순 정렬 형식 >> 리스트명.sort(reverse = True)

(2) sorted()
- sorted(리스트명) : 내장 함수
- 리스트 원본 값은 그대로, 새로운 정렬 값을 반환
- 내림차순 정렬 형식 >> sorted(리스트명, reverse = True)

* reverse vs reversed
(1) reverse()
- 리스트 타입에서 제공하는 함수(리스트 자료만 적용)
- 값을 반환하지 않고 해당 리스트를 역으로 정렬
- 반환되는 것이 없음 
ex) a = [1,2,3,4,5]
a.reverse() >> a = [5,4,3,2,1]

(2) reversed()
- 내장함수, 리스트에서 제공하는 함수가 아님
- 순서가 있는 자료형에는 모두 사용 가능 
- 숫자와 딕셔너리는 시퀀셜한 타입이 아니므로 지원하지 않음
- 객체를 반환함 
ex) a = [1,2,3,4,5]
reversed(a) >> <list_reverseiterator object at 0x03C0CA48> //에러
list(reversed(a)) >> [5,4,3,2,1]

a = (1,2,3,4,5)
tuple(reversed(a)) >> (5,4,3,2,1)

a = '12345'
''.join(reversed(a)) >> '54321'


* ''.join(list) / '구분자'.join(list)
- 매개변수로 들어온 리스트에 있는 요소를 합쳐 하나의 문자열로 반환하는 함수
- ''.join(list) >> ['a','b','c'] -> 'abc'
- '_'.join(list) >> ['a','b','c'] -> 'a_b_c'
"""
