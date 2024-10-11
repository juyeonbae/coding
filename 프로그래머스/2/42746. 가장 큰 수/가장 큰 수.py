from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

def solution(numbers):
    # numbers의 모든 요소를 문자열로 변환
    numbers = list(map(str, numbers))
    # 맞춤형 비교 함수로 정렬
    numbers.sort(key=cmp_to_key(compare))
    # 정렬된 숫자들을 이어 붙임
    answer = ''.join(numbers)
    # 결과가 '000...'인 경우 '0'으로 변환
    return str(int(answer))