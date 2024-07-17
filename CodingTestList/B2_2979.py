# B2_2979_트럭 주차.py - 32ms

a, b, c = map(int,input().split()) # 분당 요금 

arr = {}
for i in range(3):
    start, end = map(int,input().split())
    
    for j in range(start, end):
        if j not in arr:
            arr[j] = 1
        else:
            arr[j] += 1

answer = 0
for key, value in arr.items():
    if value == 1:
        answer += a
    elif value == 2:
        answer += b * 2
    elif value == 3:
        answer += c * 3

print(answer)


'''
1-2-3--5-6--8
1--------6
    3--5
  2---------8
1-2: 5 * 1 * 1
2-3: 3 * 2
3-5: 1 * 3 * 2

5 3 1 1 1 3 5 5 > 24
5 6 3 3 3 6 5 5 > 36

15-----25--30-----50---70--80
15---------30
       25---------50
                       70--80

15-25 : 10 * 10 = 100
25-30 : 8 * 2 * 5 = 80
30-50 : 10 * 20 = 200
70-80 : 10 * 10 = 100
'''