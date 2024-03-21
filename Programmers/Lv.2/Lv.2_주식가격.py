def solution(p):
    answer = []
    # i = 0,1,2,3,4
    for i in range(len(p)): 
        cnt = 0 #몇 초간 유지했는지 
        # j = (i=0일때,1,2,3,4),(i=1일때 2,3,4)
        for j in range(i+1,len(p)):
            # p[2,3,2,3] - p[1] = 1,2,1,2 cnt = 4
            if p[j] >= p[i]: 
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer

#stack이나 큐로 풀어야 하는데 어떻게 푸는지 모르겠다. 
