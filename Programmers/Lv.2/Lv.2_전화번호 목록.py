def solution(phone_book):
    phone_book.sort()  # 사전 순으로 정렬

    for i in range(len(phone_book) - 1):
        # 인접한 전화번호만 비교하여 접두사 여부 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True

'''
startswith 
- 문자열 메서드
- 특정 문자열이 주어진 접두사로 시작하는지 확인

str.startswith(prefix, start, end)
- str: 확인하려는 문자열
- prefix: 시작 여부를 확인할 접두사 문자열, 튜플 형태로 여러 접두사를 넣을 수 있음
- start(선택): 확인을 시작할 인덱스, 기본값은 0
- end(선택): 확인을 종료할 인덱스, 기본값은 문자열 끝

반환값
- 문자열이 지정된 접두사로 시작하면 True, 아니면 False
'''


# 틀린 코드 - 1차 시도
'''
# 접두사인지 확인하는 함수
def prefix(arr):
    for i in range(len(arr)-1):
        x = len(arr[i]) # arr[i] 가 접두사일 때 

        for j in range(i+1, len(arr)):
            s = arr[j] # x가 s의 접두사인지 확인
            if arr[i] == s[:x]:
                return False
            
        else: return True

# main
def solution(phone_book):
    arr = sorted(phone_book, key= lambda x: len(x))
    answer = prefix(arr)

    return answer
'''