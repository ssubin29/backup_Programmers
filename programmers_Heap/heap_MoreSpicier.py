# 힙 - 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    
    scoville.sort()
    heapq.heapify(scoville)
    
    ret_val = heapq.heappop(scoville)
    print(ret_val)
    
    return answer