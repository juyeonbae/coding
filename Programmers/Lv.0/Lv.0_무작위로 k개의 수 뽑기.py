#슈도코드 따라 풀이한 코드 
def solution(arr, k):
    answer = []
    cnt = 0

    for i in range(len(arr)):
        if cnt == k: break
        if arr[i] not in answer:
            answer.append(arr[i])
            cnt += 1

    if len(answer) < k:
        for j in range(k-len(answer)):
            answer.append(-1)
            cnt += 1
            
    return answer

#코드 간결하 정리 
answer = []

for i in arr:
    if i not in answer:
        answer.append(i)
    if len(answer) == k:
        break
    
return answer + [-1] * (k-len(answer))

