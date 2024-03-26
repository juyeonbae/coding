#그냥 replace 반복으로 품 
#replace 시간 복잡도 
#O(문자열의 길이 * (교체할 문자열의 길이 + 교체되는 문자열의 길이/교체할 문자열의 길이))

def solution(s):
    s = s.replace('zero','0')
    s = s.replace('one','1')
    s = s.replace('two','2')
    s = s.replace('three','3')
    s = s.replace('four','4')
    s = s.replace('five','5')
    s = s.replace('six','6')
    s = s.replace('seven','7')
    s = s.replace('eight','8')
    s = s.replace('nine','9')
    return int(s)

'''
딕셔너리 사용해서 푸는 방법 >> 시간복잡도 우려 
def solution(s):
    nums = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    for key, value in nums.items():
        s = s.replace(key,value)

    return int(s)


#리스트로 만들어서 인덱스와 replace
def solution(s):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(num)):
        s = s.replace(num[i],str(i))
    return int(s)
'''
        
