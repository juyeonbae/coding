def solution(files):
    answer = []
    
    tmp = []
    for file in files:
        head_end, num_end = 0, 0 
        while head_end < len(file) and not file[head_end].isdigit():
            head_end += 1
        
        num_end = head_end 
        
        while num_end < len(file) and file[num_end].isdigit():
            num_end += 1
            
        head = file[:head_end]
        number = file[head_end:num_end]
        tail = file[num_end:]
        
        tmp.append([head, number, tail])
    
    tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1])))
    
    for t in tmp:
        answer.append(''.join(t))
        
    return answer