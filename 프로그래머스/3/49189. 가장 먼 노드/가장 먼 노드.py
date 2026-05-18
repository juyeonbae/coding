from collections import deque 

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n+1)
    distance[1] = 0 
    
    q = deque([1])
    
    while q:
        now = q.popleft()
        
        for nxt in graph[now]:
            if distance[nxt] == -1:
                distance[nxt] = distance[now] + 1
                q.append(nxt)
                
    max_dist = max(distance)
    return distance.count(max_dist)