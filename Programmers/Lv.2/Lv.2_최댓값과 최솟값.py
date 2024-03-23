def solution(s):
    s = list(map(int,s.split()))
    minX, maxX = min(s), max(s)
    return str(minX)+" "+str(maxX)


'''
마지막 두 줄 합쳐서
return str(min(s)) + ' ' + str(max(s)) 
가능
'''
