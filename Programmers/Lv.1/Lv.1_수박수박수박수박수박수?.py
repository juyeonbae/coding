#가장 단순하게 푸는 조건문 코드 
def solution(n):
    if n == 1:
        return "수"
    elif n % 2 == 0:
        return "수박" * (n//2)
    else:
        return "수" + "박수" * ((n-1)//2)
            
#한 줄 코드 
def solution(n):
    return "수박" * (n//2) + "수" * (n%2)

#문자열 슬라이스 사용
def solution(n):
    return ("수박" * n) [:n]


'''
맨마지막 코드처럼 알고 있는 걸 적재적소에 써먹을 수 있는 문풀 센스가 생기길 바라며... (24/03/10) 
'''
