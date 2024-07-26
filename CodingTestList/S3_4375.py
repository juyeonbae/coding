import sys

def num(n):
    one = 1 % n
    length = 1
    while one != 0:
        one = (one * 10 + 1) % n # 상수 계산 -> O(1)
        length += 1
    return length


for n in sys.stdin: # O(N)
    n = n.strip()
    if n == '':
        break
    print(num(int(n)))



'''
import sys

for n in sys.stdin: # 입력의 종료 조건을 모를 때 
    n = n.strip()
    
    if n == '': # if문으로 공백이 들어왔을 때 종료해준다. 
        break
        
    one = '1' * len(n)
    while True:
        if int(one) % int(n) == 0:
            print(len(one))
            break
        else:
            one += '1'
'''