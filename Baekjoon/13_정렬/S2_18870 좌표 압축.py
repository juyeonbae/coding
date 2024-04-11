import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

sort_arr = sorted(set(arr)) 

idx_dict = {sort_arr[i]:i for i in range(len(sort_arr))}

for i in arr:
    print(idx_dict[i], end=' ')
