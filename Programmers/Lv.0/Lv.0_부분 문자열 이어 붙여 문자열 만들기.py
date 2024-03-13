def solution(ms, parts):
    answer = ''
    for i in range(len(ms)):
        answer += ms[i][parts[i][0]:parts[i][1]+1]
    return answer
