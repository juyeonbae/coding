def solution(arr, q):
    for i in range(len(q)):
        tmp = arr[q[i][0]]
        arr[q[i][0]] = arr[q[i][1]]
        arr[q[i][1]] = tmp
    return arr

#파이썬은 동시에 두 개 바 수 있다고 하네요..
def solution(arr, queries):
    for a,b in queries: #이차원 배열 원소 표현 방법 기억해두기 
        arr[a],arr[b]=arr[b],arr[a]
    return arr
