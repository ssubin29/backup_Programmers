# 스택/큐 - 기능개발


def solution(progresses, speeds):
    answer = []
    
    for n in range(len(progresses)):
        p = 100-progresses[n]
        s = speeds[n]
        day = p//s
        if day * s < p:
           day = day+1 
        answer.append(day)
    while(progresses):
        progresses.pop()
        print(progresses)
    return answer