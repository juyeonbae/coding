def solution(n):
    answer = 0
    arr = []
    while True:
        if n == 0: break 
        arr.append(n%3)
        n = n//3

    arr2 = list(reversed(arr))     #list해줄 필요 없이 그냥 arr.reverse() 해도 뒤집어짐 
    for i in range(len(arr)):
        answer += (3**i)*arr2[i]
    
    return answer

'''
# n진수 > 10진수 변환 
int("문자열", 사용된 진법)  
ex) int("0021",3) # 3진법인 0021을 10진수로 변환 > 7 출력 

#10진수 > 2,8,16 진수 변환
bin(수) > 2진수 변환 # 0b < 진법 표기 지우려면 [2:] 문자열 슬라이스 사용
oct(수) > 8진수 변환 # 0o
hex(수) > 16진수 변환 # 0x
'''
