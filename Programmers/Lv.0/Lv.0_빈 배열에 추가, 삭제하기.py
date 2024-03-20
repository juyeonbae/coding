#생각난대로 풀기, 시간복잡도 O(n^2)
def solution(arr, flag):
    stack = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i] * 2):
                stack.append(arr[i])
        else:
            for j in range(arr[i]):
                stack.pop()
    return stack

#line 6, 7 을 다음과 같이 줄여서 작성할 수 있음
#>> stack += [arr[i]] * (arr[i]*2)
