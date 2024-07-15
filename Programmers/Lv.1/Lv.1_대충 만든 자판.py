def solution(keymap, targets):
    # step 1. 각 문자에 대한 최소 누름 횟수를 저장하는 딕셔너리 생성
    min_dict = {}
    for km in keymap:
        for idx, char in enumerate(km):
            if char not in min_dict:
                min_dict[char] = idx + 1
            else:
                min_dict[char] = min(min_dict[char], idx + 1)

    # step 2. 각 target 문자열에 대한 누름 횟수 계산
    answer = []
    for target in targets:
        tt = 0
        for char in target:
            if char in min_dict:
                tt += min_dict[char]
            else:
                tt = -1
                break
        answer.append(tt)

    return answer
