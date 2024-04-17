#S4_1158 요세푸스 문제.py

n, k = map(int,input().split())
arr = [i for i in range(1,n+1)]
answer = []
index = 0

while arr:
    index = (index + k -1) % len(arr)
    answer.append(str(arr.pop(index)))
    
#출력
print("<"+", ".join(answer)+">")
