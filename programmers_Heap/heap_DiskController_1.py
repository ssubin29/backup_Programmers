# 힙 - 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)

    heapq.heapify(jobs)
    
    fir_job = heapq.heappop(jobs)
    time = fir_job[0] + fir_job[1] # 시간의 초기값
    answer = time
    
    while(jobs):
        order_list = []
        heapq.heapify(order_list)
        
        for job in jobs:
            if (job[0] >= time):
                heapq.heappush(order_list,[job[1], 
                                           job[0], job[1],
                                          (job[0] - time) + job[1]])
            else:
                heapq.heappush(order_list,[time - job[0] + job[1], 
                                           job[0], job[1], job[1]])
            
        print(order_list)
            
        answer = answer + order_list[0][0]
        time = time + order_list[0][3]
        
        jobs.remove([order_list[0][1], order_list[0][2]])
        
    answer = answer // length
    
    return answer