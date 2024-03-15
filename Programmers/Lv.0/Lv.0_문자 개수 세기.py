def solution(ms):
    answer = [0] * 52
    for s in ms:
        if ord(s) > 90:  #if s.islower(): 로 조건문 작성해줘도 좋음 // s가 소문자인지 확인 
            answer[ord(s)-71] += 1
        else:
            answer[ord(s)-65] += 1
    return answer
