def solution(s):
    answer = ''
    index = 0
    for x in s:
        if x == ' ':
            answer += ' '
            index = 0
        else:
            if index % 2 == 0:
                answer += x.upper()
            else: answer += x.lower()
            index += 1

    return answer

'''
처음에는 split() 한 후, 배열로 접근했다. 테스트케이스만 통과하고 제출은 통과되지 않아 반례를 찾아헤멤..
(반례 - 프로그래머스 질문하기에서 답변 받았다. // 공백도 문자로 받아야 한다.)
s = "try   hello   world"
return -> "TrY   HeLlO   WoRlD"

def solution(s):
    s = s.split()
    answer = ''
    for i in range(len(s)):
        if i > 0:
            answer += ' '
        for j in range(len(s[i])):
            if j % 2 == 0:
                answer += s[i][j].upper()
            else:
                answer += s[i][j].lower()

    return answer
'''
