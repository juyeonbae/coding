def solution(number):
    return int(number) % 9 # test 21 56.05ms
    #return sum(map(int,number)) % 9 << test 21 20.63ms


'''
문자열을 정수로 바꾼 후 9로 나누면, 시간이 오래 걸린다. 
문자열을 int로 쪼개고 합한 후 9로 나누는 방법이 시간이 덜 걸린다. 
'''
