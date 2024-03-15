from collections import deque
def solution(n, d):
    dq = deque(n)
    if d == 'right':
        dq.rotate(1) # >> 이 방향으로 1만큼 rotate
    else: dq.rotate(-1) # << 이 방향으로 1만큼 rotate
    return list(dq)

'''
from collections import deque 
dq = deque(인자)
dq.rotate(x)
- x 값이 양수면 오른쪽으로 x 값만큼 rotate
- x 값이 음수면 왼쪽으로 x 값만큼 rotate
'''
