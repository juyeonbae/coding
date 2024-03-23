def solution(num):
    answer = []
    n = len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i] + num[j] not in answer:
                answer.append(num[i] + num[j])
    return sorted(answer)
