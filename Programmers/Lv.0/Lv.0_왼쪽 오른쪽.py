def solution(s):
    for i in range(len(s)):
        if s[i] == 'l':
            return s[:i]
        if s[i] == 'r':
            return s[i+1:]
    return []

'''
##처음에 푼 풀이
[오류사항]
- 처음에 나오는 l 또는 r을 제외하고는 l, r 출력을 해주어야 함. 

def solution(s):
    answer = []
    for i in s:
        if 'r' not in s and 'l' not in s:
            break
        if i == 'l':
            if 'r' in s:
                if s.index('r') < s.index('l'):
                    continue
            break
        if i == 'r':
            answer = []
        else:
            answer.append(i)
    return answer

  '''
