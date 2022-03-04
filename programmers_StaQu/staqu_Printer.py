# 스택/큐 - 프린터

def solution(priorities, location):
    answer = 0
    order = []
    
    priorities_copy = priorities.copy()
    
    start_index = 0
    while(priorities_copy):
        count = 0
        
        max_value = max(priorities_copy)
        max_index = priorities.index(max_value)
        
        # 첫번째 루프 ( [바로 전 프린터가 멈춘 위치 :])
        for i in range(start_index,len(priorities)):
            if priorities[i] == max_value:
                count = count + 1
                order.append(i)
                
        if start_index != 0 :
             # 두번째 루프 ( [ : 바로 전 프린터가 멈춘 위치-1])
            for i in range(0,start_index):
                if priorities[i] == max_value:
                    count = count + 1
                    order.append(i)
                    
        for j in range(count):
            priorities_copy.remove(max_value)
            
        if(priorities_copy):
            start_index = max_index
            
    answer = order.index(location)
    #print(order)
    
    return answer+1