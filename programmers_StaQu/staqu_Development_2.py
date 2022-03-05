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
    print("days는", days)
    # days는 progresses가 걸리는 일 수 
    
    count = 0
    answer.append(1)
    
    for num1, num2 in zip(days, days[1:]):     
        if num1 >= num2 :
            answer[count] = answer[count] + 1
        else:
            answer.append(1)
            count = count+1
            
    return answer