from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0 
    
    def can_change(word1, word2):
        count = 0 
        for a, b in zip(word1, word2):
            if a != b:
                count += 1
        return count == 1
    
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    
    while q:
        word, step = q.popleft() 
        
        if word == target:
            return step 
        
        for i in range(len(words)):
            if not visited[i] and can_change(word, words[i]):
                visited[i] = True 
                q.append((words[i], step+1))
        
    return 0