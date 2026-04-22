def solution(arr):
    answer = 0
    tmp = list(arr)
    while True:
        new_arr = tmp[:]
        for i in range(len(tmp)):
            if tmp[i] >= 50 and tmp[i] % 2 == 0:
                new_arr[i] = tmp[i] // 2
            elif tmp[i] < 50 and tmp[i] % 2 != 0:
                new_arr[i] = tmp[i] * 2 + 1
        
        if new_arr == tmp:
            break 
        
        answer += 1
        tmp = new_arr
    
    return answer