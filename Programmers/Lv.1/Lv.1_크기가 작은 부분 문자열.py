def solution(t, p):
    answer = 0
    arr = []
    for i in range(len(t)-len(p)+1): 
        arr.append(t[i:i+len(p)]) 

    for i in arr:
        if p >= i:
            answer += 1
    return answer

'''
굳이 새로운 반복문을 만들 필요 없이 바로 answer에 +1 해도 된다. 
for i in range(len(t)-len(p)+1): 
    if int(p) >= int(t[i:i+len(p)]):
        answer += 1
'''
