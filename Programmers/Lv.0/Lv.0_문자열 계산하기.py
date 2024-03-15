def solution(my_string):
    #return eval(my_string)
    return sum(map(int,my_string.replace(' - ',' + -').split(' + ')))

#eval 함수를 사용하면 인자의 문자식 값을 구해주지만 보안 상 취약하다. 
