#첫 풀이(에러났던 풀이) - IndexError: list index out of range
def solution(arr):
    answer = []
    arr2 = sorted(arr)
    
    for i in range(len(arr)):
        if arr2[0] == arr[i]:
            arr.pop(i)
            
    return [-1] if len(arr) < 1 else arr
'''
arr.pop(i) 수행하면 리스트에서 요소를 삭제하고 반환해서 리스트 길이가 줄어들고, 반복문이 유효한 인덱스 범위를 벗어나게 됨 
'''

#첫번째 풀이 수정 방법 1 - 배열 정렬하고, 원래 배열과 비교하며 다르면 answer 배열에 추가
def solution(arr):
    answer = []
    arr2 = sorted(arr)
    
    for i in range(len(arr)):
        if arr2[0] != arr[i]:
            answer.append(arr[i])
            
    return [-1] if len(arr) == 1 else answer

# 첫번째 풀이 수정 방법 2 - 루프를 반대로 돌리기, 또는 오른쪽과 같이 break 후 pop 가능 
def solution(arr):
    answer = []
    arr2 = sorted(arr)
    
    for i in range(len(arr)-1,-1,-1):    #for i in range(len(arr)):
        if arr2[0] == arr[i]:                #if arr2[0] == arr[i]: 
            arr.pop(i)                            #break
                                         #arr.pop(i) 
    return [-1] if len(arr) < 1 else arr
#-------------------------------------------------------------------------------------

#두번째 풀이 - 배열을 정렬할 필요없이 min 함수로 리스트 중 최소값을 찾고, 리스트.index() 함수로 최소값의 인덱스를 찾아서 pop 
def solution(arr):
    arr.pop(arr.index(min(arr)))
    return [-1] if len(arr) < 1 else arr


