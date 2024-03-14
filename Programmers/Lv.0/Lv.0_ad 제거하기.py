def solution(strArr):
    answer = []
    for i in strArr:
        if "ad" not in i: answer.append(i)
    return answer

#한줄 코드
def solution(strArr):
  return [s for s in strArr if "ad" not in s]
