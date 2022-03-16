# K번째 수

def solution(array, commands):
    answer = []
    for command in commands:
        if (command[0]==command[1]):
            answer.append(array[command[0]])
        else : 
            answer.append(array[command[0]-1:command[1]-1][2])
    return answer