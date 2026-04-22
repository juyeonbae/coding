def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        m = -1
        for i in range(s, e+1):
            if arr[i] > k:
                if m < k:
                    m = arr[i]
                m = min(m, arr[i])
        
        answer.append(m)
                
    return answer