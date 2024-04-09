n = int(input())

while n % 2 == 0:
    print(2)
    n //= 2

i = 3
while i * i <= n:
    if n % i == 0:
        n //= i
        print(i)
    else:
        i += 2

if n > 2:
    print(n)
