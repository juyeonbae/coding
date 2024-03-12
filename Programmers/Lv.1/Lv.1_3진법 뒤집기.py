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
3진법 변환 방법
int("문자열", 변환하고자 하는 진법)
'''
