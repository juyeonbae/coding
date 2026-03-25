import sys
input = sys.stdin.readline 

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

# 알파벳 순으로 
# 최소 한 개의 모음, 최소 두 개의 자음 포함 
lst = []
visited = [False] * C

def backtrack(num):
    # 종료 조건
    if len(lst) == L:
        v_count = 0 
        for char in lst:
            if char in "aeiou":
                v_count += 1
        c_count = len(lst) - v_count
        if v_count >= 1 and c_count >= 2:
            print(''.join(lst))
        return 

    # for 반복 in 선택 가능한 리스트:
    for i in range(num, C):
        if visited[i]:
            continue
            
        visited[i] = True
        lst.append(arr[i])

        # 백트래킹
        backtrack(i+1) 
    
        # 선택 취소 
        visited[i] = False
        lst.pop()


backtrack(0)