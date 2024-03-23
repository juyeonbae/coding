def solution(s):
    time,cnt = 0,0
    while True:
        a = ''
        if s == '1': break
        for i in s:
            if i == '0':
                cnt += 1
            else:
                a += i
        s = bin(len(a))[2:]
        time += 1
    return [time,cnt]

'''
3~12번 줄 코드를 다음과 같이 수정하여 시간복잡도를 줄일 수 있다. 
    while s != '1':
        time += 1
        num = s.count('1')
        cnt += len(s) - num
        s = bin(num)[2:]
        
후... 좀 간단하게 생각하지 못하는가...
'''
