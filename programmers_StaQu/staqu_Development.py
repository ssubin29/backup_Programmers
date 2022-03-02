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
        if len(days) < 2 :
            print('days가 비어있습니다')
            answer.append(count)
            break
        while(a>=days[0]):
            if not len(days) > 0:
                print('두번째 while문을 나갑니다')
                break
            days.pop(0)
            print(days)
            count = count + 1
        answer.append(count)
        print(days)
    return answer

print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))
