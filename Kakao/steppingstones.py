# 2019 카카오 개발자 겨울 인턴십 - 징검다리 건너기

def solution(stones, k):
    answer = 0
    emp = [0] * len(stones)
    
    avail = [l+1 for l  in range(k)]
    
    
    while(answer < 3): # 징검다리를 건너는 사람을 count하는 루프
        i = 0
        while(i <= len(stones)-1):
        # 징검다리의 각 숫자를 확인하는 루프
            if stones[i] > 0:
                stones[i] -= 1
                i += 1
            else:
                avai = [i+K for K in avail if i+K <= len(stones)-1]
                if not (avai): # 마지막이라 더 건널 돌이 없을 때
                    if (len(stones)-1-i < k):
                        break
                    else:
                        print('도착지까지 ')
                        return answer
                for a in avai:                    
                    if stones[a] > 0:
                        i = a
                        break
                if a == avail[-1]:
                    print('앞에 돌이 있으나 디딜 수 없으므로 갈 수 없습니다')
                    return answer
        answer += 1
            
    return answer

print(solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))