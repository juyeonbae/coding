def solution(A, B):
    return [[sum(a * b for a, b in zip(row, col)) 
             for col in zip(*B)] 
             for row in A]