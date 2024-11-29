def solution(s):
    idx = 0
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            answer += s[i]
        elif idx == 0:
            answer += s[i].upper()
            idx += 1
        else:
            answer += s[i].lower()
            idx += 1

    return answer