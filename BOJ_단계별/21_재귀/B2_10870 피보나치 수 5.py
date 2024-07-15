#B2_10870 피보나치 수 5.py

def f(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1

    return f(x-1) + f(x-2)

#main
n = int(input())
print(f(n))
