arr = []
maxNum = 0
row,col = 0,0

for i in range(9):
    arr.append(list(map(int,input().split())))
    for j in range(9):
        if arr[i][j] > maxNum:
            maxNum = arr[i][j]
            row,col = i,j

print(maxNum)
print(row+1,col+1)
