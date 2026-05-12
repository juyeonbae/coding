def solution(babbling):
    answer = 0
    
    for b in babbling:
        b = b.replace("aya", " ")
        b = b.replace("ye", " ")
        b = b.replace("woo", " ")
        b = b.replace("ma", " ")
        
        b = b.replace(" ", "")
        if len(b) == 0:
            answer += 1
    return answer