# S1_1629_곱셈.py

def dac(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (dac(a, b//2, c)**2) % c
    else:
        return (dac(a, (b // 2), c)**2 % c) * a % c


# main
a, b, c = map(int, input().split())
answer = dac(a, b, c)
print(answer)
