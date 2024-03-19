#내가 푼 풀이 - 부울 연산 기호를 몰랐다. ㅠㅠ~
def solution(x1, x2, x3, x4):
    if (x1 == False and x2 == False) or (x3 == False and x4 == False):
        return False
    else: return True

#이렇게나 간단한 풀이였다 ㅠㅠ~
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)
