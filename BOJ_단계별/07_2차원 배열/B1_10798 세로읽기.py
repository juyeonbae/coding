arr = []
for j in range(5):
    arr.append(input())

answer = ''
for i in range(15):  #각 줄의 글자 인덱스 
    for j in range(5):
        if i < len(arr[j]):  #각 글자 길이보다 작은 경우만
            answer += arr[j][i]
    
print(answer)
