import heapq


def solution(k, score):
    answer = []
    min_heap = []

    for s in score:
        heapq.heappush(min_heap, s)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

        answer.append(min_heap[0])

    return answer
