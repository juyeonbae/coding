def solution(arr, q):
    for s,e,k in q:
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
    return arr

# k = 0 인 테스트케이스가 추가된다면, 아래와 같이 하면 되지 않을까? 라는 생각 
def solution(arr, q):
    for s,e,k in q:
        for i in range(s,e+1):
            if k == 0: continue
            elif i % k == 0:
                arr[i] += 1
    return arr
