def solution(arr, q):
    for n in q:
        s, e = n
        for i in range(s,e+1):
            arr[i] += 1
    return arr
