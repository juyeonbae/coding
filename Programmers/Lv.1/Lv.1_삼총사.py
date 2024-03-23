def solution(n):
    answer = 0
    for i in range(len(n)): # 0,1,2,3,4
        for j in range(i+1,len(n)): # 1,2,3,4
            for k in range(j+1,len(n)): #2,3,4
                if n[i]+n[j]+n[k] == 0:
                    answer += 1
    return answer

'''
나는 직관적으로 삼중 반복문을 사용했다. 

from itertools import combinations 를 사용하면 조합을 사용할 수 있다.

for i in combinations(n, 3):
  if sum(i) == 0: 
    answer += 1 
위와 같이 표현 가능하다. 
'''
