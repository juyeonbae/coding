n = int(input())
arr = list(map(int,input().split()))

def isPrime(x):
    cnt = 0 
    for i in range(2,x):
        if x % i == 0:
            cnt += 1
    return 1 if cnt == 0 else 0

#main
result = 0
for i in arr:
    if isPrime(i) == 1 and i != 1:
        result += 1

print(result)
