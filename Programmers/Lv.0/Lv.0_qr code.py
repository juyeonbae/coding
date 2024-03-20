def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer
    #return code[r::q] 로도 가능/q로 나눈 값이 규칙적으로 반복되므로 q 간격으로 반환 
