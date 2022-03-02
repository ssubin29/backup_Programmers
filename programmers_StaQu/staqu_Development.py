# 스택/큐 - 기능개발

def solution(progresses, speeds):
    answer = []
    days = []
    
    for n in range(len(progresses)):
        p = 100-progresses[n]
        s = speeds[n]
        day = p//s
        if day * s < p:
           day = day+1 
        days.append(day)
    
    while(days):
        
        if len(days) <= 1:
            break
            
        a = days.pop(0)
        print(a)
        count = 1
        
        while(a>=days[0]):
            days.pop(0)
            count = count + 1
        answer.append(count)
                        
    return answer

solution([93, 30, 55], [1, 30, 5])