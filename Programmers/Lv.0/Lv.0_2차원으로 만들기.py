def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        answer.append(num_list[i:i+n])
    return answer

'''
2차원 배열 만들기

1) 원소 하나씩 입력 받기
arr = [for i in range(n)]
for i in range(n): 
    arr[i] = list(map(int,input().split()))

2) 원소에 list 추가하기 
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

3) 선언과 동시에 입력 받기
arr = [list(map(int,input().split())) for i in range(n)]
'''
