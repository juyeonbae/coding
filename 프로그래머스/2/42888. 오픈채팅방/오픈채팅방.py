def solution(records):
    answer = []
    tmp = []
    d = {}
    for record in records:
        arr = list(record.split(" "))
        
        if len(arr) == 2:
            state, user = arr[0], arr[1]
        else:
            state, user, name = arr[0], arr[1], arr[2]
            d[user] = name 
        
        if state == 'Enter':
            tmp.append((user, "님이 들어왔습니다."))
            
        elif state == 'Leave':
            tmp.append((user, "님이 나갔습니다."))
            
    for i, txt in tmp:
        x = d[i] + txt
        answer.append(x)
    
    return answer