def solution(sides):
    #개수 
    cnt = 0

    #가장 긴 변이 sides 배열에 있는 경우
    max_length = max(sides)

    for i in range(1,max_length+1):
        if min(sides) + i > max_length:
            cnt += 1    

    #가장 긴 변이 나머지 한 변일 경우
    cnt += sum(sides) - max(sides) - 1 #중복 하나 
    
    return cnt

'''
#위의 코드 정리 
나머지 한 변을 n 이라고 가정했을 때, 
1) n이 가장 긴 변일 경우
>> sum(sides) > n > max(sides) >> n의 개수 : sum(sides) - max(sides)
2) 아닌 경우
>> max(sides) > n > max(sides) - min(sides) >> n의 개수 : max(sides) - (max(sides) - min(sides)) >> min(sides) 

위의 경우를 더하고 식을 정리하면 n 이 될 수 있는 변의 개수
>> sum(sides) - max(sides) + min(sides) - 1 (1,2 경우에서 중복되는 값) 
'''
