# 힙 - 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = len(jobs)
    time = 0
    
    heapq.heapify(jobs)
    
    # 다음으로 선택받을 job의 조건
    # 1. job[0]이 일단 가장 작아야 한다.
    # 2. 그 다음으론 job[1]보다 ㅈ
    while(jobs):        
        job_list = [[job[1],job[0]]  for job in jobs if job[0] <= time]
        heapq.heapify(job_list)
        print(job_list) 
        
        time = time + job_list[0][0] + job_list[0][1]
            
        print(time)
        jobs.remove([job_list[0][1], job_list[0][0]])
    
    print(time)
    answer = time // answer
    
    return answer
