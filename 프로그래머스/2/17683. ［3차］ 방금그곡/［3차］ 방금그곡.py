import re

def solution(m, musicinfos):
    arr = []
    
    m_list = re.findall(r'[A-G]#?', m)
    
    for idx, info in enumerate(musicinfos):
        st, et, title, music = info.split(",")
        
        sh, sm = map(int, st.split(":"))
        eh, em = map(int, et.split(":"))
        
        time = (eh * 60 + em) - (sh * 60 + sm)
                
        music_list = re.findall(r'[A-G]#?', music)
        
        # 재생 시간만큼 음악 늘리기
        played = []
        for i in range(time):
            played.append(music_list[i % len(music_list)])
        
        # 멜로디 포함 여부 확인
        chk = False
        
        for i in range(len(played) - len(m_list) + 1):
            if played[i:i+len(m_list)] == m_list:
                chk = True
                break 
                
        if chk:
            arr.append([time, idx, title])
            
    arr.sort(key=lambda x: (-x[0], x[1]))
        
    return arr[0][2] if arr else "(None)"
        
        