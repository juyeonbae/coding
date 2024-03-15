#내가 푼 풀이 
def solution(arr):
    x = ''
    for i in arr:
        x += str(i)
    return x.count('7')

'''
1) list에다가 str 씌우면 원소가 str 형이 된다. 
>>> return str(arr).count('7')

2) map 함수로 str 형으로 쪼개주기 
>>> return ''.join(map(str,arr)).count('7')
'''
