def solution(ms, alp):
    return ms.replace(alp,alp.upper())

#return ms.replace(alp,alp.upper()) if alp in ms else ms 라고 풀었는데, 굳이 조건문 없어도 alp가 있는 경우만 replace한다. 
