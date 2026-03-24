import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

password = [] 
visited = [False] * len(arr)
vowels = {'a', 'e', 'i', 'o', 'u'}

# 추가 조건) 모음 최소 1개, 자음 최소 2개 

def backtrack(num):
    pass
    # 종료 조건 
    if len(password) == L:
        password_set = set(password)
        v_count = len(password_set & vowels)
        c_count = len(password) - v_count

        if v_count >= 1 and c_count >= 2:
            print("".join(password))
        return

    # for 선택지 in 가능한 후보들: 
    for i in range(num, len(arr)):
        if visited[i]:
            continue
            
        # 선택할 수 있다면 선택 
        visited[i] = True
        password.append(arr[i])

        # backtrack()
        backtrack(i+1)
        
        # 선택 취소
        visited[i] = False 
        password.pop()
        
# 정답 출력 
backtrack(0)