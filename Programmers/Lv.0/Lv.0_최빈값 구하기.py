def solution(array):
    ans = [0] * 1000
    for i in array:
        ans[i] += 1
        
    return -1 if ans.count(max(ans)) > 1 else ans.index(max(ans))
