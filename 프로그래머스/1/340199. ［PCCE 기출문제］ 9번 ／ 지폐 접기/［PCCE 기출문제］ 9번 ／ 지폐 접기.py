def fold(n, cnt):
    return n // 2, cnt + 1

def solution(wallet, bill):
    answer = 0
    
    # wallet 과 대소비교 
    max_wallet = max(wallet)
    min_wallet = min(wallet)
    max_bill = max(bill)
    min_bill = min(bill)
    
    while max_wallet < max_bill or min_wallet < min_bill:
        if max_wallet < max_bill or min_wallet < min_bill:
            max_bill //= 2
            answer += 1
            max_bill, min_bill = max(max_bill, min_bill), min(max_bill, min_bill)
            
    
    
    return answer