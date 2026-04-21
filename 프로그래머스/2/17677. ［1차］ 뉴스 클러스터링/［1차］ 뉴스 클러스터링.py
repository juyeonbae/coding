def change(word):
    s = []
    for i in range(len(word)-1):
        if word[i].isalpha() and word[i+1].isalpha():
            tmp = word[i].lower() + word[i+1].lower()
            s.append(tmp)
    return s

from collections import Counter
def solution(str1, str2):
    answer = 0 
    
    s1 = change(str1)
    s2 = change(str2)
    
    print(s1, s2)

    x = list((Counter(s1)&Counter(s2)).elements())
    y = list((Counter(s1)|Counter(s2)).elements())
    
    print(x, y)
    if not y: jkd = 1
    else: jkd = len(x) / len(y)
    
    print(jkd)
        
    return int(jkd * 65536) 
