def solution(arr, itv):
    answer = []
    for i in range(len(itv)):
        answer += arr[itv[i][0]:itv[i][1]+1]
    return answer

'''
처음에는 answer.append() 함수를 사용하니, [[2,3,4],[1,2,3,4,5]] 이렇게 이차원 배열이 만들어졌다. 

0. += 
- 리스트들을 합치는 것이므로 append 보다는 속도가 느리다. 
-ex) [2,3,4] + [1,2,3,4,5] >> [2,3,4,1,2,3,4,5] 로 출력 
1. append() 
- 인자를 리스트에 객체로 집어넣는다. 그래서 이차원 배열이 될 수 밖에 없었다..
2. extend()
- append와 다른 점은 괄호( ) 안에는 iterable 자료형만 올 수 있다. 
- ex) answer.extend([1,2,3,4,5]) >> [2,3,4,1,2,3,4,5] 로 출력 

+ 추가로, 통과 후 다른 사람 풀이를 보았는데,
s1, e1 = intervals[0] // 2차원 배열 중 1행을 의미
s2, e2 = intervals[1] // 2차원 배열 중 2행을 의미
반복문을 사용하지 않고 이렇게 표현할 수도 있었다. 
'''
