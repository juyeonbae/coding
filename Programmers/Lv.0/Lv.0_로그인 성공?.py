def solution(id_pw, db):
    for i in range(len(db)):
        if id_pw[0] != db[i][0]:
            if id_pw[1] != db[i][1]:
                answer = "fail"
        else:
            if id_pw[1] != db[i][1]:
                answer = "wrong pw"
            else:
                answer = "login"
                
    return answer

'''
사용하는 조건문 수를 줄이는 방법
def solution(id_pw,db):
    answer = 'fail'
    for x,y in db:
        if id_pw[0] == x:
            if id_pw[1] == y:
                answer = 'login'
            else:
                answer = 'wrong pw'
    return answer

    '''
