from collections import deque


def chk(q):
    st = []
    for i in range(len(q)):
        if q[i] == '[' or q[i] == '{' or q[i] == '(':
            st.append(q[i])
        elif len(st) > 0:
            if (st[-1] == '[' and q[i] == ']') or (st[-1] == '{' and q[i] == '}') or (st[-1] == '(' and q[i] == ')'):
                st.pop()
        else:
            return False

    if len(st) == 0: return True
    else: return False


def solution(s):
    answer = 0
    
    q = deque(s)
    for x in range(len(s)):
        if chk(q):
            answer += 1

        q.rotate(-1)
    return answer