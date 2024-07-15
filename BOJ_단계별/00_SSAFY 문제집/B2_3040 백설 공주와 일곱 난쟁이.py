def find(arr,x):
    for i in range(9):
        for j in range(i+1,9):
            if sum(arr) - (arr[i] + arr[j]) == 100:
                for k in range(9):
                    if k != i and k != j:
                        x.append(arr[k])
                return x

#main
arr = []
for i in range(9):
    arr.append(int(input()))

x = []
check = find(arr, x)

for n in check:
    print(n)

'''
idea
1. 전체 합을 구한다. 
2. 전체 합 - 100 = 값을 구해서,
3. 9개의 n 값 중 2개를 골라 값이 같으면
그거만 빼고 출력 . 
'''

arr = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(i+1,9):
        if sum(arr) - (arr[i]+arr[j]) == 100:
            x, y = i, j
            break
arr.pop(y); arr.pop(x)
for i in arr:
    print(i)
