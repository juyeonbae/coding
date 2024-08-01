# 첫번째 풀이

def solution(numbers, hand):
    answer, tl, tr = '', [[3, 0]], [[3, 2]]

    # 키패드 배열
    arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    # 왼손 키, 오른손 키
    left_key, right_key = [1,4,7], [3,6,9]

    for n in numbers:
        for i in range(4):
            for j in range(3):
                if arr[i][j] == n:
                    if n in left_key:
                        answer += 'L'
                        tl.append([i, j])
                    elif n in right_key:
                        answer += 'R'
                        tr.append([i, j])
                    else:
                        left = abs(tl[-1][0] -i) + abs(tl[-1][1] - j)
                        right = abs(tr[-1][0] -i) + abs(tr[-1][1] - j)

                        if left > right:
                            answer += 'R'
                            tr.append([i, j])
                        elif left < right:
                            answer += 'L'
                            tl.append([i, j])
                        else:
                            if hand == 'right':
                                answer += 'R'
                                tr.append([i, j])
                            else:
                                answer += 'L'
                                tl.append([i, j])

    return answer


# 두번째 풀이

def solution(numbers, hand):
    answer = ''
    left_pos, right_pos = [3, 0], [3, 2]
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2], '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    
    left_keys, right_keys = {1, 4, 7}, {3, 6, 9}
    
    for number in numbers:
        pos = keypad[number]
        if number in left_keys:
            answer += 'L'
            left_pos = pos
        elif number in right_keys:
            answer += 'R'
            right_pos = pos
        else:
            left_dist = abs(left_pos[0] - pos[0]) + abs(left_pos[1] - pos[1])
            right_dist = abs(right_pos[0] - pos[0]) + abs(right_pos[1] - pos[1])
            
            if left_dist < right_dist:
                answer += 'L'
                left_pos = pos
            elif left_dist > right_dist:
                answer += 'R'
                right_pos = pos
            else:
                if hand == 'right':
                    answer += 'R'
                    right_pos = pos
                else:
                    answer += 'L'
                    left_pos = pos
                    
    return answer