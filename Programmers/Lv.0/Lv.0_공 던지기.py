#deque.rotate로 풀었다. 
from collections import deque
def solution(numbers, k):
    dq = deque(numbers)
    dq.rotate(-2 * (k-1))
    return dq[0]


#수학적으로 풀기, 한 명 건너뛰고 공을 던지니까 2, k번째 공을 던진 사람을 구하므로 k-1, 총인원수로 나눔 len(numbers)
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]
