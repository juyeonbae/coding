def solution(order):
    answer = 0
    now = 1
    arr = [i for i in range(1, len(order)+1)] 
    st = [] # 보조 컨베이어 벨트 
    
    i, idx = 0, 0
    while i < len(order):
        if arr[i] == order[idx]: 
            answer += 1
            i += 1
            idx += 1
            
        elif st and st[-1] == order[idx]:
            answer += 1
            idx += 1
            st.pop() 
            
        else:
            st.append(arr[i])
            i += 1
            
    for j in range(len(st)):
        if st[-1] == order[idx]:
            idx += 1
            answer += 1
            st.pop() 
        
 
    return answer