def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i: answer+= i
    return answer 

#한 줄 코드 
  def solution(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])
