import heapq

def solution(book_time):
    times = []
    
    # 1. 시간 변환
    for s, e in book_time:
        sh, sm = map(int, s.split(":"))
        eh, em = map(int, e.split(":"))
        
        start = sh * 60 + sm
        end = eh * 60 + em + 10 
        
        times.append((start, end))
    
    # 2. 시작 시간 기준 정렬 
    times.sort()  
    
    # 3. 힙
    heap = []
    for start, end in times:
        # 방 재사용 
        if heap and heap[0] <= start:
            heapq.heappop(heap)
            
        heapq.heappush(heap, end)
    
    return len(heap)