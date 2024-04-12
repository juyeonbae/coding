import sys
input = sys.stdin.readline

a, b = map(int,input().split())
x, y = map(int,input().split())

def gcd(f1,f2):
    if f2 > f1:
        f1, f2 = f2, f1

    while f2 > 0:
        f1, f2 = f2, f1 % f2
    return f1

def foun(a, x):
    global b, y, num1
    a = a * (num1 // b)
    x = x * (num1 // y)
    return a + x

num1 = b*y//gcd(b,y) #분모
num2 = foun(a,x) #분자 

#기약분수로 나타내기
fin_gcd = gcd(num1, num2)

print(num2//fin_gcd, num1//fin_gcd)
