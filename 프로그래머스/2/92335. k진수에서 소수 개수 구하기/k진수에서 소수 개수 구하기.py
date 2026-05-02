def solution(n, k):
    answer = 0
    
    def convert(num, base):
        result = ''
        while num > 0:
            result = str(num % base) + result
            num //= base
        return result 
    
    arr = [int(x) for x in convert(n, k).split("0") if x]
    
    def isPrime(x):
        if x == 1: return False
        for i in range(2, int(x**0.5+1)):
            if x % i == 0:
                return False
        return True
            
    for a in arr:
        if isPrime(a):
            answer += 1
            
    return answer
        