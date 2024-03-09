#240309 프로그래머스 Lv.1 K번째 수 
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(sorted(array[commands[i][0]-1: commands[i][1]])[commands[i][2]-1])
    return answer


#test

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]


answer = []
for i in range(len(commands)):
    answer.append(sorted(array[commands[i][0]-1: commands[i][1]])[commands[i][2]-1])
print(answer)
    
        
