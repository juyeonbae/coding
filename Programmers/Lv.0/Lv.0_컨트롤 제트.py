def solution(s):
    s = list(s.split())
    s_sum = 0
    for i in range(len(s)):
        if s[i] == 'Z':
            s_sum -= int(s[i-1])
        else:
            s_sum += int(s[i])
    return s_sum

#스택으로 풀기 >> 배열로 할 때는 pop하면 인덱스가 리스트 범위 넘어갔다고 자꾸 에러 떠서 힘들었는데, 스택은 에러 뜰 일이 없어서 좋네..^^
def solution(s):
    stack = []
    for i in s.split():
        if i != 'Z':
            stack.append(int(i))
        else:
            stack.pop()
    return sum(stack)
