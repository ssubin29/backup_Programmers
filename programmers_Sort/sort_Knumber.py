# K번째 수

def solution(array, commands):
    answer = []
    
    a=[2,5,1,6,3,4]
    print(a[3:4])
    
    for command in commands:
        if (command[0]==command[1]):
            #answer.append(array[command[0]]
            print(1)
        else : 
            #answer.append(array[command[0]-1:command[1]][command[2]])
            print(0)
    return answer