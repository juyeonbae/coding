import heapq

def solution(n, k, enemy):
    heap = []
    
    for i in range(len(enemy)):
        n -= enemy[i]
        
        heapq.heappush(heap, -enemy[i])
        
        if n < 0:
            if k == 0:
                return i 
            
            n += -heapq.heappop(heap)
            k -= 1 
            
    return len(enemy)
    