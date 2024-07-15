'''
import sys
input = sys.stdin.readline

n = int(input())

arr = []
while n>=1:
    arr.append(n%10)
    n = n // 10

arr.sort(reverse=True)

answer = ''
for i in arr:
    answer += str(i)

print(''.join(answer))
'''

arr = list(map(int,input()))
arr.sort(reverse=True)

for i in arr:
    print(i,end='')
