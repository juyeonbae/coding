import math
def solution(n,m):
    return [math.gcd(n,m),n*m//math.gcd(n,m)]

'''프로그래머스 파이썬 버전이 math.lcm() 최소공배수 함수 나오기 이전 버전이라 적용 X
두 수의 곱 // 최대공약수 = 최소공배수 임을 활용'''


#파이썬 내장함수 사용 안 하고 풀이하기
def solution(n,m):
    answer = []
    
    #최대공약수: 두 수가 서로 공통으로 가지고 있는 약수 중 가장 큰 수 
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            answer.append(i)

    #최소공배수: 두 수에 서로 공통으로 존재하는 배수 중 가장 작은 수
    for i in range(1,n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
    
    return answer


#유클리드 호제법 풀이
def solution(n, m):
    x, y = max(n,m), min(n,m)
    t = 1
    while t>0:
        t = x % y
        x, y = y, t
    answer = [x, int(n*m/x)]
    return answer
