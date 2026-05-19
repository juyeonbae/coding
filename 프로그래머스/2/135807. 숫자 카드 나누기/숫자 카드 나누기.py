from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)
    
    answer = 0 
    
    if all(b % gcdA != 0 for b in arrayB):
        answer = max(answer, gcdA)
        
    if all(a % gcdB != 0 for a in arrayA):
        answer = max(answer, gcdB)
            
    return answer