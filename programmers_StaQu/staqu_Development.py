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
        a = days.pop(0)     
        count = 1       
        if not days :
            print('days가 비어있습니다')
            break
        print(a, days[0])
        while(a>=days[0]):
            if not len(days) > 0:
                break
            days.pop(0)
            count = count + 1
        answer.append(count)
        print(days)
    return answer


solution([93, 30, 55], [1, 30, 5])