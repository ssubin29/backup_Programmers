# K번째 수

def solution(array, commands):
    answer = []
    
    for command in commands:
        if (command[0]==command[1]):
            answer.append(array[command[0]])
        else : 
            comm = array[command[0]-1:command[1]]
            comm.sort()
            answer.append(comm[command[2]])
            print(comm)
        print(answer)
    return answer