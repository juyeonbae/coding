def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        answer += str(n).count(str(k))
    return answer

'''
i = 1, j = 13, k = 1 일 경우, 1 ~ 13까지 1이 들어가는 수는 1,10,11,12,13이다.
11에는 1이 두 번 들어가므로 반환값은 6이여야 한다. 

처음에는 if str(k) in str(i) 로 했으나, 11의 상황을 해결해주지 못했다. 
>> count 함수를 사용해서 k의 개수를 구했다. 
'''
