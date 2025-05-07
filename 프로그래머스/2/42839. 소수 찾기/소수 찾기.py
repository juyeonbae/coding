from itertools import permutations

def solution(numbers):
    answer, per = [], []
    nums = [n for n in numbers]
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))
    new_nums = [int("".join(p)) for p in per]
    
    for n in new_nums:
        if n < 2:
            continue
        chk = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                chk = False
                break
        if chk:
            answer.append(n)
            
    return len(set(answer))