def solution(sizes):
    big = [] #각 배열마다 큰 값 비교할 리스트
    small = [] #각 배열마다 작은 값 비교할 리스트
    for i,j in sizes:
        big.append(max(i,j))
        small.append(min(i,j))
    return max(big) * max(small)
