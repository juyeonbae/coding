#내가 푼 코드 - 경우를 모두 나눠서 조건문을 남발함 ㅠㅠ
def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper():
            if ord(i) + n > 90:
                answer += chr((ord(i)+n)%90 + 64)
            else:
                answer += chr(ord(i) + n)
        else:
            if ord(i) + n > 122:
                answer += chr((ord(i)+n)%122 + 96)
            else:
                answer += chr(ord(i) + n)
    return answer

'''
조건문을 합쳐보자. 
def solution(s,n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper(): #알파벳이 26개이므로 
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        else:  
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
    return answer
'''
