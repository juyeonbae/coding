#수학계산으로 풀기 O(n)
def solution(n):
    answer = []
    for i in range(len(str(n))):
        answer.append(n//(10**i)%10)
    return answer

#문자열로 변환해서 함수 쓰기
def solution2(n):
  return list(map(int,reversed(str(n))))
