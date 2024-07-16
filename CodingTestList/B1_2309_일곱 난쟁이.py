# B1_2309_일곱 난쟁이.py
from itertools import combinations as c

arr = []
for _ in range(9):
    arr.append(int(input()))

# 일곱 난쟁이 합 == 100 
# tmp = list(c(arr,7)) for문과 combinations 합쳐서 작성할 수 있음 
#for i in tmp:

for i in c(arr, 7):
    if sum(i) == 100:
        answer = list(i)

answer.sort()
for i in answer:
    print(i)
