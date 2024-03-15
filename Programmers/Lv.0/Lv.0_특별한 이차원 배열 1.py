def solution(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

'''
기본 프로그래머스 함수 셋팅이 answer = [[]]로 되어있어서 2차원 배열 선언하는데 애를 먹었다. 
answer = [[0] * n ] * n shallow copy 진행하고, 배열 내의 요소들이 같은 객체를 가리키게 된다. 
>>> 하나만 바꿔도 [[1,1,1],[1,1,1],[1,1,1]] 이렇게 출력되었다. 

  answer=[[0]*n for i in range(n)]
  for i in range(n): answer[i][i]=1

이 식을 축약해서 작성한 것이 맨위의 식인데, 배열을 초기화하고, 반복을 한 번만 돌리는 것이 시간이 덜 걸린다고 한다. 
이차원 배열이 손에 안 익어서 하루종일 잡고 있었네 -_-;;
'''
