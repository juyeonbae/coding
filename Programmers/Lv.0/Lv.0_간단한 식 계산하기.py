def solution(b):
  a, op, b = b.split()
  if op == '+': return int(a) + int(b)
  elif op == '-': return int(a) - int(b)
  else: return int(a) * int(b)


#eval 함수 사용 // solution = eval 로 코드 작성 가능 
def solution(b):
  return eval(b)

'''
eval(expression) 함수 
- 문자열로 표현된 식을 인자로 받아 결과값을 반환 
'''
