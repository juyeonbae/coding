def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        can_speak = True
        prev = ''
        idx = 0 
        
        while idx < len(word):
            found = False
            
            for sound in sounds:
                if word.startswith(sound, idx):
                    # 이전 단어와 같으면, 말할 수 없음
                    if sound == prev:
                        can_speak = False
                        break 
                    
                    # 아닌 경우, 단어 탐색 
                    idx += len(sound)
                    prev = sound
                    found = True
                    break 
                    
            if not can_speak:
                break
                
            if not found:
                can_speak = False
                break
                
        if can_speak:
            answer += 1
        
    return answer