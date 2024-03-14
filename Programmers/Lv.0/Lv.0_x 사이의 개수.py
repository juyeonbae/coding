def solution(s):
    answer = []
    index = 0
    for i in s:
        if i == 'x':
            answer.append(index)
            index = 0 
        else: index += 1
    answer.append(index)
    
    return answer

'''
x 로 split() 해서 쪼개진 문자열의 길이를 return 해주는 방법도 가능하다. 
'''
