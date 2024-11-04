import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) >= 2:
            m1 = heapq.heappop(scoville)
            m2 = heapq.heappop(scoville)

            heapq.heappush(scoville, m1 + (m2 * 2))
            answer += 1
        else:
            answer = -1
            break

    return answer