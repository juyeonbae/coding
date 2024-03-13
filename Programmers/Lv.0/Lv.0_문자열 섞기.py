#내가 푼 첫 풀이
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer 

#zip 함수 사용 
#zip 함수:  두 개의 리스트를 서로 묶어줄 때 사용
# * 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환

def solution(str1,str2):
    return ''.join(i+j for i,j in zip(str1,str2))
