def change(n, t, m):
    result = '0'
    chars = "0123456789ABCDEF" 
    for i in range(t*m+1):
        tmp = ''
        while i > 0:
            tmp = chars[i % n] + tmp
            i //= n 
            
        result += tmp
    return result

def solution(n, t, m, p):
    answer = ''
    arr = change(n, t, m)
    for i in range(p-1, m*t, m):
        answer += arr[i]
        
    return answer