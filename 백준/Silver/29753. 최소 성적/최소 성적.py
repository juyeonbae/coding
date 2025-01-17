from decimal import Decimal, ROUND_FLOOR
import sys

input = sys.stdin.readline

grade = {'A+': Decimal('4.50'), 'A0': Decimal('4.00'), 'B+': Decimal('3.50'), 
         'B0': Decimal('3.00'), 'C+': Decimal('2.50'), 'C0': Decimal('2.00'), 
         'D+': Decimal('1.50'), 'D0': Decimal('1.00'), 'F': Decimal('0.00')}

N, X = input().split()
N, X = int(N), Decimal(X)

cnt, score = 0, 0
for i in range(N-1):
    c, g = input().split()
    score += Decimal(c) * grade[g]
    cnt += int(c)

L = int(input())
cnt += L

answer = 'impossible'
for k, v in grade.items():
    tmp = (score + (v * L)) / cnt
    tmp = tmp.quantize(Decimal('0.01'), rounding=ROUND_FLOOR)
    if tmp > X:
        answer = k

print(answer)