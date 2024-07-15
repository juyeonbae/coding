def isPrime(x):
    cnt = 0 
    for i in range(2,x):
        if x % i == 0:
            cnt += 1
            break
    return 1 if cnt == 0 else 0

#main
m = int(input())
n = int(input())

prime = []
for i in range(m,n+1):
    if isPrime(i) == 1 and i != 1:
        prime.append(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
