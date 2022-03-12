# 힙 - 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)

    heapq.heapify(jobs)
    
    fir_job = heapq.heappop(jobs)
    time = fir_job[0] + fir_job[1] # 시간의 초기값
    answer = time
    #job[0]의 값이 가장 작은 것 중에서 job[1]이 가장 작은 값
    
    # 다음으로 선택받을 job의 조건
    # 1번 경우 job[0]이 count보다 작거나 같다면 job[1]의 값만 가장 작으면 된다
    # 2번 경우 count보다 크다면 위와 같다. 
    # job[0]의 값이 가장 작은 것 중에서 job[1]이 가장 작은 값 (걍 heap에서 가장 작은 값)
    while(jobs):
        if jobs[0][0] > time:
            job = heapq.heappop(jobs)
            answer = answer + (time - job[0] + job[1]) 
            time = time + (job[0] + job[1])
            
        else:
            job_list = [[job[1],job[0]]  for job in jobs if job[0] <= time]
            job_list.sort()
            answer = answer + (time - job_list[0][1]) + job_list[0][0]
            time = time + job_list[0][0]
            jobs.remove([job_list[0][1],job_list[0][0]])
            
    answer = answer // length
    
    return answer