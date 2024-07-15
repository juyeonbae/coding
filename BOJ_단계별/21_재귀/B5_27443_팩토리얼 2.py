#B5_27443_팩토리얼 2.py

def f(x):
    global factorial
    if x == 0 or x == 1:
        return factorial
    
    factorial *= x
    return f(x-1)

#main
n = int(input())
factorial = 1
print(f(n))
