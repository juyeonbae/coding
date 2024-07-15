import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append((int(age),i,name))

arr = sorted(arr, key = lambda x: (x[0],x[1]))
for i in arr:
    print(i[0],i[2])
