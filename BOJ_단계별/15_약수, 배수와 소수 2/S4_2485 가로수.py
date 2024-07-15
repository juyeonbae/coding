#축약, 정리된 코드
import sys
input = sys.stdin.readline

#gcd
def gcd(a,b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

#main
n = int(input())
arr = [int(input()) for _ in range(n)]
arr2 = [arr[i+1] - arr[i] for i in range(len(arr)-1)]

sum_arr2, set_arr2 = sum(arr2), list(set(arr2))

g = set_arr2[0]
for i in set_arr2:
    g = gcd(g, i)

print(sum_arr2//g - n + 1)

////////////////////////////////
#처음 코드 

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    tree = int(input().strip())
    arr.append(tree)

#간격 계산 
arr2 = []
for i in range(len(arr)-1):
    arr2.append(arr[i+1] - arr[i])

#유클리드 호제법 
def gcd(a,b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

#간격들의 최대공약수 구하기
def gcd_list(arr):
    if len(arr) == 1:
        return arr[0]

    g = gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        g = gcd(g, arr[i])
    return g

g = gcd_list(arr2)

#심어야 하는 나무 개수 
cnt = 0
for i in arr2:
    cnt += i // g - 1

print(cnt)
