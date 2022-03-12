# 힙 - 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while(scoville[0] < K):
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, fir + sec * 2)
        answer = answer + 1
        
        if(len(scoville)<2):
            if (scoville[0] >= K):
                return answer
            else:
                return -1
    
    return answer