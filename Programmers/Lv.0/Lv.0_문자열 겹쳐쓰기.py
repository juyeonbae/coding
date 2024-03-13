def solution(ms, os, s):
    return ''.join(ms[0:s]+os+ms[s+len(os):])

'''
처음에는 겹쳐쓴다해서 replace 함수를 사용했다. 
>> return ms.replace(ms[s:len(os)+s], os) 
이 코드는 테스트케이스 6번을 통과하지 못했다. 다른 사람들도 6번 예제에서 통과를 못했고,
반례로, ms = "aaaaaa", os = "bbb", s = 3 경우가 있었다. 
>> 이 경우 원하는 결과값은 "aaabbb"인데, 실제 출력은 "bbbbbb" 가 나왔다. 

idea
>> 문자열을 replace 하기보다 잘라서 붙이며 되겠다 싶었다. 

question
>> replace로는 풀 수 없는 것인가? 
>>replace는 처음 값을 변환하고 못바꿔서 그렇다는 말을 보았는데 좀더 공부해서 알게 되면 수정해놓겠다. 
'''
