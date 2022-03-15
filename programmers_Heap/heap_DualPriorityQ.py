# 힙 - 이중 우선순위 큐
import heapq
def solution(operations):
    answer = []    
    operations_=[]
    for operation in operations:
        operations_.append([operation.split()[0], int(operation.split()[1])])
    
    max_heap = []
    min_heap = []
    md_in_max_heap = [] # md = must delete
    md_in_min_heap = []
    
    for operation in operations_:
        if operation[0] == "I":
            # 최소 힙
            heapq.heappush(min_heap, operation[1])
            # 최대 힙
            heapq.heappush(max_heap, -operation[1])
            
        elif operation[0] == "D":            
            if operation[1] == 1: 
                if not (max_heap):
                    break
                elif not (md_in_max_heap):
                    pop = heapq.heappop(max_heap)  
                    heapq.heappush(md_in_min_heap, -pop)
                    
                elif (max_heap[0]!=md_in_max_heap[0]):
                    pop = heapq.heappop(max_heap)  
                    heapq.heappush(md_in_min_heap, -pop)
                    
            else : # elif operation[1] == -1 :
                if not (min_heap):
                    break
                elif not (md_in_min_heap):
                    pop = heapq.heappop(min_heap)  
                    heapq.heappush(md_in_max_heap, -pop)
                elif (min_heap[0]!=md_in_min_heap[0]):
                    pop = heapq.heappop(min_heap)
                    heapq.heappush(md_in_max_heap, -pop)
        
        
        #print('max_heap은', max_heap, 'min_heap은', min_heap)
        #print('md_in_max_heap은', md_in_max_heap, 'md_in_min_heap은', md_in_min_heap)
    
    answers = []
    while(True):
        if not md_in_min_heap:
            break
        if (min_heap[0] != md_in_min_heap[0]):
            answers.append(heapq.heappop(min_heap))
        else:
            heapq.heappop(min_heap)
            heapq.heappop(md_in_min_heap)
    
    if answers:
        answer = [max(answers), min(answers)]
    else:
        answer = [0,0]
    
    
    return answer