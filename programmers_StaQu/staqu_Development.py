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
    print(days, "days는")
    # days는 progresses가 걸리는 일 수 
    
    while(days):    
        a = days.pop(0)     
        count = 1       
        if len(days) == 1 :
            answer.append(count)
            break
        if len(days) == 2 :
            if days[0] >= days[1]:
                count = count + 1
                answer.append(count)
            else:
                answer.append(1)
                break
        while(a>=days[0] and not days):            
            days.pop(0)
            count = count + 1
        answer.append(count)
    return answer

    
print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))