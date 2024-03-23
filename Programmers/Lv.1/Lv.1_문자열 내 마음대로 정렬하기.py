def solution(s, n):
    s.sort(key = lambda x : (x[n],x))   
    return s


'''
s.sort(key = lambda x: (x[n],x))
람다 정렬
x배열의 n번째 인덱스로 오름차순 정렬
>>만일 n번째 인덱스가 같다면 x 전체 확인
'''
