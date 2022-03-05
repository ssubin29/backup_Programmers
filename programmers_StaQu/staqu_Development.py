# # 스택/큐 - 기능개발

# def solution(progresses, speeds):
#     answer = []
#     days = []
    
#     for n in range(len(progresses)):
#         p = 100-progresses[n]
#         s = speeds[n]
#         day = p//s
#         if day * s < p:
#            day = day+1 
#         days.append(day)
#     print(days, "days는")
#     # days는 progresses가 걸리는 일 수 
    
#     while(days):    
#         a = days.pop(0) 
#         count = 1  
#         if(a>=days[0]):
#             count = count+1
#         else:
#             answer.append(count)
#         if len(days) == 1 :
#             answer.append(count)
#             break
#         elif len(days) == 2 :
#             if days[0] >= days[1]:
#                 count = count + 1
#                 answer.append(count)
#             else:
#                 answer.append(1)
#                 break
#         while(a>=days[0] and not days):            
#             days.pop(0)
#             count = count + 1
#         answer.append(count)
#     return answer


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
    
    count = 101
    
    for num1, num2 in zip(days, days[1:]):     
        if count == 101:
            if num1 >= num2:
                count = 2
            else:
                answer.append(1)
                count = 1
        else : 
            if num1 >= num2 :
                count = count+1
            else:
                answer.append(count)
                count = 1
    answer.append(count)
    
    return answer