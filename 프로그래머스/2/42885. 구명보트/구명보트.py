def solution(people, limit):
    people.sort()  # 오름차순 정렬
    left = 0  # 가장 가벼운 사람의 인덱스
    right = len(people) - 1  # 가장 무거운 사람의 인덱스
    boats = 0
    
    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람을 함께 태울 수 있는 경우
        if left < right and people[left] + people[right] <= limit:
            left += 1
            right -= 1
        # 무거운 사람 혼자 태우는 경우
        else:
            right -= 1
        boats += 1
    
    return boats