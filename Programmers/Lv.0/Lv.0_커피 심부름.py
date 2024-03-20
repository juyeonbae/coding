#왜 이렇게 풀었지? 아무튼 count로 풀었다. 굳이긴 싶다. 
def solution(order):
    answer = 0
    for i in order:
        answer += (i.count("cafelatte") * 5000) + (i.count("americano") * 4500) + (i.count("anything") * 4500)
    return answer


#count 안 쓰고 풀기, 이게 더 시간이 빠를 것 같기도 
def solution(order):
    answer = 0
    for i in order:
        if 'latte' in i: 
              answer += 5000
        else:
              answer += 4500
    return answer 
