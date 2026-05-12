def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0 
    for i in range(len(A)):
        while j < len(B):
            if A[i] < B[j]:
                answer += 1
                j += 1
                break
            j += 1
                
    return answer