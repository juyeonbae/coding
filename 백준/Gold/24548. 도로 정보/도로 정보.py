# 나무 T, 잔디 G, 울타리 F, 사람 P -> 길이 N의 문자열로 표현
# 도로 구간: 도로의 연속된 일부분, 도로의 연속 부분 문자열로 표현
# 흥미로운 구간: 
    # 길이가 1 이상인 도로 구간 중 
    # 그에 속한 모든 물체의 수가 3의 배수

# 흥미로운 구간이 될 수 있는 도로 구간의 개수 구하기 

import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

# 각 물체별 누적 개수의 나머지 상태 (T, G, F, P)
current_state = [0, 0, 0, 0]
mapping = {'T':0, 'G':1, 'F':2, 'P':3}

# 상태별 등장 횟수 저장 (튜플을 키로 사용)
# 초기 상태 (0, 0, 0, 0)은 이미 1번 존재 
state_counts = {(0, 0, 0, 0): 1}

answer = 0 
for char in S:
    # 1. 현재 물체 개수 추가 후 3으로 나눈 나머지 갱신 
    idx = mapping[char]
    current_state[idx] = (current_state[idx] + 1) % 3

    # 2. 튜플로 변환하여 딕셔너리 키로 사용
    state_tuple = tuple(current_state)
    
    # 3. 이전에 같은 상태가 나온 적 있다면, 그 횟수만큼 흥미로운 구간 형성 
    if state_tuple in state_counts:
        # 누적해서 더하는 이유: 
            # 상태 개수만큼 정답 구간이 새로 생긴다. 
        answer += state_counts[state_tuple]
        state_counts[state_tuple] += 1
    else:
        state_counts[state_tuple] = 1 

print(answer)