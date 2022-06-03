def solution(stones, k):
    answer = 0
    emp = [0] * len(stones)
    print(stones)
    
    avail = [l+1 for l  in range(k)]
    print(avail)
        
    
    while(True): # 징검다리를 건너는 사람을 count하는 루프
        i = 0
        while(i == len(stones)):
        # 징검다리의 각 숫자를 확인하는 루프
            if not stones[i] > 0:
                stones[i] -= 1
                i += 1
            else:
                for K in avail:
                    if stones[i+K] > 0:
                        i += K
                        stones[K] -= 1
                        break
                return answer
            answer += 1
                
                
        
    print(stones)            
        
    return answer