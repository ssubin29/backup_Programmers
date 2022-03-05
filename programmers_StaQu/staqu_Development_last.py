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

    answer.append(1)  
    
    # 차례대로 비교하며 num1 >= num2일 경우 그 값을 시발....
    for i, (num1, num2) in enumerate(zip(days, days[1:])):
        max_value = max(days[:i+1])
        if num1 >= num2 or max_value >= num2 :
            answer[-1] = answer[-1] + 1
        else:
            answer.append(1)
    
    #뭐가 잘못되었는지 알겠다.....
    return answer