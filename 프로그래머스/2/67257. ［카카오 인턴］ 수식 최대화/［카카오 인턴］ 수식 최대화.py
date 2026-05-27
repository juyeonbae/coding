import re
from itertools import permutations

def solution(expression):
    answer = 0
    
    # 1. 숫자, 연산자 분리 
    nums = list(map(int, re.findall(r'[0-9]+', expression)))
    ops = re.findall(r'[\+\-\*]', expression)
    
    # 2. 연산자 우선순위
    p = list(permutations(set(ops), len(set(ops))))

    # 3. 우선순위별 연산 
    for order in p:
        cur_nums = nums[:]
        cur_ops = ops[:]
        
        for op in order:
            new_nums = [cur_nums[0]]
            new_ops = []
            
            for i in range(len(cur_ops)):
                if cur_ops[i] == op:
                    a = new_nums.pop()
                    b = cur_nums[i+1]
                    
                    if op == '+':
                        new_nums.append(a+b)
                        
                    elif op == '-':
                        new_nums.append(a-b)
                        
                    else:
                        new_nums.append(a*b)
                        
                else:
                    new_ops.append(cur_ops[i])
                    new_nums.append(cur_nums[i+1])
                    
            cur_nums = new_nums
            cur_ops = new_ops
            
        answer = max(answer, abs(cur_nums[0]))
                    
    return answer