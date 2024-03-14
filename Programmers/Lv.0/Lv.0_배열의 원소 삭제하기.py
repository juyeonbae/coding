def solution(arr, d):
  answer = [] 
  for i in arr:
    if i not in d: answer.append(i)
  return answer

#코드 줄여서 
def solution(arr, d):
    return [i for i in arr if i not in d]
