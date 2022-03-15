# 힙 - 이중 우선순위 큐
import heapq
def solution(operations):
    answer = []
    
    operations_=[]
    for operation in operations:
        operations_.append([operation.split()[0], int(operation.split()[1])])
    print(operations_)
    
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
                if (max_heap[0]!=md_in_max_heap[0]):
                    pop = heapq.heappop(max_heap)  
                    heapq.heappush(md_in_max_heap, -pop)
                    
            elif operation[1] == -1 :
                if (min_heap[0]!=md_in_min_heap[0]):
                    pop = heapq.heappop(min_heap)
                    heapq.heappush(md_in_min_heap, pop)
                    
    print(max_heap)
    print(min_heap)
    
    return answer