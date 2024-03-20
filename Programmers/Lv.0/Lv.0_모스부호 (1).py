def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    return ''.join(morse[i] for i in letter.split())  #리스트 컴프리헨션 대신 제너레이터 표현식을 사용
  
'''
  join 함수 안에 대괄호 있고 없고 차이 설명
  return ''.join([morse[i] for i in letter.split()])
  >>이 코드는 리스트 컴프리헨션을 사용하여 문자열을 Morse 부호로 변환
  >>letter.split(' ')는 공백을 기준으로 문자열을 나누고, 그 결과를 리스트로 반환
  >>그런 다음 리스트 컴프리헨션은 각 문자를 Morse 부호로 변환하고, 이를 다시 하나의 문자열로 결합
  
  메모리 사용량 차이
  리스트 컴프리헨션은 결과를 리스트에 저장하여 메모리를 더 많이 사용할 수 있다. 
  반면 제너레이터 표현식은 각 요소를 순회하면서 필요한 만큼의 값만 생성하므로 메모리 사용량이 더 적다. 
  '''
